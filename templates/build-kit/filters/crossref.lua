--[[
Cross-references for figures and tables, numbered by FIRST MENTION in the
text (ICMJE: Table 1 is the first table cited, not the first one written).

Source syntax
  Figure:  ::: {#fig:flow}
           ![Participant flow.](figures/flow.png)
           :::
           (or simply  ![Participant flow.](figures/flow.png){#fig:flow})
  Table:   ::: {#tbl:baseline}
           Table: Baseline characteristics.

           | ... pipe table ... |
           :::
  Mention: @fig:flow  ->  "Figure 1"      [@tbl:baseline] -> "Table 1"
           -@fig:flow ->  "1"             [@fig:a; @fig:b] -> "Figures 1 and 2"
  Prefixes: fig, tbl, sfig (Supplementary Figure), stbl (Supplementary Table).

Placement (set by build.py from the journal profile, metadata `xref`):
  xref.tables  = "inline" | "end"            tables after the reference list
  xref.figures = "inline" | "legends-at-end" figures removed, legends listed
                                              at the end, images shipped as
                                              separate files by build.py

Numbering must match scripts/common.py:float_numbers().
]]

local NAMES = {
  fig  = {"Figure", "Figures"},
  tbl  = {"Table", "Tables"},
  sfig = {"Supplementary Figure", "Supplementary Figures"},
  stbl = {"Supplementary Table", "Supplementary Tables"},
}

local nums = {}
local counters = {}

local function kind(id)
  local k = id and id:match("^(%a+):")
  if k and NAMES[k] then return k end
  return nil
end

local function assign(id)
  if nums[id] then return end
  local k = kind(id)
  counters[k] = (counters[k] or 0) + 1
  nums[id] = counters[k]
end

local function page_break()
  return pandoc.RawBlock("openxml", '<w:p><w:r><w:br w:type="page"/></w:r></w:p>')
end

local function label(id)
  return NAMES[kind(id)][1] .. " " .. tostring(nums[id] or "??")
end

-- Prefix "Figure 1." to a caption (list of blocks); returns new blocks.
local function prefix_caption(blocks, id)
  local lead = pandoc.Strong{pandoc.Str(label(id) .. ".")}
  if #blocks == 0 then return {pandoc.Plain{lead}} end
  local first = blocks[1]
  if first.content then
    first.content:insert(1, pandoc.Space())
    first.content:insert(1, lead)
  end
  return blocks
end

local function caption_blocks(el)
  -- Figure / Table caption, or a Div wrapping one of them.
  if el.t == "Figure" or el.t == "Table" then return el.caption.long end
  if el.t == "Div" then
    for _, b in ipairs(el.content) do
      if b.t == "Figure" or b.t == "Table" then return b.caption.long end
    end
  end
  return nil
end

local function label_float(el)
  local id = el.identifier
  if not kind(id) then return nil end
  if el.t == "Figure" or el.t == "Table" then
    el.caption.long = prefix_caption(el.caption.long, id)
    return el
  end
  for i, b in ipairs(el.content) do
    if b.t == "Figure" or b.t == "Table" then
      b.caption.long = prefix_caption(b.caption.long, id)
      el.content[i] = b
      return el
    end
    -- An image without Figure wrapper (paragraph with one image).
    if b.t == "Para" and #b.content == 1 and b.content[1].t == "Image" then
      local img = b.content[1]
      local cap = prefix_caption({pandoc.Plain(img.caption)}, id)
      el.content[i] = pandoc.Figure({pandoc.Plain{img}}, {long = cap}, pandoc.Attr(""))
      return el
    end
  end
  return el
end

function Pandoc(doc)
  local meta = doc.meta.xref or {}
  local tables_mode = pandoc.utils.stringify(meta.tables or "inline")
  local figures_mode = pandoc.utils.stringify(meta.figures or "inline")

  -- Pass 1: first mentions, then floats never mentioned, in document order.
  doc:walk({traverse = "topdown", Cite = function(c)
    for _, cit in ipairs(c.citations) do
      if kind(cit.id) then assign(cit.id) end
    end
  end})
  doc:walk({traverse = "topdown",
    Div = function(d) if kind(d.identifier) then assign(d.identifier) end end,
    Figure = function(f) if kind(f.identifier) then assign(f.identifier) end end,
    Table = function(t) if kind(t.identifier) then assign(t.identifier) end end,
  })

  -- Pass 2: replace mentions.
  doc = doc:walk({Cite = function(c)
    local ids = {}
    for _, cit in ipairs(c.citations) do
      if kind(cit.id) then table.insert(ids, cit) else return nil end
    end
    local k = kind(ids[1].id)
    local numbers = {}
    for _, cit in ipairs(ids) do table.insert(numbers, tostring(nums[cit.id] or "??")) end
    local joined
    if #numbers == 1 then joined = numbers[1]
    elseif #numbers == 2 then joined = numbers[1] .. " and " .. numbers[2]
    else joined = table.concat(numbers, ", ", 1, #numbers - 1) .. ", and " .. numbers[#numbers] end
    if ids[1].mode == "SuppressAuthor" then return pandoc.Str(joined) end
    local name = NAMES[k][#numbers == 1 and 1 or 2]
    local out = pandoc.Inlines{}
    local words = {}
    for w in (name .. " " .. joined):gmatch("%S+") do table.insert(words, w) end
    for i, w in ipairs(words) do
      if i > 1 then out:insert(pandoc.Space()) end
      out:insert(pandoc.Str(w))
    end
    return out
  end})

  -- Pass 3: label captions; move floats if the journal wants them at the end.
  local end_tables, legends = {}, {}
  local body = pandoc.Blocks{}
  for _, b in ipairs(doc.blocks) do
    local id = b.identifier
    local k = (b.t == "Div" or b.t == "Figure" or b.t == "Table") and kind(id) or nil
    if k then
      b = label_float(b)
      if (k == "tbl" or k == "stbl") and tables_mode == "end" then
        table.insert(end_tables, {n = nums[id], k = k, b = b})
      elseif (k == "fig" or k == "sfig") and figures_mode == "legends-at-end" then
        table.insert(legends, {n = nums[id], k = k, caption = caption_blocks(b) or {}})
      else
        body:insert(b)
      end
    else
      body:insert(b)
    end
  end
  table.sort(end_tables, function(a, b) return a.k == b.k and a.n < b.n or a.k < b.k end)
  table.sort(legends, function(a, b) return a.k == b.k and a.n < b.n or a.k < b.k end)

  for _, t in ipairs(end_tables) do
    body:insert(page_break())
    body:insert(t.b)
  end
  if #legends > 0 then
    body:insert(page_break())
    body:insert(pandoc.Header(1, "Figure legends", pandoc.Attr("figure-legends")))
    for _, l in ipairs(legends) do
      for _, cb in ipairs(l.caption) do body:insert(pandoc.Para(cb.content or {})) end
    end
  end
  doc.blocks = body
  return doc
end
