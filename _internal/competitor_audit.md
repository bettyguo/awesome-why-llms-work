# Competitor audit

> A respectful audit of existing `awesome-*` and curated-bibliography repositories
> that overlap this one. The audit is committed (not hidden) per
> [ADR-0005](../DECISIONS.md). The goal is to be honest about what is being
> duplicated, what is genuinely new here, and where readers should be sent for
> use cases this repo does not serve.

For each competitor we record:

- **Organizing principle** — how is content structured?
- **Sections** — top-level entries.
- **Annotation style** — what does each entry look like?
- **Scale** — order of magnitude of entries.
- **What it does well** — and we should link to rather than duplicate.
- **What it does not do** — and we should.

---

## `JShollaj/awesome-llm-interpretability`

- **Organizing principle**: by resource type (tools / papers / articles / groups / surveys).
- **Sections**: 5 top-level — LLM Interpretability Tools, Papers, Articles, Groups, Survey.
- **Annotation style**: one-sentence descriptive phrase per entry.
- **Scale**: ~93 entries.
- **What it does well**: tool directory; broad coverage of community resources.
- **What it does not do**: no status verdicts; no falsification framing; no notebooks; no synthesis.

Recommendation: link to this repo for *tool discovery*; do not duplicate its tool list.

---

## `ruizheliUOA/Awesome-Interpretability-in-Large-Language-Models`

- **Organizing principle**: thematic, from foundational to advanced; emphasizes mechanistic interpretability.
- **Sections**: Libraries / Blogs & Videos / Tutorials / Forums & Workshops / Tools / Papers (sub-categorized: surveys, position papers, mechanistic analysis, SAEs, vision models, benchmarking).
- **Annotation style**: tabular metadata (title, venue, date, code, blog); GitHub stars on library entries.
- **Scale**: ~400+ paper entries; particularly deep on sparse autoencoders.
- **What it does well**: largest reasonable index of MI papers and tools; SAE coverage in particular.
- **What it does not do**: no notebooks, status verdicts, or synthesis.

Recommendation: link to this repo as the *bibliography of record* for SAE work specifically. Our Programme 02 file does not try to duplicate its SAE-paper coverage.

---

## `cooperleong00/Awesome-LLM-Interpretability`

- **Organizing principle**: hierarchical topic taxonomy.
- **Sections**: Tutorial / History / Code / Survey / Video / Paper & Blog, with sub-axes on tools/techniques, task-solving, components (attention / MLP / neurons), learning dynamics, and applications.
- **Annotation style**: title + venue/date + direct link; star emoji on influential work.
- **Scale**: ~305 stars on the repo itself; moderate paper count; interactive UI.
- **What it does well**: clean topic taxonomy; the interactive UI is a non-trivial value-add.
- **What it does not do**: no status verdicts, falsification, notebooks, or synthesis.

Recommendation: link to this repo for *topic-indexed paper discovery*.

---

## `Dakingrai/awesome-mechanistic-interpretability-lm-papers`

- **Organizing principle**: formal taxonomy from the maintainers' survey paper (*A Practical Review of Mechanistic Interpretability for Transformer-Based Language Models*).
- **Sections**: Techniques / Evaluation / Findings and Applications / Tools.
- **Annotation style**: structured per-paper metadata + TL;DR summary; tabular.
- **Scale**: ~70+ papers; survey-driven curation.
- **What it does well**: cleanest survey-anchored taxonomy in the MI competitor set; TL;DR annotations are useful.
- **What it does not do**: no notebooks; no status verdicts; no falsification framing.

Recommendation: link as a *survey-anchored entry point* for readers new to MI. Their TL;DRs are good; we do not replace them.

---

## `apartresearch/Awesome-AI-Alignment`

- **Result**: HTTP 404 at audit time. Either the repo is private or has been moved/renamed.
- We do not include it in the recommended-links list until it is locatable.

---

## What this repo does that none of the above do

- **Programme map with epistemic status.** Each tracked claim has 🟢 / 🟡 / 🔴 / ⚪ status.
- **Falsification ledger.** Per-claim status changes with cited rationales in `tracker/falsification-events.md`.
- **Hands-on mini-notebooks.** Five teaching notebooks, one per programme, each <5 min on a free Colab T4.
- **Synthesis essays.** Four essays that argue specific cross-programme positions, including a methodological essay on the falsifiability frame itself.
- **Strict contribution schema** enforced by CI: `scripts/verify_citations.py` blocks unverifiable arXiv references.
- **Audit trail.** Decisions, status changes, and competitor audits are committed — not hidden in a maintainer's drafts.

## What this repo does *not* do that competitors do

- **Comprehensive tool / library directory.** Several competitors (JShollaj, ruizheliUOA, cooperleong00) cover this better.
- **Comprehensive SAE bibliography.** ruizheliUOA's coverage is deeper.
- **General paper-discovery indexing.** Any of the four reviewed competitors is a better starting point if you want "what papers exist."

The mental model: this repo is the *opinionated map*; the competitor repos are the *exhaustive index*. They serve different jobs.
