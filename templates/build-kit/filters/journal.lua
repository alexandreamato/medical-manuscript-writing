--[[
Journal presentation layer. Content never changes here; only how it is shown.

Reads metadata written by build.py from the journal profile (`journal-build`):
  headings       map section id -> heading text for this journal
                 (e.g. abstract-results -> "Findings", methods -> "Patients and methods")
  unstructured   true -> drop abstract subheadings, keep the text
  mode           "full"      title page + manuscript
                 "blinded"   manuscript without any author information
                 "titlepage" title page only (for separate upload)
  word-counts    {abstract=, main=} computed by validate.py, printed on the title page
  omit           list of section ids to drop in this output (e.g. acknowledgments
                 in the blinded file)

Author metadata (metadata.yaml):
  author:
    - name: Ana Silva
      orcid: 0000-0000-0000-0000
      affiliations: [1, 2]
      corresponding: true
      email: ana@example.org
  affiliations:
    - id: 1
      name: Department ..., University ..., City, Country
]]

local S = pandoc.utils.stringify

local function lst(v)
  if v == nil then return {} end
  if type(v) == "table" and v.t == nil and #v > 0 then return v end
  if pandoc.utils.type(v) == "List" then return v end
  return {v}
end

local function title_page(meta)
  local blocks = pandoc.Blocks{}
  blocks:insert(pandoc.Para{pandoc.Strong(meta.title)})
  if meta["running-title"] then
    blocks:insert(pandoc.Para{pandoc.Str("Running title:"), pandoc.Space(), table.unpack(meta["running-title"])})
  end

  -- Affiliation numbering follows order of first appearance among authors.
  local aff_names, aff_num, aff_order = {}, {}, {}
  for _, a in ipairs(lst(meta.affiliations)) do aff_names[S(a.id)] = a.name end
  local names = pandoc.Inlines{}
  local corr
  for i, a in ipairs(lst(meta.author)) do
    if i > 1 then names:insert(pandoc.Str(",")); names:insert(pandoc.Space()) end
    local nm = type(a) == "table" and a.name or a
    names:extend(pandoc.Inlines(nm))
    local sups = {}
    for _, af in ipairs(lst(a.affiliations)) do
      local key = S(af)
      if not aff_num[key] then
        table.insert(aff_order, key)
        aff_num[key] = #aff_order
      end
      table.insert(sups, tostring(aff_num[key]))
    end
    if #sups > 0 then names:insert(pandoc.Superscript{pandoc.Str(table.concat(sups, ","))}) end
    if a.corresponding then corr = a end
  end
  blocks:insert(pandoc.Para(names))
  for _, key in ipairs(aff_order) do
    blocks:insert(pandoc.Para{pandoc.Superscript{pandoc.Str(tostring(aff_num[key]))},
                              table.unpack(pandoc.Inlines(aff_names[key] or ("[affiliation " .. key .. "]")))})
  end

  local orcids = pandoc.Blocks{}
  for _, a in ipairs(lst(meta.author)) do
    if a.orcid then
      orcids:insert(pandoc.Plain{pandoc.Str(S(a.name) .. ":"), pandoc.Space(),
        pandoc.Link(S(a.orcid), "https://orcid.org/" .. S(a.orcid))})
    end
  end
  if #orcids > 0 then
    blocks:insert(pandoc.Para{pandoc.Strong{pandoc.Str("ORCID")}})
    blocks:extend(orcids)
  end
  if corr then
    local c = {pandoc.Strong{pandoc.Str("Corresponding author:")}, pandoc.Space(), pandoc.Str(S(corr.name))}
    if corr.address then table.insert(c, pandoc.Str(", " .. S(corr.address))) end
    if corr.email then table.insert(c, pandoc.Str(". E-mail: " .. S(corr.email))) end
    blocks:insert(pandoc.Para(c))
  end
  local jb = meta["journal-build"] or {}
  local wc = jb["word-counts"]
  if wc then
    blocks:insert(pandoc.Para{pandoc.Str("Word count: abstract " .. S(wc.abstract or "?")
      .. "; main text " .. S(wc.main or "?") .. ".")})
  end
  if meta.keywords then
    local kws = {}
    for _, k in ipairs(lst(meta.keywords)) do table.insert(kws, S(k)) end
    blocks:insert(pandoc.Para{pandoc.Strong{pandoc.Str("Keywords:")}, pandoc.Space(),
                              pandoc.Str(table.concat(kws, "; "))})
  end
  return blocks
end

function Pandoc(doc)
  local jb = doc.meta["journal-build"] or {}
  local mode = S(jb.mode or "full")
  local headings = jb.headings or {}
  local omit = {}
  for _, id in ipairs(lst(jb.omit)) do omit[S(id)] = true end
  local unstructured = jb.unstructured == true

  local out = pandoc.Blocks{}
  local skipping = false
  local in_abstract = false
  for _, b in ipairs(doc.blocks) do
    if b.t == "Header" and b.level == 1 then
      skipping = omit[b.identifier] or false
      in_abstract = b.identifier == "abstract"
    elseif b.t == "Header" and b.level == 2 and omit[b.identifier] then
      skipping = true
    elseif b.t == "Header" and b.level == 2 and skipping and not omit[b.identifier] then
      skipping = false
    end
    if not skipping then
      if b.t == "Header" and headings[b.identifier] then
        b.content = pandoc.Inlines(S(headings[b.identifier]))
      end
      if not (unstructured and in_abstract and b.t == "Header" and b.level == 2) then
        out:insert(b)
      end
    end
  end

  if mode == "titlepage" then
    doc.blocks = title_page(doc.meta)
  elseif mode == "full" then
    local tp = title_page(doc.meta)
    tp:insert(pandoc.RawBlock("openxml", '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'))
    tp:extend(out)
    doc.blocks = tp
  else -- blinded: title only, no authors anywhere
    local tp = pandoc.Blocks{pandoc.Para{pandoc.Strong(doc.meta.title)}}
    tp:extend(out)
    doc.blocks = tp
  end
  -- The title page above replaces pandoc's own title/author block.
  doc.meta.title = nil
  doc.meta.author = nil
  doc.meta.date = nil
  doc.meta.subtitle = nil
  return doc
end
