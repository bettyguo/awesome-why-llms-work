<!--
Thank you for the PR. This template is mandatory — sections that do not apply
to your PR should be filled in with "n/a", not deleted.
-->

## What this PR changes

One or two sentences. Conventional Commit-style ("feat:", "docs:", "fix:") if applicable.

## Type

- [ ] Adding a paper to an existing programme (use [`paper-suggestion.md`](./ISSUE_TEMPLATE/paper-suggestion.md) for the schema fields).
- [ ] Status change (a 🟢 / 🟡 / 🔴 / ⚪ transition; requires [`status-change.md`](./ISSUE_TEMPLATE/status-change.md) issue first).
- [ ] New programme proposal (requires [`new-programme.md`](./ISSUE_TEMPLATE/new-programme.md) issue first).
- [ ] New / updated notebook.
- [ ] New / updated synthesis essay.
- [ ] Fixing a typo / dead link / broken notebook.
- [ ] Repository infrastructure (CI / scripts / templates).
- [ ] Other (describe below).

## Schema check (required for paper-adds and status changes)

- **Programme(s) affected**:
- **Claim ID(s) affected** (e.g., `01-D`, `04-E`):
- **Citations added/changed** (arXiv ID list):

For paper-adds, confirm:

- [ ] Each new entry follows the exact schema in [`CONTRIBUTING.md`](../CONTRIBUTING.md).
- [ ] The annotation is specific (not abstract paraphrase).
- [ ] The status assignment is defensible per the operational definitions.
- [ ] A falsifier is named (or `none`).

For status changes, confirm:

- [ ] A `status-change` issue was opened first.
- [ ] The cited paper is at workshop level or above.
- [ ] An entry was added to [`tracker/falsification-events.md`](../tracker/falsification-events.md).
- [ ] The programme file's ledger table is updated.
- [ ] The README ledger summary was regenerated (`python scripts/render_ledger.py --write-readme`).

## Quality bar

- [ ] `python scripts/verify_citations.py` is green locally (and in CI).
- [ ] `python scripts/check_links.py` is green locally (and in CI).
- [ ] For notebooks: runs end-to-end on a free Colab T4 in < 5 min; sets seeds; saves figures.
- [ ] For essays: addresses the strongest counter-argument explicitly.

## Notes for the reviewer

Anything else — including known limitations, related work you did *not* include
and why, or open questions you would like reviewer input on.
