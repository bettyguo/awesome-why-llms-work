# How to Falsify an LLM Theory — A Methodological Essay

> The most uncomfortable critique of this repo is not that any particular claim is wrong but that the *whole frame* — programmes with hard cores, falsification ledgers, status verdicts — is itself a research claim, contested and possibly badly chosen. This essay takes that critique seriously, responds to it, and lays out what a falsifiability-driven curation effort can and cannot deliver.

---

## The critique, in its strongest form

A serious reader could say all of the following:

1. **"This taxonomy is itself a research claim and is contested."** The five-programme structure is one of many defensible carvings. Other reasonable carvings exist (e.g., a four-programme version that merges Superposition and Circuits; a six-programme version that promotes Singular Learning Theory). The repo presents its choice as if it were neutral curation; it is not.
2. **"Status verdicts are subjective."** Calling something 🟡 *Contested* vs. 🔴 *Refuted* is an editorial decision. Two competent reviewers will disagree on borderline cases. The repo treats the verdicts as if they were extracted from the literature; they are produced by maintainers.
3. **"Awesome-list format trivializes complex disagreements."** A 40-word annotation cannot capture the actual content of a careful paper. By compressing into the schema, the repo flattens nuance and may misrepresent positions.
4. **"Falsifiability is a 1934 idea applied to a 2024 field."** Karl Popper's falsifiability criterion was developed for physics. Statistical, scale-dependent, multi-causal empirical claims about deep networks do not fit it neatly. Pretending they do is borrowed authority.
5. **"The repo will be obsolete in 12 months."** The field moves fast; the falsification ledger is a snapshot. By the time someone reads this in 2027, half the claims will have moved.

These are real critiques. They deserve responses, not deflection.

---

## Response

### On (1) — the taxonomy is a research claim

