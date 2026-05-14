# Adjacent Programmes

Theories that intersect the five core programmes but do not (yet) have a dense enough evidence ledger to stand alone as a programme. Each appendix entry sketches the claim and the relationship to the core five, and lists the criterion for promotion to a full programme.

Promotion criterion (per [`DECISIONS.md`](../DECISIONS.md#adr-0003--adjacent-programmes-are-an-appendix-not-a-sixth-slot)): at least 5 verifiable claims with non-trivial evidence ledgers, including at least one 🔴 or 🟡, and a named ≥-PhD-level critic.

---

## Singular Learning Theory

### What it is

A line of work originating with **Sumio Watanabe** in algebraic statistics, treating learning as a problem about the geometry of singular parameter spaces. The central technical object is the *Real Log Canonical Threshold* (RLCT, also called *learning coefficient* $\lambda$), which generalizes the role of dimension count in penalty-based generalization bounds to settings where the loss landscape contains degenerate (non-smooth) directions. In the alignment / interpretability community, SLT has been adopted as a lens on phase transitions and on which network parameters "matter."

### Relationship to the core programmes

- **Programme 05 — Emergence.** SLT predicts phase changes during training as the model transitions between regions of parameter space with different effective dimensions. The cleanest contact with empirical work is via grokking; SLT-flavored explanations of grokking are an active research line.
- **Programme 01 — Compression.** RLCT-style penalties relate to Minimum Description Length / Bayesian model selection, which is the formal home of compression-as-intelligence; the two frameworks are not in tension but are not currently unified empirically.
- **Programme 03 — Circuits.** Speculative: SLT might give principled answers to "which circuit components are minimally sufficient" and "what does a phase transition look like in circuit-space."

### Status as a programme

⚪ Open. SLT is a strong theoretical framework with growing empirical contact; it does not yet have the catalog of falsifiable empirical claims about real LMs that the five core programmes have. Promotion to a full programme requires (1) a published study connecting RLCT estimates of real trained LMs to a downstream empirical claim about their behavior, and (2) at least one published refutation or sharpening.

### Pointers

- Watanabe, *Algebraic Geometry and Statistical Learning Theory*, Cambridge 2009.
- The alignment-community writeups: Daniel Murfet, Edmund Lau, and Jesse Hoogland's expository sequences on LessWrong / Alignment Forum.
- *Open Problems in Mechanistic Interpretability* ([arXiv:2501.16496](https://arxiv.org/abs/2501.16496)) — Murfet and Hoogland are coauthors; SLT is explicitly mentioned as a connecting framework.

---

## Platonic Representation Hypothesis

### What it is

The conjecture, formalized by **Huh, Cheung, Wang, Isola (2024)**, that representations across different deep models — different architectures, different modalities, different objectives — are *converging* toward a shared statistical representation of reality. The convergence is itself the proposed explanation for why models trained on text help models trained on images and vice versa.

- [**The Platonic Representation Hypothesis** (2024)](https://arxiv.org/abs/2405.07987) — *Huh, Cheung, Wang, Isola*.

### Relationship to the core programmes

- **Programme 02 — Superposition / LRH.** The Platonic hypothesis is, in part, a cross-model generalization of the universality sub-claim of Programme 02. If different models converge to similar features, then LRH's "linear directions" should be cross-model-comparable. Several measurement methodologies for this comparison are being developed.
- **Programme 01 — Compression.** A natural reading: compression of the same world produces convergent representations of that world. The Platonic and Compression programmes share an information-theoretic spine.
- **Programme 03 — Circuits.** If representations converge, *circuits* over those representations might too — this is the strong cross-family universality sub-claim of Programme 03, here promoted to a research target.

### Status as a programme

⚪ Open (with one strong proposal paper). Promotion requires (1) follow-up empirical work testing the convergence claim across many model families and modalities, (2) a refutation paper or at least one published critical paper, (3) operationalization of "Platonic representation" beyond representation-alignment metrics.

### Pointers

- Huh et al. 2024, as above.
- Representation-alignment literature (model-stitching, Procrustes alignment of representations, CCA-based comparisons) is the empirical context.

---

## Predictive Coding / Free Energy

### What it is

The neuroscience-inspired hypothesis that the brain — and, by analogy, LLMs — minimizes prediction error / free energy as its core objective; that a wide range of intelligent behaviors derive from this optimization. The mathematical anchor is Karl Friston's free-energy principle.

### Relationship to the core programmes

- **Programme 01 — Compression.** Free-energy minimization and lossless-compression-via-prediction are very nearly the same optimization (the variational free energy bound is closely related to negative log-likelihood). The conceptual overlap is large; the distinct empirical content is small.
- **Programme 04 — ICL as Bayes.** Predictive-coding accounts of cortex are explicitly Bayesian; the same machinery applies, conceptually, to ICL.

### Why it is adjacent and not a core programme

In ML the analogies are productive but have not (yet) produced a distinct catalog of falsifiable LLM-specific claims. The Free Energy literature is rich in cognitive-neuroscience and active-inference settings; its bridging to transformer-specific phenomena is mostly through Compression and ICL-Bayes, which are already core programmes here.

### Status as a programme

⚪ Open. Promotion would require LLM-specific predictions distinct from those of Programmes 01 and 04.

### Pointers

- The free-energy-principle literature (Friston and colleagues). Useful conceptual background.
- The growing literature comparing predictive-coding-trained networks to transformers (mostly outside the scope of this repo).

---

## Grokking and phase transitions (as a candidate sub-programme of Emergence)

### What it is

The empirical phenomenon — and the family of theoretical explanations — by which neural networks generalize *long after* fitting the training set. Originally documented on modular addition by Power et al. (2022) and given a mechanistic explanation by Nanda et al. (2023).

- [**Grokking: Generalization Beyond Overfitting on Small Algorithmic Datasets** (2022)](https://arxiv.org/abs/2201.02177) — *Power, Burda, Edwards, Babuschkin, Misra*.
- [**Progress Measures for Grokking via Mechanistic Interpretability** (2023)](https://arxiv.org/abs/2301.05217) — *Nanda, Chan, Lieberum, Smith, Steinhardt*.

### Why it is adjacent, not core

In this repo we treat grokking as a sub-programme inside Programme 05 (Emergence). It has its own internal evidence ledger but the central theoretical claim — that internal phase transitions can be made mechanistically visible — is the operative finding of Programmes 03 and 05 together, not a separate programme.

### Conditions for promotion

If a future result shows grokking-like phase transitions for *non-algorithmic* tasks at scale — i.e., real-world capabilities — with a mechanistic explanation, the case for promoting grokking to a standalone programme becomes much stronger.

---

## Other candidates we considered and rejected

- **"Scaling laws"** as a programme. The scaling-laws literature is a measurement framework, not a theory of *why* LLMs work; it is referenced inside Programmes 01 and 05 but does not host a competing hard core.
- **"Reinforcement learning from human feedback / preference learning"** as a programme. Substantively about *alignment* and behavior shaping, not about why pretraining works. Out of scope.
- **"Mesa-optimization"** as a programme. The conjecture that trained networks contain internal optimizers is conceptually adjacent (intersects Programme 04 — ICL-as-optimizer — and Programme 03 — circuits as internal computational structure). We are watching the empirical evidence; not yet a programme.
- **"Tool use / agentic frameworks"** as a programme. About *how to use* LLMs, not why they work.

---

## How this file is maintained

Same conventions as the core programmes. To propose a new adjacent programme, use [`new-programme.md`](../.github/ISSUE_TEMPLATE/new-programme.md). To propose a promotion of an adjacent programme to a core programme, the bar is higher: explicit evidence-ledger checklist in the issue, and 30-day public discussion period.
