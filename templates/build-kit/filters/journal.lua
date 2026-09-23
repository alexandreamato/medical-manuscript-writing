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
  titlepage-sections  section ids printed on the title page instead of the text
                 (J Vasc Bras: ethics, conflicts, funding, data availability, contributions)
  keywords-after-abstract  print "Keywords:" after each abstract (and the
                 second-language list after `abstract-alt`) instead of on the title page

Second language (metadata): title-alt, keywords-alt, lang-alt; the second
abstract is the section {#abstract-alt}.

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

-- Title-page labels in the manuscript's language (metadata `lang`).
local LABELS = {
  en = {running = "Running title", corr = "Corresponding author", email = "E-mail",
        wc = "Word count: abstract %s; main text %s.", kw = "Keywords"},
  pt = {running = "Título curto", corr = "Autor correspondente", email = "E-mail",
        wc = "Contagem de palavras: resumo %s; texto %s.", kw = "Palavras-chave"},
  es = {running = "Título corto", corr = "Autor de correspondencia", email = "Correo electrónico",
        wc = "Recuento de palabras: resumen %s; texto %s.", kw = "Palabras clave"},
}

local function labels(meta)
  local code = (meta.lang and S(meta.lang) or "en"):match("^(%a+)") or "en"
  return LABELS[code] or LABELS.en
end

local function title_page(meta)
  local L = labels(meta)
  local blocks = pandoc.Blocks{}
  blocks:insert(pandoc.Para{pandoc.Strong(meta.title)})
  if meta["title-alt"] then blocks:insert(pandoc.Para{pandoc.Strong(meta["title-alt"])}) end
  if meta["running-title"] then
    blocks:insert(pandoc.Para{pandoc.Str(L.running .. ":"), pandoc.Space(), table.unpack(meta["running-title"])})
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
    local c = {pandoc.Strong{pandoc.Str(L.corr .. ":")}, pandoc.Space(), pandoc.Str(S(corr.name))}
    if corr.address then table.insert(c, pandoc.Str(", " .. S(corr.address))) end
    if corr.email then table.insert(c, pandoc.Str(". " .. L.email .. ": " .. S(corr.email))) end
    blocks:insert(pandoc.Para(c))
  end
  local jb = meta["journal-build"] or {}
  local wc = jb["word-counts"]
  if wc then
    blocks:insert(pandoc.Para{pandoc.Str(string.format(L.wc, S(wc.abstract or "?"), S(wc.main or "?")))})
  end
  if meta.keywords then
    local kws = {}
    for _, k in ipairs(lst(meta.keywords)) do table.insert(kws, S(k)) end
    blocks:insert(pandoc.Para{pandoc.Strong{pandoc.Str(L.kw .. ":")}, pandoc.Space(),
                              pandoc.Str(table.concat(kws, "; "))})
  end
  return blocks
end

-- Blocks of the section with identifier `id` (its header and everything up to
-- the next header of the same or higher level).
local function section_blocks(blocks, id)
  local out, level = pandoc.Blocks{}, nil
  for _, b in ipairs(blocks) do
    if level then
      if b.t == "Header" and b.level <= level then break end
      out:insert(b)
    elseif b.t == "Header" and b.identifier == id then
      level = b.level
      out:insert(b)
    end
  end
  return out
end

local function keywords_para(label, kws)
  local list = {}
  for _, k in ipairs(lst(kws)) do table.insert(list, S(k)) end
  if #list == 0 then return nil end
  return pandoc.Para{pandoc.Strong{pandoc.Str(label .. ":")}, pandoc.Space(),
                     pandoc.Str(table.concat(list, "; ") .. ".")}
end

local function titles(meta)
  local b = pandoc.Blocks{pandoc.Para{pandoc.Strong(meta.title)}}
  if meta["title-alt"] then b:insert(pandoc.Para{pandoc.Strong(meta["title-alt"])}) end
  return b
end

function Pandoc(doc)
  local jb = doc.meta["journal-build"] or {}
  local mode = S(jb.mode or "full")
  local headings = jb.headings or {}
  local omit = {}
  for _, id in ipairs(lst(jb.omit)) do omit[S(id)] = true end
  local unstructured = jb.unstructured == true
  local kw_after = jb["keywords-after-abstract"] == true
  local heading_of = function(id) return headings[id] and S(headings[id]) or nil end

  local out = pandoc.Blocks{}
  local skip_level = nil   -- level of the omitted section being skipped
  local in_abstract = nil  -- "abstract" / "abstract-alt" while inside one
  local function close_abstract()
    if kw_after and in_abstract then
      local p = in_abstract == "abstract"
        and keywords_para(S(jb["keywords-label"] or "Keywords"), doc.meta.keywords)
        or keywords_para(S(jb["keywords-label-alt"] or "Keywords"), doc.meta["keywords-alt"])
      if p then out:insert(p) end
    end
    in_abstract = nil
  end

  for _, b in ipairs(doc.blocks) do
    if b.t == "Header" then
      if skip_level and b.level <= skip_level then skip_level = nil end
      if b.level == 1 then
        close_abstract()
        if b.identifier == "abstract" or b.identifier == "abstract-alt" then in_abstract = b.identifier end
      end
      if not skip_level and omit[b.identifier] then skip_level = b.level end
    end
    if not skip_level then
      if b.t == "Header" and heading_of(b.identifier) then
        b.content = pandoc.Inlines(heading_of(b.identifier))
      end
      if not (unstructured and in_abstract and b.t == "Header" and b.level == 2) then
        out:insert(b)
      end
    end
  end
  close_abstract()

  if kw_after then doc.meta.keywords = nil end  -- printed after the abstracts, not on the title page

  if mode == "titlepage" then
    local tp = title_page(doc.meta)
    for _, id in ipairs(lst(jb["titlepage-sections"])) do
      local sec = section_blocks(doc.blocks, S(id))
      for _, b in ipairs(sec) do
        if b.t == "Header" and heading_of(b.identifier) then b.content = pandoc.Inlines(heading_of(b.identifier)) end
      end
      tp:extend(sec)
    end
    doc.blocks = tp
  elseif mode == "full" then
    local tp = title_page(doc.meta)
    tp:insert(pandoc.RawBlock("openxml", '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'))
    tp:extend(out)
    doc.blocks = tp
  else -- blinded: titles only, no authors anywhere
    local tp = titles(doc.meta)
    tp:extend(out)
    doc.blocks = tp
  end
  -- The title page above replaces pandoc's own title/author block, and nothing
  -- else from the metadata may reach the file: pandoc writes leftover fields to
  -- docProps/custom.xml (local paths, affiliations, e-mails), which a blinded
  -- manuscript must not carry. Only the language is kept.
  local lang = doc.meta.lang
  for k, _ in pairs(doc.meta) do doc.meta[k] = nil end
  doc.meta.lang = lang
  return doc
end
