# CSL styles

Every style used by a bundled journal profile is stored here, so the kit builds and its tests run offline, and a submission's reference formatting cannot change because the upstream style was edited. Downloaded on 2026-09-23 from the official repository, https://github.com/citation-style-language/styles:

| File | Used by |
| --- | --- |
| `nlm-citation-sequence.csl` | `generic-icmje` (Vancouver, *Citing Medicine*) |
| `jornal-vascular-brasileiro.csl` | `jvb` (local derivative of NLM superscript: first three authors + et al. above six) |
| `obesity.csl` | `obesity` |
| `obesity-facts.csl` → `karger-journals.csl` | `obesity-facts` (dependent style and its parent) |
| `american-medical-association.csl` | `clinical-obesity`, `example-journal-b` |
| `international-journal-of-obesity.csl` → `nature-publishing-group-vancouver.csl` | `ijo` |
| `journal-of-clinical-medicine.csl` → `multidisciplinary-digital-publishing-institute.csl` | `jcm` |
| `cureus.csl` | `cureus` |

A profile that names a style not stored here downloads it on first use (network needed once) and keeps it here. Journal styles are often *dependent* (a pointer to a parent); `build.py` resolves the parent. If the download fails, the error says whether the style does not exist (HTTP 404) or the network is unavailable.

Find a journal's style at https://www.zotero.org/styles. CSL styles are licensed CC BY-SA 3.0 by their authors.
