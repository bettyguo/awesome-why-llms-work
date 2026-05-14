# Decisions log (ADR-style)

Architectural and taxonomic decisions. Each entry: context, decision, alternatives, consequences. Newest first.

---

## ADR-0005 — `_internal/` is committed, not ignored

**Date**: 2026-05-14
**Status**: Accepted

### Context

The master prompt suggested putting planning artifacts (competitor audit, pre-seed targets, launch playbook) in a `_internal/` directory and `.gitignore`-style hiding it. We considered both options.

### Decision

Commit `_internal/` to the repo. Make the contents themselves self-aware that they will be public.

### Rationale

A research-curation repo's reputation depends on transparency about its own process. Hiding the competitor audit signals defensiveness; publishing it signals confidence. The pre-seed list contains only public Twitter/X handles and public lab accounts — no DMs, no PII — so there is nothing to hide.

The launch playbook is the only borderline case. We keep it committed because the marketing isn't the point — the curation is — and a maintainer who is embarrassed by the playbook should not be running the playbook.

### Consequences

- Contributors can read `_internal/competitor_audit.md` and propose corrections via PR.
- Pre-seed list must remain PII-free; we added that as a rule in `CONTRIBUTING.md`.

---

## ADR-0004 — Status taxonomy is four-valued, not five

**Date**: 2026-05-14
**Status**: Accepted

### Context

We considered adding a fifth status, 🟠 "Mostly supported, with caveats," to capture claims where most evidence points one way but a serious caveat exists.

### Decision

Stay at four values: 🟢 Supported / 🟡 Contested / 🔴 Refuted / ⚪ Open.

### Rationale

🟠 was tempting but collapses into 🟡 in practice. The "with caveats" detail belongs in the annotation, not in the status. Four values keep the at-a-glance table legible.

### Consequences

- The ledger summary stays small.
- Annotations carry more weight; we tightened the schema rules in `CONTRIBUTING.md`.

---

## ADR-0003 — Adjacent programmes are an appendix, not a sixth slot

**Date**: 2026-05-14
**Status**: Accepted

### Context

Decision gate 1 from the master prompt: should we use 5 programmes, or 6/7? Candidates for additional programmes:

- **Singular Learning Theory** (Watanabe; alignment-community SLT writeups).
- **The Platonic Representation Hypothesis** (Huh et al. 2024).
- **Predictive Coding / Free Energy analogues** (Friston).
- **Grokking & phase transitions** (could be its own programme or a sub-programme of Emergence).

### Decision

Stay at five programmes. The four candidates live in `programmes/adjacent-programmes.md`. They can be promoted to full programmes if they accumulate enough evidence ledgers.

### Rationale

- **SLT** has strong theoretical machinery but a small set of empirical claims about LLMs specifically; today it functions more as a lens on the others (especially Emergence and Compression) than as a standalone programme.
- **Platonic Representation** is one paper plus follow-ups; it overlaps heavily with the cross-modal extension of LRH (programme 02).
- **Predictive Processing** is a productive analogy but lacks a falsification ledger specific to LLMs.
- **Grokking** is a phenomenon, not a programme; the canonical mechanistic explanation (Nanda et al. 2023) lives inside programme 03.

### Consequences

- Five-programme structure stays. Adjacent appendix exists.
- Promotion criterion documented: at least 5 verifiable claims with non-trivial evidence ledgers, including at least one 🔴 or 🟡, would justify promotion to a full programme.

---

## ADR-0002 — Citation verification is enforced in CI, not on the honor system

**Date**: 2026-05-14
**Status**: Accepted

### Context

The repo's central differentiator is *defensibility*. A single fabricated citation undermines the falsification ledger. We considered:

- (A) Manual review only.
- (B) A CI script that calls the arXiv API and checks every link.
- (C) A daily cron that re-verifies all existing entries.

### Decision

All three. `scripts/verify_citations.py` runs in CI on every PR (B). `scripts/check_links.py` runs nightly via GitHub Actions (C). Manual review (A) is still required because the script cannot detect "this paper exists but its claim is misstated."

### Rationale

Verification automation is cheap; embarrassment from a fabricated citation is expensive. The script also serves as a contributor education tool — "your PR was auto-rejected because arXiv:9999.99999 does not exist."

### Consequences

- CI must be green before merge.
- Contributors writing offline cannot test the script without internet; we accept that.

---

## ADR-0001 — Programme map, not flat directory

**Date**: 2026-05-14
**Status**: Accepted

### Context

Multiple existing `awesome-*` lists cover LLM interpretability and theory. None of them takes a position on *which claims are alive*. We could:

- (A) Build a slightly bigger flat directory than the existing ones.
- (B) Build a Lakatos-style programme map with epistemic statuses.
- (C) Build a wiki of individual claims with their evidence and refutations.

### Decision

Option B (programme map). Option C is too granular for a curation repo and would need full-time editorial staff. Option A would not be differentiated.

### Rationale

The field is contested. The taxonomy *itself* is a research claim, and we are fine with that — the master prompt's reviewer pass requires us to defend the taxonomy in the methodological essay (`essays/how-to-falsify-an-llm-theory.md`).

### Consequences

- The repo takes positions and is therefore criticizable. Good.
- We need infrastructure (status template, falsification log, monthly digest) that pure paper-dumps do not.
- We need to be unusually careful about citation quality, since the repo *claims* to know what the literature says.
