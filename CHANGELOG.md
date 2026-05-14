# Changelog

All notable changes to this repo. Format loosely follows [Keep a Changelog](https://keepachangelog.com/).

Status-change-only entries live in [`tracker/falsification-events.md`](tracker/falsification-events.md). This file records *structural* changes: new programmes, new essays, new notebooks, new scripts, new infrastructure.

---

## [Unreleased]

### Added

- `scripts/verify_citations.py` now persists a `.cache/arxiv-verify.json` across runs so flaky-network local sessions accumulate verified IDs instead of starting over each time. Pass `--no-cache` to force fresh fetches.
- `scripts/generate_papers_index.py` produces a flat, deduplicated `PAPERS.md` index of every arXiv-cited paper across all programmes and essays, with the programme assignment(s) and the citing files.
- `PAPERS.md` (generated artifact; see above).
- `CHANGELOG.md` (this file).

---

## [0.2.0] — 2026-05-14 — Round-two expansion

### Added

- **Programme 02** — 6 primary entries spanning the 2024–25 SAE wave (Gao et al. *Scaling SAEs*; Rajamanoharan et al. *Gated SAEs* and *JumpReLU SAEs*; Marks et al. *Sparse Feature Circuits*; Marks & Tegmark *Geometry of Truth*; Wendler et al. *Do Llamas Work in English?*). Three new claim rows in the per-claim ledger (02-H, 02-I, 02-J).
- **Programme 03** — 4 primary entries (Anthropic 2025 *Circuit Tracing* attribution-graph methodology; Tigges et al. 2024 universality across training; Li et al. 2023 *Inference-Time Intervention*; Zou et al. 2023 *Representation Engineering*) plus a cross-reference to Sparse Feature Circuits. Three new claim rows (03-H, 03-I, 03-J).
- **Programme 04** — 4 primary entries (Hendel et al. 2023 *Task Vectors*; Todd et al. 2023 *Function Vectors*; Min et al. 2022 *Rethinking the Role of Demonstrations*; Merullo et al. 2023 *word2vec-style arithmetic*). Two new claim rows (04-H, 04-I). Claim 04-G moved ⚪ Open → 🔴 Refuted-in-strict-form, citing Min et al.
- **GLOSSARY** — 7 new terms (Attribution graph, Function vector, JumpReLU SAE, nnsight, Representation engineering, Sparse Feature Circuits, Task vector).
- **`TOOLS.md`** — opinionated index of load-bearing tools (TransformerLens, SAELens, nnsight, Pyvene, Neuronpedia, Goodfire Ember, ACDC/EAP, circuit-tracer, HF stack).
- **`FAQ.md`** — 17 anticipated questions with honest answers.
- **`CITATION.cff`** — citation metadata for the GitHub "Cite this repository" widget and tools like Zotero.
- **`.gitleaks.toml`** + **`.github/workflows/secret-scan.yml`** — pre-launch secret-scanning baseline.

### Fixed

- `scripts/render_taxonomy.py` now auto-escapes XML in node labels; cairosvg can rasterize the SVG without `ParseError` on `<` / `>` / `&` in claim text.
- Renamed inner loop variables in the SVG renderer so they no longer shadow the new XML-escape helper.

---

## [0.1.0] — 2026-05-14 — Seed launch state

### Added

- Five programme files with hard cores, protective belts, falsification ledgers, open problems, and reading paths: [01 Compression](programmes/01-compression-as-intelligence.md), [02 Superposition / LRH](programmes/02-superposition-linear-rep.md), [03 Circuits](programmes/03-circuits-and-biology.md), [04 ICL-as-Bayes](programmes/04-icl-as-bayes-meta-learning.md), [05 Emergence](programmes/05-emergence-and-reasoning.md).
- [Adjacent programmes appendix](programmes/adjacent-programmes.md) (SLT, Platonic Representation, Predictive Coding, grokking-as-subprogramme).
- 5 runnable notebooks targeting `<5 min` on a free Colab T4 (`01` through `05`).
- 4 synthesis essays — compression↔superposition, circuits↔ICL-Bayes, emergence↔reasoning-models, and the methodological steel-man.
- 4 reading paths — 30-minute / weekend / month / research-track.
- `GLOSSARY.md` with 60+ programme-aware definitions.
- `scripts/`: `verify_citations.py`, `check_links.py`, `ingest_arxiv.py`, `render_taxonomy.py`, `render_ledger.py`.
- `taxonomy.svg` + `taxonomy.png`.
- `.github/workflows/`: link-check, citation-verify, weekly arxiv-ingest. Issue and PR templates.
- `tracker/falsification-events.md` + `tracker/monthly-digest-2026-05.md`.
- `_internal/`: competitor audit, preseed targets, launch playbook (committed per ADR-0005).
- Top-level `README.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `DECISIONS.md`, dual license (CC-BY-4.0 for content, MIT for code).
