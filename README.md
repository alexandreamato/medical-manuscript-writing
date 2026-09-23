# Medical Manuscript Writing: Skill

A Claude skill for writing and revising medical and biomedical manuscripts of any type (original research, systematic review, meta-analysis, narrative or evidence-based clinical review, case report, brief report), from title to response to reviewers.

**Author:** Alexandre Campos Moraes Amato (ORCID [0000-0003-4008-4029](https://orcid.org/0000-0003-4008-4029))
**Version:** 1.11.0 (see [`CHANGELOG.md`](CHANGELOG.md))
**License:** CC BY 4.0 ([`LICENSE`](LICENSE))

## Installation

Three install formats are available. Pick the one that matches your environment.

| Format | Where it runs |
| --- | --- |
| **Claude.ai upload** | Claude.ai web or desktop app (Pro, Max, Team, Enterprise) |
| **Local skill** | Claude Code or Cowork: personal Mac/Linux/Windows |
| **Plugin** | Claude Code plugin for team or marketplace distribution |

All three contain the same skill content; only the packaging differs. Download the zips from the repository's [GitHub Releases](https://github.com/alexandreamato/medical-manuscript-writing/releases), or build them yourself with `bash dist/build-zips.sh` (they are not stored in git; the version comes from `CHANGELOG.md`).

`agents/openai.yaml` is optional interface metadata for OpenAI Codex / ChatGPT skills (display name, short description, default prompt; see https://developers.openai.com/codex/skills). Claude ignores it; it lets the same folder be installed as a Codex skill.

### 1. Claude.ai (web or desktop)

1. Open Claude.ai → click your initials → **Settings** → **Capabilities** → **Skills**.
2. Click **Upload skill**.
3. Upload `medical-manuscript-writing-claudeai.zip` (from Releases, or `dist/` after building).

To invoke it, ask Claude: *"Use the medical manuscript writing skill to draft the Methods section of my RCT."*

To update, upload the same zip again: Claude.ai replaces the existing entry.

### 2. Claude Code: local skills folder

```bash
curl -L https://github.com/alexandreamato/medical-manuscript-writing/archive/refs/heads/main.zip -o mmw.zip
unzip mmw.zip
mkdir -p ~/.claude/skills
mv medical-manuscript-writing-main ~/.claude/skills/medical-manuscript-writing
```

Restart Claude Code (or open a new session), then run `/skills`: the skill should appear in the list.

To update later:

```bash
rsync -a --delete medical-manuscript-writing/ ~/.claude/skills/medical-manuscript-writing/
```

### 3. Claude Code plugin (team / marketplace)

```bash
unzip medical-manuscript-writing-plugin.zip
/plugin install ./medical-manuscript-writing-plugin
```

The repository itself is laid out as a skill, not as a plugin marketplace, so `/plugin marketplace add` does not apply to it.

### Verifying the install

Ask Claude: *"What does the medical-manuscript-writing skill cover?"* A correctly loaded skill answers from `SKILL.md`: the three working modes (point edit, section revision, submission preparation), the integrity rules, and the "Where to Look" map of reference files.

---

## What this skill does

The skill guides authors through every stage of manuscript writing, from drafting through critical self-reading, formal pre-submission review, and responding to reviewers, aligned with the reporting standard for the study type (CONSORT 2025, SPIRIT 2025, STROBE, PRISMA 2020 and its extensions, STARD 2015, CARE, TRIPOD+AI, ARRIVE 2.0, and others).

How it works:

- **The work matches the request.** A paragraph edit returns the paragraph and only the notes the author needs; a section revision adds an outline, open issues and a claim–evidence map; submission preparation adds a full audit, delivered separately from the manuscript.
- **Integrity rules come first.** No fabricated references, data or results; every claim is checked against the evidence its type needs (prior knowledge: a citation; the study's own findings: the Results; interpretation: both); scientific changes are proposed to the authors, never made silently. Journal-specific conventions (reference style, dashes, file format) are defaults that the journal's instructions override.
- **It knows when to stop.** Writing fixes writing; design limitations and missing analyses are listed for the authors instead of being argued around in prose.

Entry point: [`SKILL.md`](SKILL.md). All guides are in [`references/`](references/).

## Companion tools

Browser-based diagram generators are integrated as the preferred options for the participant flow diagrams:

- **CONSORT Flow Diagram Generator**: https://enciclopedia.med.br/consort2010 (parallel-2/3, crossover, cluster, factorial). The URL keeps the 2010 name; the layout matches CONSORT 2025 once the follow-up and analysis boxes are relabelled "for primary outcome".
- **PRISMA 2020 Flow Diagram Generator**: https://enciclopedia.med.br/prisma2020 (new and updated reviews; English and Portuguese)
- **STROBE Flow Diagram Generator**: https://enciclopedia.med.br/strobe (cohort, case-control, cross-sectional; count-consistency check; JSON save/load)
- **CARE Timeline Generator**: https://enciclopedia.med.br/care-timeline (case-report timelines by section, date or both)

All released under CC BY 4.0.

## Reference files

The skill comprises 34 reference files: section guides (title, abstract, introduction, methods, results, discussion), article types (case report, systematic review, narrative review), standards (reporting guidelines, study types, statistical reporting, ethics), presentation (conventions, citation styles, figures and tables, diagrams, statistical figures, the build kit), and process (writing process, flow, self-reading, pre-submission review, responses to reviewers, cover letter, journal selection, non-native authors, glossary), plus a bank of fictional worked examples for abstracts, introductions, methods, results and discussions. `SKILL.md` ends with the full map ("Where to Look").

## Manuscript starter templates

Ready-to-fill scaffolds for the four most common article types are in [`templates/`](templates/):

| Template | Article type | Reporting standard |
| --- | --- | --- |
| [`rct-manuscript.md`](templates/rct-manuscript.md) | Randomized controlled trial | CONSORT 2025 |
| [`observational-study.md`](templates/observational-study.md) | Cohort / case-control / cross-sectional | STROBE |
| [`case-report.md`](templates/case-report.md) | Case report | CARE 2013 |
| [`systematic-review.md`](templates/systematic-review.md) | Systematic review and meta-analysis | PRISMA 2020 |

Each template contains the standard section structure, placeholder text, and inline references to the matching reporting-standard items.

## Procedural .docx build

[`templates/build-kit/`](templates/build-kit/) is optional: use it for new manuscripts, or when a manuscript will go through many revisions or several journals. Existing Word files are revised in Word as usual. The kit keeps the manuscript as Markdown sections under git, references as CSL-JSON cited by key, and each journal's rules as a JSON profile, then generates the submission files with pandoc.

- **Numbering by construction.** References and figures/tables are renumbered by first mention on every build; changing journal is choosing another profile (style, headings, limits, title page, blinding).
- **Journal profiles.** Eleven profiles: nine real journals, each rule annotated with the page it was read on, **Jornal Vascular Brasileiro** (the default), **Journal of Vascular Surgery**, **Phlebology**, **Obesity** (Silver Spring), **Obesity Facts**, **Clinical Obesity**, **International Journal of Obesity**, **Journal of Clinical Medicine** (MDPI) and **Cureus**; plus `generic-icmje` (drafting defaults) and `example-journal-b` (illustrative, to show how a change of journal changes the files). `validate.py --compare` shows what each journal would still need for the same manuscript.
- **References.** `refs.py` adds them by DOI or PMID (never typed by hand), verifies title, year and first author against Crossref and PubMed, flags retractions and corrections, and re-checks after 90 days. Sources without DOI/PMID are recorded with who checked them and how.
- **Validation.** Word limits with their counting scope, required sections, abstract structure in both languages, declarations, citations, estimate/CI consistency between abstract and results, placeholders, ORCIDs.
- **Draft is not ready.** `--submission` blocks example content, unverified references, generic profiles and any human-review item not signed off.
- **Preview.** `preview.py` renders every file to PDF and a contact sheet of all pages, and catches author names left in a blinded file.
- **Revision rounds.** The .docx the journal sends back is compared with what was submitted (tracked changes, comments and untracked edits); accepted edits go into the source first. Then the clean file, the file with your changes marked as the journal asks (red text for J Vasc Bras, or Word tracked changes) and the response letter are generated, with identical numbering.
- **File names.** One rule for every upload: `<short-name>_<journal>[_rev<N>]_<part>.<ext>`.

Python standard library only, plus pandoc ≥ 3.1 (LibreOffice and poppler for the preview). 54 tests, offline: `cd templates/build-kit && python3 -m unittest discover -s scripts/tests`. Workflow and agent rules: [`references/docx-build.md`](references/docx-build.md); commands: [`templates/build-kit/README.md`](templates/build-kit/README.md).

## Quick reference files

- [`references/glossary.md`](references/glossary.md): ~90 statistical, methodological, and reporting terms with short definitions.
- [`references/common-mistakes.md`](references/common-mistakes.md): single-page cheatsheet of desk-rejection patterns, why they fail, and how to fix them. Use as a 5-minute pre-submission audit.
- [`references/research-apis.md`](references/research-apis.md): ten open APIs for programmatic literature work (Crossref, OpenAlex, Semantic Scholar, DataCite, NCBI E-utilities, Europe PMC, CORE, arXiv, ORCID, OpenCitations) with authentication, rate-limit guidance, and "best API by goal" mapping.
- [`references/citation-styles.md`](references/citation-styles.md): Vancouver (default), comparison table, reference-manager workflow, hard rules. Paired with [`references/citation-styles-detail.md`](references/citation-styles-detail.md) for AMA, APA 7, Harvard, Chicago 18, and CSE detail.
- [`references/paragraph-flow.md`](references/paragraph-flow.md): paragraph-, section-, and manuscript-level flow rules; reverse-outlining workflow; transitions by function; symptom → fix table.
- [`references/title.md`](references/title.md): titles, running titles and keywords (MeSH, DeCS), in one or two languages.
- [`references/cover-letter.md`](references/cover-letter.md): the cover letter for initial submission.
- [`references/journal-selection.md`](references/journal-selection.md): choosing a journal, spotting predatory journals, preprints and the ICMJE policy.
- [`references/non-native-authors.md`](references/non-native-authors.md): writing in English as a Portuguese-speaking author.

## Versioning and license

- [`CHANGELOG.md`](CHANGELOG.md): chronological list of changes by version.
- [`LICENSE`](LICENSE): Creative Commons Attribution 4.0 International (CC BY 4.0).

---

# Bibliography

The skill synthesizes guidance from peer-reviewed methodological papers, official reporting-standard documents, and reference manuals on biomedical writing. Sources are grouped by topic.

## Reporting standards (official statements)

- Hopewell S, Chan AW, Collins GS, Hróbjartsson A, Moher D, Schulz KF, et al. CONSORT 2025 statement: updated guideline for reporting randomised trials. *BMJ* 2025;389:e081123. doi:10.1136/bmj-2024-081123
- Hopewell S, Chan AW, Collins GS, Hróbjartsson A, Moher D, Schulz KF, et al. CONSORT 2025 explanation and elaboration: updated guideline for reporting randomised trials. *BMJ* 2025;389:e081124. doi:10.1136/bmj-2024-081124
- Schulz KF, Altman DG, Moher D; CONSORT Group. CONSORT 2010 statement: updated guidelines for reporting parallel group randomised trials. *BMJ* 2010;340:c332. doi:10.1136/bmj.c332 (superseded by CONSORT 2025)
- von Elm E, Altman DG, Egger M, Pocock SJ, Gøtzsche PC, Vandenbroucke JP; STROBE Initiative. The Strengthening the Reporting of Observational Studies in Epidemiology (STROBE) Statement: guidelines for reporting observational studies. *PLoS Med* 2007;4(10):e296.
- STROBE Statement v4 combined checklist (cohort, case-control, cross-sectional studies). https://www.strobe-statement.org
- Page MJ, McKenzie JE, Bossuyt PM, Boutron I, Hoffmann TC, Mulrow CD, et al. The PRISMA 2020 statement: an updated guideline for reporting systematic reviews. *BMJ* 2021;372:n71. doi:10.1136/bmj.n71
- Bossuyt PM, Reitsma JB, Bruns DE, Gatsonis CA, Glasziou PP, Irwig L, et al. STARD 2015: an updated list of essential items for reporting diagnostic accuracy studies. *BMJ* 2015;351:h5527.
- Cohen JF, Korevaar DA, Altman DG, Bruns DE, Gatsonis CA, Hooft L, et al. STARD 2015 guidelines for reporting diagnostic accuracy studies: explanation and elaboration. *BMJ Open* 2016;6:e012799. doi:10.1136/bmjopen-2016-012799
- Gagnier JJ, Kienle G, Altman DG, Moher D, Sox H, Riley D; CARE Group. The CARE guidelines: consensus-based clinical case reporting guideline development. *J Med Case Reports* 2013;7:223. https://www.care-statement.org
- Collins GS, Moons KGM, Dhiman P, Riley RD, Beam AL, Van Calster B, et al. TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods. *BMJ* 2024;385:e078378. doi:10.1136/bmj-2023-078378
- Collins GS, Reitsma JB, Altman DG, Moons KGM. Transparent Reporting of a multivariable prediction model for Individual Prognosis Or Diagnosis (TRIPOD): the TRIPOD Statement. *BMJ* 2015;350:g7594. (superseded by TRIPOD+AI)
- Gallifant J, et al. The TRIPOD-LLM reporting guideline for studies using large language models. *Nat Med* 2025;31(1):60-69. doi:10.1038/s41591-024-03425-5
- Rethlefsen ML, et al. PRISMA-S: an extension to the PRISMA statement for reporting literature searches in systematic reviews. *Syst Rev* 2021;10(1):39. doi:10.1186/s13643-020-01542-z
- McInnes MDF, et al. Preferred Reporting Items for a Systematic Review and Meta-analysis of Diagnostic Test Accuracy Studies: the PRISMA-DTA statement. *JAMA* 2018;319(4):388-396. doi:10.1001/jama.2017.19163
- Campbell M, et al. Synthesis without meta-analysis (SWiM) in systematic reviews: reporting guideline. *BMJ* 2020;368:l6890. doi:10.1136/bmj.l6890
- Kottner J, et al. Guidelines for Reporting Reliability and Agreement Studies (GRRAS) were proposed. *J Clin Epidemiol* 2011;64(1):96-106. doi:10.1016/j.jclinepi.2010.03.002
- Lang TA, Altman DG. Basic statistical reporting for articles published in biomedical journals: the SAMPL Guidelines. *Int J Nurs Stud* 2015;52(1):5-9. doi:10.1016/j.ijnurstu.2014.09.006
- Heidari S, et al. Sex and Gender Equity in Research: rationale for the SAGER guidelines and recommended use. *Res Integr Peer Rev* 2016;1:2. doi:10.1186/s41073-016-0007-6
- Piaggio G, et al. Reporting of noninferiority and equivalence randomized trials: extension of the CONSORT 2010 statement. *JAMA* 2012;308(24):2594-2604. doi:10.1001/jama.2012.87802
- Percie du Sert N, Hurst V, Ahluwalia A, Alam S, Avey MT, Baker M, et al. The ARRIVE guidelines 2.0: Updated guidelines for reporting animal research. *PLoS Biol* 2020;18(7):e3000410.
- Chan AW, Boutron I, Hopewell S, Moher D, Schulz KF, Collins GS, et al. SPIRIT 2025 statement: updated guideline for protocols of randomised trials. *BMJ* 2025;389:e081477. doi:10.1136/bmj-2024-081477
- Hróbjartsson A, Boutron I, Hopewell S, Moher D, Schulz KF, Collins GS, et al. SPIRIT 2025 explanation and elaboration: updated guideline for protocols of randomised trials. *BMJ* 2025;389:e081660. doi:10.1136/bmj-2024-081660
- Chan AW, Tetzlaff JM, Altman DG, Laupacis A, Gøtzsche PC, Krleža-Jerić K, et al. SPIRIT 2013 statement: defining standard protocol items for clinical trials. *Ann Intern Med* 2013;158(3):200-207. (superseded by SPIRIT 2025)
- SPIRIT-CONSORT Item 18: Participant timeline. https://www.consort-spirit.org/item18-participanttimeline
- Husereau D, Drummond M, Augustovski F, de Bekker-Grob E, Briggs AH, Carswell C, et al. Consolidated Health Economic Evaluation Reporting Standards 2022 (CHEERS 2022) statement. *BMJ* 2022;376:e067975.
- Ogrinc G, Davies L, Goodman D, Batalden P, Davidoff F, Stevens D. SQUIRE 2.0 (Standards for QUality Improvement Reporting Excellence): revised publication guidelines from a detailed consensus process. *BMJ Qual Saf* 2016;25:986-992.
- O'Brien BC, Harris IB, Beckman TJ, Reed DA, Cook DA. Standards for reporting qualitative research: a synthesis of recommendations. *Acad Med* 2014;89(9):1245-1251.
- EQUATOR Network. Enhancing the QUAlity and Transparency Of health Research. https://www.equator-network.org

## Reporting-standard educational papers

- Falci SGM, Marques LS. CONSORT: when and how to use it. *Dental Press J Orthod* 2015;20(3):13-15. doi:10.1590/2176-9451.20.3.013-015.ebo

## How-to-write guides: overall manuscript

- Mateu Arrom L, Huguet J, Errando C, Breda A, Palou J. How to write an original article. *Actas Urol Esp* 2018;42(9):545-550. doi:10.1016/j.acuroe.2018.02.012
- Alexandrov AV. How to write a research paper. *Cerebrovasc Dis* 2004;18(2):135-138. doi:10.1159/000079266
- Hoogenboom BJ, Manske RC. How to write a scientific article. *Int J Sports Phys Ther* 2012;7(5):512-517.
- Jha KN. How to Write Articles That Get Published. *J Clin Diagn Res* 2014;8(9):XG01-XG03. doi:10.7860/JCDR/2014/8107.4855
- Mondal H, Mondal S, Saha K. What to Write in Each Segment of an Original Article? *Indian J Vasc Endovasc Surg* 2019;6(3):221.
- Kallet RH. How to write the methods section of a research paper. *Respir Care* 2004;49(10):1229-1232.
- International Committee of Medical Journal Editors (ICMJE). Recommendations for the Conduct, Reporting, Editing, and Publication of Scholarly Work in Medical Journals. https://www.icmje.org

## Section-specific guides

### Introduction

- Armağan A. How to write an introduction section of a scientific article? *Turk J Urol* 2013;39(Suppl 1):8-9.

### Abstract

- Koopman P. How to Write an Abstract. Carnegie Mellon University; 1997. Reproduced widely as a writing-instruction reference.
- Bucholtz M. Writing Conference Abstracts. University of California, Santa Barbara; 2004-2007.

### Discussion and Conclusion

- Hess DR. How to write an effective discussion. *Respir Care* 2023;68(12):1771-1774. doi:10.4187/respcare.11435
- Şanlı Ö, Erdem S, Tefik T. How to write a discussion section? *Turk J Urol* 2013;39(Suppl 1):20-24.
- Makar G, Foltz C, Lendner M, Vaccaro AR. How to Write Effective Discussion and Conclusion Sections. *Clin Spine Surg* 2018;31(8):345-346.

## Case reports

- McCarthy LH, Reilly KEH. How to write a case report. *Fam Med* 2000;32(3):190-195.
- Cohen H. How to write a patient case report. *Am J Health Syst Pharm* 2006;63(19):1888-1892.
- CARE Statement. CARE Checklist of information to include when writing a case report (English, 2013). https://www.care-statement.org

## Reviews: narrative and clinical update

- Van Wee B, Banister D. How to write a literature review paper? *Transp Rev* 2016;36(2):278-288. doi:10.1080/01441647.2015.1065456
- Siwek J, Gourlay ML, Slawson DC, Shaughnessy AF. How to write an evidence-based clinical review article. *Am Fam Physician* 2002;65(2):251-258.
- Gülpınar Ö, Güçlü AG. How to write a review article? *Turk J Urol* 2013;39(Suppl 1):44-48.
- Denney AS, Tewksbury R. How to write a literature review. *Journal of Criminal Justice Education* 2013;24(2):218-234.

## Systematic reviews and meta-analysis

- Wright RW, Brand RA, Dunn W, Spindler KP. How to write a systematic review. *Clin Orthop Relat Res* 2007;455:23-29.
- Cochrane Handbook for Systematic Reviews of Interventions. Higgins JPT, Thomas J, Chandler J, Cumpston M, Li T, Page MJ, Welch VA (editors). Version 6.4 (or current). Cochrane; 2024.
- Page MJ, McKenzie JE, Bossuyt PM, et al. The PRISMA 2020 statement (cited above under reporting standards).

## Critical appraisal and self-reading

- Greenhalgh T. How to read a paper: getting your bearings (deciding what the paper is about). *BMJ* 1997;315:243-246.
- Greenhalgh T. How to read a paper: The Medline database. *BMJ* 1997;315:180-183.
- Greenhalgh T. How to read a paper: Papers that report diagnostic or screening tests. *BMJ* 1997;315:540-543.
- Greenhalgh T. *How to Read a Paper: The Basics of Evidence-Based Medicine*. London: BMJ Publishing Group; 2001 (subsequent editions through 2019).

## Responding to reviewers

- Efron N. Ensure your paper gets published: ten tips for responding effectively to reviewer comments. *Clin Exp Optom* 2025. doi:10.1080/08164622.2025.2589401
- Cushman M. How I respond to peer reviewer comments. *Res Pract Thromb Haemost* 2023;7(4):100166. doi:10.1016/j.rpth.2023.100166
- Hidouri S, Kamoun H, Salah S, Jellad A, Ben Saad H. Key Guidelines for Responding to Reviewers. *F1000Research* 2024;13:921.

## Statistics and methodology

- Hernán MA, Robins JM. *Causal Inference: What If*. Boca Raton, FL: Chapman & Hall/CRC; 2020.
- Sterne JA, White IR, Carlin JB, Spratt M, Royston P, Kenward MG, et al. Multiple imputation for missing data in epidemiological and clinical research: potential and pitfalls. *BMJ* 2009;338:b2393.
- Higgins JPT, Altman DG, Gøtzsche PC, Jüni P, Moher D, Oxman AD, et al. The Cochrane Collaboration's tool for assessing risk of bias in randomised trials. *BMJ* 2011;343:d5928.
- Sterne JAC, Savović J, Page MJ, Elbers RG, Blencowe NS, Boutron I, et al. RoB 2: a revised tool for assessing risk of bias in randomised trials. *BMJ* 2019;366:l4898.
- Sterne JAC, Hernán MA, Reeves BC, Savović J, Berkman ND, Viswanathan M, et al. ROBINS-I: a tool for assessing risk of bias in non-randomised studies of interventions. *BMJ* 2016;355:i4919.
- Whiting PF, Rutjes AWS, Westwood ME, Mallett S, Reitsma JB, Leeflang MMG, et al. QUADAS-2: a revised tool for the quality assessment of diagnostic accuracy studies. *Ann Intern Med* 2011;155(8):529-536.
- Guyatt GH, Oxman AD, Vist GE, Kunz R, Falck-Ytter Y, Alonso-Coello P, et al. GRADE: an emerging consensus on rating quality of evidence and strengths of recommendations. *BMJ* 2008;336:924-926.
- VanderWeele TJ, Ding P. Sensitivity Analysis in Observational Research: Introducing the E-Value. *Ann Intern Med* 2017;167(4):268-274.
- Hoenig JM, Heisey DM. The abuse of power: the pervasive fallacy of power calculations for data analysis. *Am Stat* 2001;55(1):19-24. doi:10.1198/000313001300339897
- Button KS, et al. Power failure: why small sample size undermines the reliability of neuroscience. *Nat Rev Neurosci* 2013;14(5):365-376. doi:10.1038/nrn3475

## Citation styles and reference management

- Patrias K, Wendling D (technical editor). *Citing Medicine: The NLM Style Guide for Authors, Editors, and Publishers*. 2nd ed. Bethesda, MD: National Library of Medicine; 2007. https://www.ncbi.nlm.nih.gov/books/NBK7256/
- *AMA Manual of Style: A Guide for Authors and Editors*. 11th ed. New York: Oxford University Press; 2020.
- *Publication Manual of the American Psychological Association*. 7th ed. Washington, DC: American Psychological Association; 2020.
- *The Chicago Manual of Style*. 18th ed. Chicago: University of Chicago Press; 2024.
- IEEE Editorial Style Manual. https://ieeeauthorcenter.ieee.org
- Curtin University Library: UniSkills referencing printable guides (Vancouver, AMA, APA 7th, IEEE, Chicago 18 Author-Date). https://uniskills.library.curtin.edu.au

## Figures, tables, and diagrams

- Tufte ER. *The Visual Display of Quantitative Information*. 2nd ed. Cheshire, CT: Graphics Press; 2001.
- Page MJ, Haddaway NR, Pritschet B, Stewart G, McKenzie JE; PRISMA flow diagram generators. https://github.com/prisma-flowdiagram/PRISMA2020
- PRISMA2020 R package. https://cran.r-project.org/web/packages/PRISMA2020/
- Amato ACM. PRISMA 2020 Flow Diagram Generator [Internet]. São Paulo: enciclopedia.med.br; 2025. Available from: https://enciclopedia.med.br/prisma2020
- Amato ACM. CONSORT 2010 Flow Diagram Generator [Internet]. São Paulo: enciclopedia.med.br; 2025. Available from: https://enciclopedia.med.br/consort2010
- Amato ACM. STROBE Flow Diagram Generator [Internet]. São Paulo: enciclopedia.med.br; 2026. Available from: https://enciclopedia.med.br/strobe
- Jornal Vascular Brasileiro. Instructions to authors [Internet]. Available from: https://www.jvascbras.org/instructions (read 2026-09-23; basis of the kit's `jvb` profile)
- Textor J, van der Zander B, Gilthorpe MS, Liśkiewicz M, Ellison GTH. Robust causal inference using directed acyclic graphs: the R package "dagitty". *Int J Epidemiol* 2016;45(6):1887-1894. https://www.dagitty.net
- Mermaid: text-to-diagram syntax. https://mermaid.js.org

## Statistical-figure tooling

- Viechtbauer W. Conducting meta-analyses in R with the metafor package. *J Stat Softw* 2010;36(3):1-48.
- Therneau TM. survival: A Package for Survival Analysis in R. https://cran.r-project.org/package=survival
- Kassambara A, Kosinski M, Biecek P. survminer: Drawing Survival Curves using ggplot2. https://cran.r-project.org/package=survminer
- Robin X, Turck N, Hainard A, Tiberti N, Lisacek F, Sanchez JC, Müller M. pROC: an open-source package for R and S+ to analyze and compare ROC curves. *BMC Bioinformatics* 2011;12:77.

## Ethics, integrity, and publication policies

- International Committee of Medical Journal Editors (ICMJE). Defining the Role of Authors and Contributors. https://www.icmje.org/recommendations/browse/roles-and-responsibilities/defining-the-role-of-authors-and-contributors.html
- Committee on Publication Ethics (COPE). Core Practices. https://publicationethics.org/core-practices
- Naranjo CA, Busto U, Sellers EM, Sandor P, Ruiz I, Roberts EA, et al. A method for estimating the probability of adverse drug reactions. *Clin Pharmacol Ther* 1981;30(2):239-245.
- World Medical Association. World Medical Association Declaration of Helsinki: ethical principles for medical research involving human participants (2024 revision). *JAMA* 2025;333(1):71-74. doi:10.1001/jama.2024.21972
- Grudniewicz A, Moher D, Cobey KD, et al. Predatory journals: no definition, no defence. *Nature* 2019;576(7786):210-212. doi:10.1038/d41586-019-03759-y

## PubMed and literature searching

- US National Library of Medicine. PubMed. https://pubmed.ncbi.nlm.nih.gov
- US National Library of Medicine. NLM Catalog: Journals referenced in the NCBI Databases. https://www.ncbi.nlm.nih.gov/nlmcatalog/journals
- US National Library of Medicine. PubMed User Guide. https://pubmed.ncbi.nlm.nih.gov/help/
- PubMed Clinical Queries. https://pubmed.ncbi.nlm.nih.gov/clinical/
- Cookjohn. pm-skills: PubMed skills for Claude Code via Chrome DevTools MCP. https://github.com/cookjohn/pm-skills

## Trial registries and reporting infrastructure

- ClinicalTrials.gov (US). https://clinicaltrials.gov
- ISRCTN registry. https://www.isrctn.com
- WHO International Clinical Trials Registry Platform (ICTRP). https://www.who.int/clinical-trials-registry-platform
- PROSPERO: International Prospective Register of Systematic Reviews. https://www.crd.york.ac.uk/prospero/

## Tools and workflow

- Greenhalgh T (cited above) for the read-as-reader framework.
- BibTeX/BibLaTeX, Zotero, EndNote, Mendeley, Paperpile: reference managers referenced in `references/citation-styles.md`.
- Citation Style Language (CSL) styles repository. https://github.com/citation-style-language/styles (browse at https://www.zotero.org/styles)
- MacFarlane J, et al. Pandoc: a universal document converter. https://pandoc.org
- DOI International Foundation: DOI Handbook. https://www.doi.org/the-identifier/resources/handbook/

---

## How to cite this skill

If you use this skill in producing a manuscript, please consider citing it:

> Amato ACM. Medical Manuscript Writing: Claude Skill [Internet]. Version 1.11.0. 2026. Available from: https://github.com/alexandreamato/medical-manuscript-writing

## Updates and contributions

The bibliography above is a working list; new sources are added as the skill evolves. If you spot a missing citation that supports a section, please open an issue or pull request.
