# Security Policy

> This is a research-curation repository. The threat model is small: there is
> no service to compromise. The risks worth documenting are around (a)
> repository hygiene (no leaked secrets in the history), (b) supply-chain
> trust for the notebooks (no malicious dependency suggestions), and (c) the
> integrity of the falsification ledger (no fabricated citations).

---

## Reporting a vulnerability

If you find a security issue — leaked credentials in the git history, a
malicious dependency hidden in `notebooks/requirements.txt`, a hidden script
that does something the docs do not advertise, etc. — **do not open a public
issue.** Instead:

1. Email the maintainers at `security@<repo-domain>` (placeholder; replace with
   the real address before launch).
2. Or use GitHub's [private vulnerability reporting](https://docs.github.com/en/code-security/security-advisories/guidance-on-reporting-and-writing-information-about-vulnerabilities/privately-reporting-a-security-vulnerability)
   on the repo page.

We will acknowledge receipt within 72 hours. Coordinated-disclosure norms
apply: we ask for 14 days before public disclosure unless the issue is
actively being exploited.

---

## Hardening commitments

The repo runs the following automated checks:

- **Gitleaks** (`.gitleaks.toml` + `.github/workflows/secret-scan.yml`) scans
  every push, every PR, and weekly the entire history. Configured to allow
  the only "false positive" we expect (arXiv IDs that look like numeric
  strings).
- **Pinned dependencies** in `notebooks/requirements.txt`. We do not use
  unbounded `>=` version specs on the runtime path.
- **CI on every PR** runs `scripts/verify_citations.py` (no fabricated
  arXiv IDs) and `scripts/check_links.py` (no dead links). Both block the
  build on hard failures.
- **No GitHub Apps with write permission**. The repo's automation is limited
  to the workflows in `.github/workflows/`.
- **No long-lived secrets**. The repo does not store API keys, tokens, or
  credentials of any kind. The `arxiv-ingest` workflow uses only the
  workflow-issued `GITHUB_TOKEN`.

---

## Out-of-scope

- "I disagree with this status verdict." Open a [status-change issue](.github/ISSUE_TEMPLATE/status-change.md);
  it is not a security issue.
- "This paper is misrepresented in an annotation." Open a [paper-suggestion
  issue](.github/ISSUE_TEMPLATE/paper-suggestion.md) with the corrected
  annotation.
- "Notebook 03 runs slowly on my CPU." Performance is not a security issue.

If in doubt, open a regular issue. We will redirect to the private channel if
the report turns out to be security-relevant.
