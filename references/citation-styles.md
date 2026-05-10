# Citation Styles for Medical Manuscripts

Different journals require different citation styles. The first step before formatting any reference is to check the target journal's Instructions to Authors. **If the target journal has not yet been chosen, use Vancouver as the default**, because it is the recommended style of the International Committee of Medical Journal Editors (ICMJE) and is accepted by most major medical journals.

## Contents

1. [Decision Rule](#decision-rule)
2. [Major Citation Styles in Medical Publishing](#major-citation-styles-in-medical-publishing) — comparison table
3. [Vancouver (Default)](#vancouver--default-style-detailed) — full detail; in-text rules; reference-list format for journals, books, chapters, supplements, eLocators, newspapers, organisation reports; Generative AI handling; sample paragraph
4. [Other styles](#other-styles) — AMA, APA, Harvard, Chicago / Turabian, CSE; pointer to `references/citation-styles-detail.md`
5. [Reference-Manager Workflow](#reference-manager-workflow) — Zotero, Mendeley, EndNote, BibTeX; CSL style files
6. [Hard Rules That Apply Regardless of Style](#hard-rules-that-apply-regardless-of-style)
7. [Common Mistakes Caught at Final Review](#common-mistakes-caught-at-final-review)
8. [Quick Sanity Check Before Submission](#quick-sanity-check-before-submission)

## Decision Rule

```
1. Has a target journal been chosen?
   - YES -> Open the journal's "Instructions to Authors" or "Author Guidelines"
           page; format the references in the exact style required.
   - NO  -> Use Vancouver (ICMJE) as the working default. Reformat later
           once the target journal is chosen.
2. When Instructions are silent on a detail (e.g., DOI placement,
   "et al." threshold, "in press" handling), default to ICMJE
   Recommendations: https://www.icmje.org/recommendations/
```

## Major Citation Styles in Medical Publishing

| Style | Family | In-text format | Reference list order | Common journals |
| --- | --- | --- | --- | --- |
| **Vancouver (ICMJE)** | Numeric | `[1]` or `(1)` | Order of first appearance | NEJM, Lancet, BMJ, Annals of Internal Medicine, Nature Medicine, JAMA family (with AMA variations), Cochrane Reviews, most specialty journals |
| **AMA (10th–11th ed.)** | Numeric | Superscript number `¹` | Order of first appearance | JAMA, JAMA Internal Medicine, Archives of *, many AMA-affiliated journals |
| **APA (7th ed.)** | Author-date | `(Smith, 2020)` | Alphabetical | Some psychology, public health, nursing, and medical-education journals |
| **Harvard** | Author-date | `(Smith 2020)` | Alphabetical | Generic; varies by publisher; common in some UK and Australian health journals |
| **Chicago / Turabian** | Notes-Bibliography or Author-Date | Footnote or `(Smith 2020)` | Alphabetical (Author-Date) or by note order (Notes-Bibliography) | Some humanities-leaning health journals |
| **MLA** | Author-page | `(Smith 23)` | Alphabetical | Rare in medical research |
| **CSE (Council of Science Editors)** | Citation-sequence (numeric) or Name-Year | `[1]` or `(Smith 2020)` | Order of appearance or alphabetical | Some general science journals |
| **Nature** | Numeric (superscript) | `¹` | Order of first appearance | Nature, Nature Medicine variations |
| **Cell** | Author-date | `(Smith et al., 2020)` | Alphabetical | Cell, Cell Reports, Cell Reports Medicine |

## Vancouver — Default Style (Detailed)

Vancouver is the **dominant** citation style for medical journals (NEJM, Lancet, BMJ, JAMA, Annals, Nature Medicine, Cochrane Reviews, and most specialty journals). It is recommended by ICMJE and aligns closely with the AMA Manual of Style 11th edition. Vancouver is the **default** style of this skill.

Key facts:

1. **Numeric citation system.** References are numbered in the **order of first appearance** in the text, and the same number is reused on every subsequent citation of that source.
2. **Reference list is in numeric order**, not alphabetical.
3. **Superscript numerals** are the default in-text format in modern Vancouver (and AMA). Some journals use bracketed numerals; check the journal's Instructions to Authors.
4. **Journal titles are abbreviated** per the NLM/PubMed list (verify each abbreviation).
5. **DOIs are mandatory** when available, formatted as metadata (`doi:10.xxxx/xxxxx`), not as a hyperlink.

### In-Text Format

#### Superscript (most common in modern Vancouver / AMA)

```
This finding has been confirmed by several studies.¹
The authors describe...²,³
Multiple cohorts have demonstrated this association.¹,⁴⁻⁶,⁹
```

#### Bracketed (older Vancouver, still accepted by some journals)

```
This finding has been confirmed by several studies [1].
The authors describe... [2,3]
Multiple cohorts have demonstrated this association [1, 4-6, 9].
```

#### Parenthetical (rare but acceptable)

```
This finding has been confirmed (1).
```

### Multiple-Citation Rules

1. **Two non-consecutive citations:** join with a comma, no space — `1,3`.
2. **Three or more consecutive citations:** join the first and last with a hyphen — `4-7`. Do not write `4,5,6,7`.
3. **Mixed consecutive and non-consecutive:** combine — `1,3-5,8`.

### Placement Around Punctuation

1. **After an author name** in narrative text: `Johnson explains¹ that ...`
2. **To the right of commas and full stops** (after them): `This is widely accepted.²`
3. **To the left of colons and semicolons** (before them): `The study lists three factors¹: motivation, ...`

### Page Numbers (Optional, Used for Direct Quotes)

When citing different pages of the same source at different points, place the page number in parentheses immediately after the superscript. Use `p` for one page and `pp` for multiple pages:

```
... pain response should be considered.⁸(p83),⁹,¹²(pp3,5)
```

This avoids creating multiple reference-list entries for the same source.

### Author Names When Mentioned in Text

1. **One author:** surname only — `Smith reported ...¹`
2. **Two authors:** both surnames joined by `and` — `Avery and Williams highlighted ...¹`
3. **Three or more authors:** first author surname plus `et al.` — `Azar et al. reported ...¹`

Do not italicize `et al.` in Vancouver/AMA (some style guides italicize it; not Vancouver).

### Author Names in the Reference List

1. **Format:** surname followed by initials with no periods between letters and no space — `Smith JA`, `Khan FM`. Multiple authors are separated by commas.
2. **One to six authors:** list **all** authors in classical Vancouver. (AMA 11 and many modern journals now also accept "first three then et al."; verify with the journal.)
3. **More than six authors (modern AMA-aligned Vancouver):** list the first **three** authors then `et al.` Example: `Smith BM, Kirby M, Hoffman EA, et al.`.
4. **Older Vancouver / ICMJE classical:** list the first **six** authors then `et al.` Verify which the target journal uses.
5. **Organization as author:** spell out in full — `Australian Institute of Health and Welfare.` `World Health Organization.`. Do not abbreviate the organization name in the reference list.
6. **No author available:** check whether an organization acted as author. If not, list the title first.

### Title Capitalization

1. **Article and chapter titles:** **sentence case** — capitalize only the first word, proper nouns, abbreviations, and named clinical trials or study groups. Example: `Community health worker home visits for adults with uncontrolled asthma: the HomeBASE Trial randomized clinical trial.` (Note `HomeBASE Trial` is capitalized as a named trial.)
2. **Journal and book titles:** **headline (title) case** — capitalize all significant words. Italicize.

### Digital Object Identifiers (DOIs)

1. **Required when available.** A DOI is preferable to a URL because it is permanent.
2. **Format as metadata, not as a hyperlink:** `doi:10.1001/jamainternmed.2014.6353` (no `https://doi.org/` prefix in classical Vancouver/AMA; AMA 11 keeps the `doi:` form).
3. **For online sources without a DOI:** include the URL with an access date (`Accessed Month Day, Year. URL`).

### Reference List Format — Journal Article

```
Author Surname Author Initials. Title of article: subtitle. Abbreviated Journal Title in Italics. Year;Volume(Issue):Page range. doi:DOI
```

Worked examples:

```
1. Solomon SD, McMurray JJV, Anand IS, et al. Angiotensin-neprilysin
   inhibition in heart failure with preserved ejection fraction. N Engl
   J Med. 2019;381(17):1609-1620. doi:10.1056/NEJMoa1908655

2. Naghavi M, Abajobir AA, Abbafati C, et al. Global, regional, and
   national age-sex specific mortality for 264 causes of death,
   1980-2016: a systematic analysis for the Global Burden of Disease
   Study 2016. Lancet. 2017;390(10100):1151-1210.
   doi:10.1016/S0140-6736(17)32152-9

3. Boatwright KD, Sperry ML. Accuracy of medical marijuana claims
   made by popular websites. J Pharm Pract. 2020;33(4):457-464.
   doi:10.1177/0897190018818907
```

Detailed rules:

1. **Article title:** sentence case; ends with a period.
2. **Journal abbreviation:** italicized; per the NLM list. Look up at https://pubmed.ncbi.nlm.nih.gov/ — click *Journals* under *Explore* and enter the full title, or check the Citing Medicine appendix B at https://www.ncbi.nlm.nih.gov/books/NBK7253/. See `references/pubmed-essentials.md` for the full lookup workflow.
3. **Year, volume, issue, pages:** `Year;Volume(Issue):Pages.` — no space before the issue parenthesis; no space between volume and issue.
4. **Page range:** abbreviate the second number when redundant — `1151-1210` or `1151-210`, per journal preference. Most modern journals keep the full second number for clarity.
5. **DOI:** end with `doi:` prefix; no trailing period in classical Vancouver (some journals add one).

### Reference List Format — Journal Article: Special Cases

**Advanced online publication (ahead of print):**

```
4. Kumar D, Warsha FN, Helmstetter N, Gupta V. Efficacy and safety of
   direct oral anticoagulants for treatment of left ventricular
   thrombus; a systematic review. Acta Cardiol. Published online
   May 10, 2021. doi:10.1080/00015385.2021.1901024
```

Replace volume, issue, and pages with `Published online Month Day, Year`.

**Article in a supplement:**

```
5. Bochenek SH, Fugit AM, Cook AM, Smith KM. Pharmacy residents'
   perceptions of preceptors as role models. Am J Health Syst Pharm.
   2016;73(11)(suppl 3):S94-S99. doi:10.2146/ajhp150661
```

Add `(suppl X)` after the issue. Page numbers retain any prefix letter (e.g., `S94-S99`).

**Article number / eLocator (online-only journals like PLOS ONE):**

```
6. Eades SJ, Banks E. 50 years since citizenship: successes and
   challenges in Indigenous health. Public Health Res Pract.
   2017;27(4):e2741730. doi:10.17061/phrp2741730
```

Use the article number in place of the page range.

**Newspaper article:**

```
7. Titelius R. War not wasted on health. The West Australian.
   March 31, 2019;Confidential:33.
```

```
8. Careful, medicines can also be poisons. The Australian. August 25,
   2020;Commentary:10. Accessed November 6, 2020.
   https://www-proquest-com/docview/2436658973
```

For print newspapers, omit the access date and URL. For unsigned articles (no author), list the article title first.

### Reference List Format — Book

```
Author Surname Author Initials. Title of Book in Italics. # ed. Publisher; Publication Year. Accessed Month Day, Year. doi:DOI or URL
```

Examples:

```
9. Khan MG. Cardiac Drug Therapy. 8th ed. Humana Press; 2015.
   Accessed October 10, 2018. doi:10.1007/978-1-61779-962-4

10. Hansen V, Horsfall J. Noongar Bush Tucker: Bush Food Plants and
    Fungi of the South-West of Western Australia. UWA Publishing;
    2019.
```

Rules:

1. **Edition** (other than first) immediately after the title — `8th ed.`
2. **Publisher; Year** — semicolon between publisher and year.
3. **Print book:** omit access date and URL/DOI.
4. **Online or e-book:** add `Accessed Month Day, Year. doi:` or URL.

### Reference List Format — Chapter in an Edited Book

```
Chapter Author Surname Initials. Title of chapter. In: Editor Surname Editor Initials, ed. Title of Book in Italics. # ed. Publisher; Year:Chapter page range. Accessed Month Day, Year. doi:DOI or URL
```

Example:

```
11. Riddle M, Taylor WD. Structural changes in the aging brain. In:
    Etkin A, Hantke N, O'Hara R, eds. Handbook of Mental Health and
    Aging. 3rd ed. Elsevier; 2020:59-70. Accessed November 6, 2020.
    http://ebookcentral.proquest.com/lib/curtin/detail.action?docID=6183701
```

### Reference List Format — Organization Report

```
12. Australian Institute of Health and Welfare. Australian Bushfires
    2019-2020: Exploring the Short-Term Health Impacts. Australian
    Institute of Health and Welfare; 2020. PHE 276. Accessed
    November 26, 2020. https://www.aihw.gov.au/...
```

Include any report number or catalogue number after the year.

### Reference List Format — Generative AI

Generative-AI tools (ChatGPT, Claude, Gemini, etc.) are **non-recoverable sources** — the content they produce is not accessible to anyone other than the person who generated it. Vancouver/AMA practice (aligned with the Curtin / AMA-derived guidance):

1. **No entry in the reference list.**
2. **In-text only**, in parentheses, with the format: `(Communicator, type of communication, Month Day, Year)`.

Example:

```
Fall reduction strategies can only be successful if a multi-faceted approach
is adopted, one which addresses both personal and environmental risk factors
(ChatGPT, response to question from author, February 22, 2023).
```

A **declaration must be included** in the manuscript (typically in Methods or after the reference list — verify the journal's policy). The declaration states:

1. The AI tool used (with URL/version).
2. How it was used (research, idea generation, clarification, structure, writing assistance, other).
3. The exact prompts.

ICMJE position: AI cannot be an author; the human authors take full responsibility. See `references/ethics-and-integrity.md`.

### Sample Vancouver Paragraph and Reference List

A short worked example showing in-text superscripts, multiple-citation hyphens, page-number citation, and the matching reference list:

```
Body text:

In Australia, falls are a leading cause of injury-related hospitalisation,
with the elderly representing the majority of cases.¹ Accidental falls in
older persons can have a detrimental effect on their mental wellbeing.²,³
"The psychological aspects, especially fear of falling, loss of confidence
and increased anxiety, can be more disabling than the physical ones."³(p18)
Effective programs to reduce the incidence of falls are therefore
important.⁴⁻⁶

References:

1. Australian Institute of Health and Welfare. Trends in Hospitalised Injury,
   Australia: 2007-08 to 2016-17. Australian Institute of Health and Welfare;
   2019. INJCAT 204. Accessed November 26, 2020.
   https://www.aihw.gov.au/reports/injury/trends-in-hospitalised-injury-2007-08-to-2016-17

2. Lee F, Mackenzie L, James C. Perceptions of older people living in the
   community about their fear of falling. Disabil Rehabil. 2008;30(23):1803-
   1811. doi:10.1080/09638280701669508

3. Barker W. Assessment and prevention of falls in older people. Nurs Older
   People. 2014;26(6):18-24. doi:10.7748/nop.26.6.18.e586

4. Sinclair AJ, Morley JE, Vellas B, eds. Pathy's Principles and Practice of
   Geriatric Medicine. 5th ed. John Wiley & Sons; 2012. Accessed October 10,
   2018. doi:10.1002/9781119952930

5. Reznik D. Fall prevention. Am J Nurs. 2013;113(7):12.
   doi:10.1097/01.NAJ.0000431897.51118.69

6. Jones D, Whitaker T. Preventing falls in older people: assessment and
   interventions. Nurs Stand. 2011;25(52):50-55.
```

### Reference List Format — Online-Only Article / Website

```
4. Author AA. Title. Site name. Year [accessed YYYY MMM DD]. URL.
```

Example:

```
4. World Health Organization. WHO Coronavirus (COVID-19) Dashboard.
   Geneva: World Health Organization; 2024 [accessed 2024 May 10].
   https://covid19.who.int.
```

### Reference List Format — Preprint

```
5. Author AA, Author BB. Title. Server [Preprint]. Year. DOI.
```

Example:

```
5. Smith AB, Jones CD. Mechanism of action of compound X. medRxiv [Preprint].
   2024. doi:10.1101/2024.01.01.24300000.
```

Mark preprints clearly as `[Preprint]` so reviewers know the source has not been peer-reviewed.

### Reference List Format — Trial Registry Entry

```
6. Author or Sponsor. Trial title. ClinicalTrials.gov identifier: NCTxxxxxxxx.
   Year [updated YYYY MMM DD; accessed YYYY MMM DD]. URL.
```

### Reference List Format — Conference Abstract

```
7. Author AA, Author BB. Title [abstract]. Conference Name; Year MMM DD-DD; City, State or Country. Abstract number.
```

### Reference List Format — Software / Code

```
8. Author AA. Software name. Version. Publisher; Year. URL or DOI.
```

### "In Press" and "Forthcoming"

For accepted but not-yet-published articles:

```
9. Author AA, Author BB. Title. Journal Abbreviation. Forthcoming Year.
```

Use only for papers that have been formally accepted. ICMJE prefers "Forthcoming" over "In press".

## Other styles

For full detail on AMA (JAMA Network), APA (7th ed.), Harvard, Chicago / Turabian (18th edition, Author-Date and Notes-Bibliography variants), and CSE (Council of Science Editors), see **`references/citation-styles-detail.md`**.

Brief orientation:

- **AMA** — numeric superscript, similar to Vancouver; default for the JAMA Network.
- **APA 7** — author-date; common in health-sciences, behavioural, public-health, nursing, and medical-education journals.
- **Harvard** — generic author-date; varies by publisher, always follow the journal's worked example exactly.
- **Chicago / Turabian 18** — Author-Date variant is the one usually used in medical contexts; Notes-Bibliography variant uses footnotes.
- **CSE** — three variants (Citation-Sequence, Citation-Name, Name-Year); confirm which the journal requires.

The remainder of this file focuses on the Vancouver default plus rules that apply across all styles.

<!-- Anchor preserved for cross-references that still point to legacy section IDs. -->
<a id="chicago--turabian-18th-edition"></a>
<a id="ama-jama-network"></a>
<a id="apa-7th-ed"></a>
<a id="harvard"></a>
<a id="cse-council-of-science-editors"></a>

## Reference-Manager Workflow

Use a reference manager from the start of the project. Manually formatting references is error-prone and a major source of citation-order errors.

| Tool | Strengths | Notes |
| --- | --- | --- |
| **Zotero** (free, open source) | Excellent CSL style support; browser connectors; group libraries | Recommended default |
| **Mendeley** (free; Elsevier) | PDF annotation; cloud sync | Style support good; ownership concerns |
| **EndNote** (paid; Clarivate) | Industry standard at many institutions; deep Word integration | Many institutional licenses |
| **Paperpile** (paid; web) | Tight Google Docs and Google Scholar integration | Good for collaborative manuscripts |
| **BibTeX / BibLaTeX** | Standard in LaTeX workflows | Use with `biblatex-vancouver`, `biblatex-ama`, or `biblatex-apa` styles |

### CSL Style Files

Most reference managers support CSL (Citation Style Language) files. Find styles at https://www.zotero.org/styles. Download the exact style required by the target journal:

- "Vancouver (Brackets)"
- "Vancouver (Superscript)"
- "American Medical Association 11th edition"
- "APA 7th edition"
- "BMJ Journals"
- "The Lancet"
- "New England Journal of Medicine"
- "Cell"
- "Nature"
- Specific journal styles when available

### Practical Workflow

1. Set up a reference manager and connect it to Word, Google Docs, or LaTeX.
2. Save every paper as you read it; never cite a paper you have not read.
3. Cite as you write. Insert citations as fields, not as plain text.
4. Use Vancouver during drafting if the journal is undecided.
5. Once the journal is chosen, change the CSL style; the manager will reformat the entire reference list automatically.
6. Before submission, spot-check 5 to 10 references against the original PubMed or DOI record. Reference managers occasionally import errors.

## Hard Rules That Apply Regardless of Style

1. **Never fabricate a reference.** Every citation must point to a real, verifiable publication. If a fact lacks a source, mark it `[CITATION NEEDED]` and stop.
2. **Cite each table and figure in the text in order of first appearance.** This applies in every style.
3. **Numeric styles: references are numbered by the order of first mention.** After every revision pass, verify ascending order.
4. **Author-date styles: reference list is alphabetical** by first author surname; multiple works by the same first author are ordered chronologically.
5. **Use the journal's exact abbreviation list** (typically NLM PubMed abbreviations for Vancouver/AMA).
6. **Verify every reference** against PubMed or DOI before submission. Common errors: wrong year, missing DOI, transposed author names, wrong journal abbreviation.
7. **Do not cite a review when a primary source is available** for a rated recommendation.
8. **Mark preprints, conference abstracts, and "in press" papers explicitly.**
9. **Limit references to those that contribute** to the manuscript. Top medical journals typically expect 30 to 50 references for an original article, 10 to 20 for a case report or letter, 50 to 150+ for a systematic review.
10. **Each in-text citation has a matching reference-list entry, and vice versa.** Run this check at the end.

## Common Mistakes Caught at Final Review

1. Citation 23 appears in the text before citation 18 (numeric styles).
2. Reference 14 cites "Smith 2018" but the in-text citation says "Smith 2019".
3. DOIs missing or broken.
4. Author initials transposed.
5. Journal name spelled out in some references and abbreviated in others.
6. "et al." used inconsistently (after 3 authors here, after 6 there).
7. URLs to articles instead of DOIs.
8. Pre-print version cited when the peer-reviewed version is now available.
9. References to retracted papers without acknowledgment of the retraction.
10. Reference-list entries with no in-text citation, or vice versa.

## Quick Sanity Check Before Submission

1. Style matches the journal's Instructions to Authors exactly.
2. Numeric styles: ascending order verified by scanning top-to-bottom.
3. Author-date styles: alphabetical order verified.
4. Every reference has a DOI when one exists.
5. Every reference has been spot-checked against PubMed or the journal record.
6. No fabricated, duplicated, or unverifiable references.
7. Tables and figures cited in order of first appearance.
8. Reference manager re-runs cleanly without "broken citation" errors.

## See also

- `references/citation-styles-detail.md` — Full detail on AMA, APA 7, Harvard, Chicago / Turabian 18 (Author-Date and Notes-Bibliography), and CSE
- `references/manuscript-conventions.md` — Journal-specific formatting requirements (margins, line numbers, anonymisation)
- `references/pubmed-essentials.md` — Looking up journal abbreviations against the NLM list; verifying a reference against the PubMed record
- `references/research-apis.md` — Crossref, OpenAlex, NCBI E-utilities, OpenCitations for programmatic reference verification
- `references/ethics-and-integrity.md` — AI disclosure, ICMJE position on AI authorship
- `references/common-mistakes.md` — Speed audit including citation order and reference list defects
- `references/paper-review.md` — Formal pre-submission checklist including reference verification
