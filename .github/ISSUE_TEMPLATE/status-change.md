---
name: Status change
about: Propose changing the epistemic status of a tracked claim.
title: "[status-change] Claim XX-Y: 🟢→🟡 / 🟡→🔴 / etc."
labels: ["status-change"]
assignees: []
---

## Claim

- **Claim ID** (e.g., `01-D`, `04-E`):
- **Current claim text** (verbatim from the programme file):
- **Current status**:

## Proposed status

- **New status**:

## Citation

The cited paper (or papers) supporting the change. **A status change without a
cited paper will be closed.**

- **Title**:
- **Authors**:
- **URL** (arXiv abs / DOI / OpenReview):
- **Venue / accepted at**:

## Rationale (100–250 words)

Argue for the move. Specifically:

- What is the central finding of the cited paper?
- Why does it move *this* claim and not a related one?
- Does the finding *fully* refute / support the claim, or only partially? Be honest about scope.
- What is the strongest counter-reading of the cited paper, and why does it not block the move?

## Process

- Once accepted, this PR will:
  - Update the per-claim ledger table in the programme file.
  - Add an entry to `tracker/falsification-events.md` with the date, claim, new status, and citation.
  - Update the ledger summary table in `README.md` (run `python scripts/render_ledger.py --write-readme`).

- Approval requirements:
  - 🟢 ↔ 🔴 transitions: two maintainer approvals.
  - Any other transition: one maintainer approval.

- We do not block on unanimity; we block on evidence. A serious disagreement
  between maintainers becomes a thread on the issue rather than a delay.
