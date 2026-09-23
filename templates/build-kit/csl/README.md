# CSL styles

`nlm-citation-sequence.csl` (Vancouver, *Citing Medicine*) is bundled so the kit builds offline. Any other style named in a journal profile (`"csl": "american-medical-association"`) is downloaded on first use from the official repository, https://github.com/citation-style-language/styles, and cached here. Journal-specific styles are often *dependent* (a pointer to a parent style); `build.py` resolves the parent automatically.

Find a journal's style at https://www.zotero.org/styles. CSL styles are licensed CC BY-SA 3.0 by their authors.
