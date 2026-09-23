--[[
Last filter, after citeproc: strip every metadata field from the output file.

pandoc writes leftover metadata to docProps/custom.xml (local paths such as
the CSL location, affiliations, e-mails). A blinded manuscript must not carry
them, and no submission file needs them. Only the language is kept.

It runs last on purpose: journal.lua chooses the content first (omitted
sections, title page), citeproc then numbers only the citations that remain,
and this filter removes the metadata citeproc needed.
]]

function Pandoc(doc)
  local lang = doc.meta.lang
  for k, _ in pairs(doc.meta) do doc.meta[k] = nil end
  doc.meta.lang = lang
  return doc
end