It is. The repo is honest about this; we discussed the structural decision in [`DECISIONS.md`](../DECISIONS.md#adr-0001--programme-map-not-flat-directory). The defense of the five-programme structure is empirical and pragmatic, not metaphysical:

- Each programme has *named proponents and critics who disagree with each other across the boundary*. That is the operational test of "this is a coherent research programme": a paper inside Programme 02 (Superposition) cites people inside Programme 02; papers across programmes engage as if speaking from different starting points. Where the field does not look like that, we say so — the adjacent-programme appendix exists precisely for the cases that do not yet have this structure.
- The five-programme structure makes *predictions*: it predicts that papers will cluster into the five core programmes and that synthesis essays bridging them will be the productive next move. If the taxonomy were a bad carving, the synthesis essays would either be impossible to write or would not yield new questions. The two we have produced (compression-superposition, circuits-icl-bayes) yield specific empirical questions; the third (emergence-vs-reasoning-models) sharpens what is genuinely open.
- Alternative carvings are *fine*. The repo is opinionated, not unique. We link to alternative organizing efforts in the [related repos](../README.md#related-and-companion-repos) section; if our five-programme structure is wrong, those exist.

The right response to "your taxonomy is a research claim" is *yes, and we treat it as one*. Issue [`new-programme.md`](../.github/ISSUE_TEMPLATE/new-programme.md) explicitly invites challenges to the taxonomy itself.

### On (2) — status verdicts are subjective

They are partly subjective. The repo handles this with explicit conventions:

- 🟢 / 🟡 / 🔴 / ⚪ have *operational* definitions in [`CONTRIBUTING.md`](../CONTRIBUTING.md) and [`programmes/README.md`](../programmes/README.md). They are not "how I feel about this paper."
- 🟢 *Supported* requires at least two independent replications or the original paper plus a community-accepted survey.
- 🔴 *Refuted* requires a cited refuting paper accepted at workshop level or above.
- 🟡 *Contested* requires a named credentialed critic with a cited paper.
- ⚪ *Open* is the default for serious claims without published replications or refutations.

Two reviewers can disagree on borderline cases. The mechanism the repo uses is: status changes are PRs, require maintainer review, and 🟢 ↔ 🔴 transitions require two maintainer approvals. The public record of disagreement lives in [`tracker/falsification-events.md`](../tracker/falsification-events.md). This is not perfect epistemic objectivity; it is the best practical approximation a curated repo can offer.

### On (3) — awesome-list format trivializes

Partially true. We mitigate by:

- Forcing **specific** annotations, not abstract paraphrases (see *Annotation quality bar* in `CONTRIBUTING.md`). A bad annotation is a rejection-on-sight criterion, not a stylistic preference.
- Pairing every paper entry with a **programme assignment** and a **falsifier**, so that the entry's place in the larger argument is explicit and reviewable.
- Writing **synthesis essays** when paper annotations alone underdescribe the situation. Essays are the long-form home for nuance that schema annotations cannot carry.

A reader who wants the *real* content of any single paper should read the paper. The repo's job is not to substitute for reading; it is to tell you which papers to read in which order with what attitude. That is a different and useful job.

### On (4) — falsifiability is from 1934

Yes, and so is general relativity, and we still use it. The relevant question is whether falsifiability is the *right* methodological criterion for LLM theory, not whether it is old.

The honest answer is: falsifiability is a *useful* criterion but not the *only* one. Some claims in this repo do not have the structure of crisp Popperian falsifiers; they have Bayesian "this evidence shifts my belief, this evidence would shift it back" structure instead. The repo accommodates that with the ⚪ *Open* status and with the protective-belt vocabulary (from Lakatos, who specifically extended Popper to handle the messier case of research programmes that defend themselves against local refutations).

The deeper point: in a young, fast-moving, multi-causal empirical field, *some* commitment to falsifiability is what distinguishes science from rhetoric. Without it, every theory expands to fit every observation and the field becomes unfalsifiable in the worst sense. With it, we are forced to specify what evidence would change our mind — and that specification is *the* contribution.

The repo is, in this sense, an experiment in a particular *kind* of curation: one that prioritizes specification of belief and updating-on-evidence over comprehensive coverage. It will succeed or fail on those terms.

### On (5) — the repo will be obsolete

Yes, partly. We treat this as a *feature* of a living document, not a bug.

- The monthly digest in [`tracker/`](../tracker/) records the literature shifts.
- The automated arXiv-ingestion script ([`scripts/ingest_arxiv.py`](../scripts/ingest_arxiv.py)) opens draft PRs that maintainers triage so the ledger stays current.
- Stale entries are *flagged*, not silently left to rot.
- The repo's structural commitments (five programmes; status taxonomy) are designed to survive specific factual updates: a claim moving from 🟡 to 🔴 does not break the programme, it updates the programme's evidence ledger.

A reader in 2027 should read both the current state of the repo and `tracker/falsification-events.md`, in that order. The latter is the audit trail.

---

## What this repo can and cannot deliver

### Can

- A defensible, opinionated, *navigable* map of the major research programmes in "why LLMs work."
- A public record of status changes — what we used to believe, what we believe now, what changed our mind.
- Pedagogical entry points (notebooks, reading paths) that let a reader internalize each programme's central content in tractable time.
- A productive forum for status-change debates that would otherwise live on scattered Twitter threads.

### Cannot

- Replace reading the actual papers. Annotations are signposts, not summaries.
- Be neutral. The five-programme structure, the status verdicts, the choice of which papers are "key" — all are editorial choices. We have made them visible rather than hidden them.
- Settle empirical questions. The repo's job is to *describe* the state of the literature; the literature is what settles questions, and the repo updates when it does.
- Predict the future. The reasoning-models wave was not in the 2022 emergence literature; SAEs were not in the 2020 interpretability literature. Some future programme is not in the 2026 version of this repo. We are committed to incorporating it when it arrives, not pretending we predicted it.

---

## The honest closing point

A curation effort like this is partly a public artifact and partly a discipline imposed on the curators. The discipline is: every claim must be defensible; every status must have an evidence ledger; every disagreement must be public. The artifact is what falls out of holding to the discipline.

If the artifact is useful to other people, that is a happy side effect. If the discipline is wrong — if falsifiability is the wrong lens, if the five programmes are the wrong carving, if the status taxonomy is too coarse — then the artifact will be revised, and the revisions will be visible. That is the closest thing to scientific honesty a curation repo can reach.

If you think the discipline is wrong, the right response is not to ignore the repo. It is to open an issue, name the wrongness, and propose a better discipline. We will engage.

---

## Pointers

- [`DECISIONS.md`](../DECISIONS.md) — the architectural decisions and their rationales.
- [`CONTRIBUTING.md`](../CONTRIBUTING.md) — the operational rules (status definitions, annotation quality bar, schema enforcement).
- [`tracker/falsification-events.md`](../tracker/falsification-events.md) — the audit trail of status changes.
- *The Logic of Scientific Discovery* — Karl Popper, 1934. Read for the original falsifiability framing.
- *The Methodology of Scientific Research Programmes* — Imre Lakatos, 1970. Read for the programme / hard-core / protective-belt vocabulary this repo uses.
