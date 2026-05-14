# Glossary

A working vocabulary for the five programmes. Definitions are short and *programme-aware*: where a term means different things in different programmes, we note it. *See also* links are to the programme files that use the term most.

Terms are alphabetized. Total: 60+. Suggest additions via PR.

---

### Ablation

The intervention of removing or zeroing-out a component of a network (a neuron, an attention head, a residual-stream direction) to measure the resulting change in behavior. The basic causal-validation tool for circuit discovery. *See also*: [Activation patching](#activation-patching), [Programme 03](programmes/03-circuits-and-biology.md).

### Activation patching

A causal-intervention method where activations from one forward pass are spliced into another at a chosen location, then downstream behavior is measured. Sharper than ablation: lets you ask "if this component had the value it would have had on input B, would the model behave as on B at the output?" *See also*: [Path patching](#path-patching), [Programme 03](programmes/03-circuits-and-biology.md).

### Algorithmic complexity / Kolmogorov complexity

The length of the shortest program that produces a given string. Uncomputable in general; the philosophical anchor of compression-as-intelligence is that approximations to algorithmic complexity (achievable compression) are the right measure of "how much pattern is in" something. *See also*: [Solomonoff induction](#solomonoff-induction), [Programme 01](programmes/01-compression-as-intelligence.md).

### Arithmetic coding

A lossless compression scheme that encodes a sequence using its predicted probabilities; with a good predictor, achieves near-optimal compression. Used by Delétang et al. (2023) to operationalize "language model as compressor" literally. *See also*: [Bits-per-byte](#bits-per-byte), [Programme 01](programmes/01-compression-as-intelligence.md).

### Attention head

A single attention sub-component within a transformer layer. Each head has its own QK (where to attend) and OV (what to write) circuits, in the mathematical framework of Elhage et al. 2021. The atomic unit of much circuit analysis. *See also*: [Induction head](#induction-head), [QK / OV circuits](#qk--ov-circuits).

### Attribution patching

A scalable approximation to activation patching that uses gradients to estimate the effect of a hypothetical patch without running the patched forward pass. Underlies several automated circuit-discovery methods (ACDC variants, EAP-IG). *See also*: [Programme 03](programmes/03-circuits-and-biology.md).

### AIXI

A hypothetical agent defined by Marcus Hutter that maximizes expected reward over all computable environments, weighted by a Solomonoff prior. Formally optimal but uncomputable; the philosophical anchor of *compression-is-intelligence*. *See also*: [Solomonoff induction](#solomonoff-induction), [Programme 01](programmes/01-compression-as-intelligence.md).

### Bayes-optimal predictor

The predictor that minimizes expected loss given a known prior — for a sequence, it averages the next-token probability over a posterior on the latent generating process. In Programme 04, the *target* against which ICL behavior is compared. *See also*: [In-context learning](#in-context-learning), [Programme 04](programmes/04-icl-as-bayes-meta-learning.md).

### Bits-per-byte (bpb)

A normalization of language-model log-loss: how many *bits* the model needs, per *byte* of input text, to encode the text losslessly via the predictor → compressor identity. Choice of bpb (vs. bits-per-token) cancels tokenization-dependence in cross-model comparisons. *See also*: [Programme 01](programmes/01-compression-as-intelligence.md).

### Circuit

A small, identifiable sub-graph of a network — typically attention heads, MLP neurons, SAE features, and the edges between them — that together implement a specific behavior. The fundamental unit of Programme 03; the *unit* of mechanistic explanation. *See also*: [Programme 03](programmes/03-circuits-and-biology.md).

### Codebook features

An interpretability primitive (Tamkin et al. 2023) where activations are quantized to a discrete codebook; an alternative to dense linear features for surfacing what models represent. *See also*: [Sparse autoencoder](#sparse-autoencoder), [Programme 02](programmes/02-superposition-linear-rep.md).

### Compression ratio

The factor by which lossless compression shrinks a corpus. As an LLM evaluation, the inverse of bits-per-byte; conventionally reported on a fixed reference corpus (e.g., enwiki8). *See also*: [Bits-per-byte](#bits-per-byte), [Programme 01](programmes/01-compression-as-intelligence.md).

### Compression-as-intelligence

The thesis that lossless-compression performance and general capability are tightly coupled — at the philosophical level (Hutter), at the formal level (Solomonoff), and at the empirical level (Huang et al. 2024). The hard core of [Programme 01](programmes/01-compression-as-intelligence.md).

### Chain-of-thought (CoT)

A prompting and training pattern in which the model produces intermediate reasoning steps before its final answer. Crucial for the reasoning-models wave (o1, R1, s1). *See also*: [Test-time compute](#test-time-compute), [Programme 05](programmes/05-emergence-and-reasoning.md).

### Direction

A vector in activation space whose presence/absence (or magnitude) the model uses to represent a feature. The unit of the Linear Representation Hypothesis. *See also*: [Linear Representation Hypothesis](#linear-representation-hypothesis-lrh), [Programme 02](programmes/02-superposition-linear-rep.md).

### Dictionary learning

The class of methods (including SAEs) that decompose activations into a sparse, overcomplete dictionary of "atoms" (features). The current standard tool for surfacing the directions that an LM uses. *See also*: [Sparse autoencoder](#sparse-autoencoder).

### Edge attribution patching

A variant of attribution patching where the unit is an *edge* (a pair-wise composition of components) rather than a component. Important for graph-structured circuit discovery. *See also*: [Attribution patching](#attribution-patching), [Programme 03](programmes/03-circuits-and-biology.md).

### Emergence (strong)

The claim that some capabilities are present discontinuously as a function of training scale, in a way that is *not predictable* from smaller-scale runs under any continuous metric. Originally Wei et al. 2022; substantially refuted in this strong form by Schaeffer et al. 2023. *See also*: [Programme 05](programmes/05-emergence-and-reasoning.md).

### Emergence (weak / operational)

The descriptive observation that under common evaluation metrics (exact-match, multi-choice), capability curves often appear sharp. Survives the Schaeffer et al. critique; useful as a forecasting signal. *See also*: [Programme 05](programmes/05-emergence-and-reasoning.md).

### Falsifier

A specific empirical observation that would, if obtained, move a claim's status to 🔴 Refuted. Every claim in this repo is supposed to come with at least one. *See also*: [Status taxonomy](#status-taxonomy).

### Feature

A behaviorally relevant, interpretable variable that a model represents. Usually identified by SAEs in modern work. The "atomic" unit of Programme 02. The definition is operational ("whatever a sufficiently good interpretability technique surfaces") and is itself contested. *See also*: [Sparse autoencoder](#sparse-autoencoder), [Programme 02](programmes/02-superposition-linear-rep.md).

### Feature splitting

The phenomenon where, as an SAE dictionary grows wider, a single feature splits into multiple finer-grained features. Complicates the "right number of features" question. *See also*: [Programme 02](programmes/02-superposition-linear-rep.md).

### Free Energy Principle

Friston's framework treating cognition as variational free-energy minimization. Conceptually related to (and arguably identical with) predictive coding and to the Bayesian frame on ICL. *See also*: [Adjacent programmes](programmes/adjacent-programmes.md#predictive-coding--free-energy).

### Grokking

The phenomenon where a neural network achieves near-zero training loss but chance-level test performance, then suddenly generalizes much later in training. Originally Power et al. 2022; mechanistic explanation by Nanda et al. 2023. *See also*: [Phase transition](#phase-transition), [Programme 05](programmes/05-emergence-and-reasoning.md).

### Hard core (Lakatos)

The central, non-negotiable claims of a research programme. Auxiliary "protective belt" hypotheses can be modified to absorb refutations; the hard core cannot be without abandoning the programme. *See also*: [Protective belt](#protective-belt).

### Induction head

An attention head (or pair of heads) that implements the pattern "if the previous occurrence of this token was followed by X, output X." The canonical circuit motif of Programme 03 and the mechanistic backbone of an important class of ICL behaviors. *See also*: [Programme 03](programmes/03-circuits-and-biology.md), [Programme 04](programmes/04-icl-as-bayes-meta-learning.md).

### In-context learning (ICL)

The model's ability to perform a task given only examples in the prompt, without parameter updates. The phenomenon Programme 04 is trying to explain. *See also*: [Bayes-optimal predictor](#bayes-optimal-predictor), [Programme 04](programmes/04-icl-as-bayes-meta-learning.md).

### Interpretability

The broad family of methods aimed at understanding what trained networks compute and how. Mechanistic interpretability is one subset, oriented toward reverse-engineering circuits and features. *See also*: [Mechanistic interpretability](#mechanistic-interpretability).

### Kolmogorov complexity

See [Algorithmic complexity](#algorithmic-complexity--kolmogorov-complexity).

### Latent task

In the Bayesian frame on ICL, the (hidden) variable indexing which task the in-context examples are describing. The Bayes-optimal predictor marginalizes over it. *See also*: [Programme 04](programmes/04-icl-as-bayes-meta-learning.md).

### Linear probe

A linear classifier trained on activations to predict an attribute. Useful for testing whether a feature is *linearly readable* (the operational form of the Linear Representation Hypothesis). Has well-known pathologies — probes can succeed when the model itself does not use the information. *See also*: [Linear Representation Hypothesis](#linear-representation-hypothesis-lrh), [Programme 02](programmes/02-superposition-linear-rep.md).

### Linear Representation Hypothesis (LRH)

The claim that at least a non-trivial subset of features in trained models are represented as approximately linear directions in activation space; binary attributes especially are recoverable by linear methods. Park, Choe, Veitch (2023) gives a careful formal statement. *See also*: [Direction](#direction), [Programme 02](programmes/02-superposition-linear-rep.md).

### Logit lens

A diagnostic that decodes residual-stream activations at intermediate layers through the model's unembedding matrix, producing layer-by-layer predicted-token distributions. Originated in early LessWrong / nostalgebraist posts; now a standard inspection tool. *See also*: [Programme 03](programmes/03-circuits-and-biology.md).

### Mechanistic interpretability (MI)

A subset of interpretability that aims to *reverse-engineer* trained networks: find the circuits, identify their components, validate causally. Centered on Programmes 02 and 03 in this repo. *See also*: [Circuit](#circuit), [Programme 03](programmes/03-circuits-and-biology.md).

### Minimum Description Length (MDL)

A model-selection principle: prefer the model whose description plus its description of the data is shortest. The formal cousin of compression-as-intelligence and the AIXI / Solomonoff family. *See also*: [Solomonoff induction](#solomonoff-induction), [Programme 01](programmes/01-compression-as-intelligence.md).

### Monosemanticity

The property of a feature (or neuron) that activates for a single, interpretable concept rather than several unrelated ones. The desired result of dictionary-learning methods; the target of *Towards Monosemanticity* (Bricken et al. 2023). *See also*: [Polysemanticity](#polysemanticity), [Programme 02](programmes/02-superposition-linear-rep.md).

### MLP / FFN

The position-wise feedforward sub-component of a transformer block (two linear layers and a nonlinearity). Stores much of the "knowledge" content of models in many analyses; the home of many monosemantic features. *See also*: [Programme 03](programmes/03-circuits-and-biology.md).

### Neuron

In LLM-MI usage, a single hidden-unit dimension of an MLP. Classically the unit of "interpretability"; the early polysemanticity literature establishes that *neurons* are usually not the right unit and that *features* are. *See also*: [Feature](#feature), [Polysemanticity](#polysemanticity).

### Path patching

A circuit-discovery technique where activations are patched along a *specific path* between components rather than at a single point, to isolate the contribution of a particular edge in the computational graph. *See also*: [Activation patching](#activation-patching), [Programme 03](programmes/03-circuits-and-biology.md).

### Phase transition

A relatively sharp change in some learning quantity (loss, accuracy, internal-state metric) as a function of training step or model scale. Used in this repo for grokking-type transitions (Programme 05) and circuit-formation transitions (Programme 03). *See also*: [Grokking](#grokking), [Emergence (strong)](#emergence-strong).

### Platonic Representation Hypothesis

Huh et al. 2024's claim that representations across different deep models converge to a shared statistical representation of reality. *See also*: [Adjacent programmes](programmes/adjacent-programmes.md#platonic-representation-hypothesis).

### Polysemanticity

The property of a neuron that activates for multiple unrelated concepts. The motivating problem for the feature-first turn in interpretability (and for the toy-superposition framework). *See also*: [Monosemanticity](#monosemanticity), [Programme 02](programmes/02-superposition-linear-rep.md).

### Predictive coding

A theory from computational neuroscience holding that perception is approximate Bayesian inference implemented by minimizing prediction error; argued by some to be the right ML-cognition analogy. *See also*: [Adjacent programmes](programmes/adjacent-programmes.md#predictive-coding--free-energy).

### Protective belt (Lakatos)

The auxiliary hypotheses around a programme's hard core that absorb local refutations. Modifying the belt to handle refutations is legitimate; modifying the hard core is abandoning the programme. *See also*: [Hard core](#hard-core-lakatos).

### QK / OV circuits

In the Elhage et al. 2021 framework, the two functional sub-circuits within an attention head: QK ("where to attend") and OV ("what to write"). The vocabulary of much circuit work. *See also*: [Programme 03](programmes/03-circuits-and-biology.md).

### Real Log Canonical Threshold (RLCT / $\lambda$)

The central technical object of Singular Learning Theory; an algebraic-geometric invariant of the loss landscape that controls generalization and learning dynamics in singular settings. *See also*: [Singular Learning Theory](#singular-learning-theory), [Adjacent programmes](programmes/adjacent-programmes.md#singular-learning-theory).

### Refusal direction

A specific residual-stream direction implicated in safety-relevant refusal behavior (Arditi et al. 2024); ablating the direction removes refusal across many models. A clean example of "behavior mediated by a direction" rather than a multi-component circuit. *See also*: [Programme 03](programmes/03-circuits-and-biology.md).

### Residual stream

The shared activation channel of a transformer: each block reads from and writes to the residual stream, and the unembedding reads the residual stream at the final position. The natural "highway" in which features live. *See also*: [Programme 02](programmes/02-superposition-linear-rep.md), [Programme 03](programmes/03-circuits-and-biology.md).

### Scaling law

An empirical functional form (typically a power law) for some performance measure as a function of model size, data, or compute. The measurement framework used by Programmes 01 and 05; not itself a programme. *See also*: [Programme 05](programmes/05-emergence-and-reasoning.md).

### Sparse autoencoder (SAE)

An autoencoder trained on the activations of a target model with a sparsity constraint, producing a dictionary of feature directions. The dominant tool for surfacing features under the LRH frame. *See also*: [Feature](#feature), [Programme 02](programmes/02-superposition-linear-rep.md).

### Singular Learning Theory (SLT)

Watanabe's algebraic-statistical framework for learning theory in singular models. Increasingly cited in the alignment community as a lens on phase transitions in training. *See also*: [Adjacent programmes](programmes/adjacent-programmes.md#singular-learning-theory).

### Solomonoff induction

A formal theory of universal prediction: the predictor whose prior over hypotheses is weighted by program length under a universal Turing machine. Uncomputable but provably optimal in a precise sense. The formal ancestor of compression-as-intelligence. *See also*: [AIXI](#aixi), [Programme 01](programmes/01-compression-as-intelligence.md).

### Status taxonomy

The four-valued epistemic status used in this repo: 🟢 Supported / 🟡 Contested / 🔴 Refuted / ⚪ Open. Definitions and merge rules in [`CONTRIBUTING.md`](CONTRIBUTING.md). *See also*: [`programmes/README.md`](programmes/README.md).

### Steering vector

A direction in activation space which, when added to the residual stream at inference time, predictably changes model behavior. The applied-LRH analogue of a control knob. *See also*: [Programme 02](programmes/02-superposition-linear-rep.md).

### Superposition

The property of trained networks of representing more features than they have neurons, by overlapping features as near-orthogonal directions in activation space. Established at toy scale by Elhage et al. 2022. *See also*: [Programme 02](programmes/02-superposition-linear-rep.md).

### Task vector

A direction in residual-stream space that, when added to the activations of a related task, switches behavior to the new task without retraining; a candidate mechanism for ICL on natural tasks. *See also*: [Programme 04](programmes/04-icl-as-bayes-meta-learning.md).

### Test-time compute (TTC)

Computation expended at inference time, including chain-of-thought sampling, search, self-consistency, and budget-forcing decoding. The lever pulled by the reasoning-models wave (o1, R1, s1). *See also*: [Programme 05](programmes/05-emergence-and-reasoning.md).

### Token-edit-distance

A continuous metric on model outputs (Levenshtein-like, at the token level). Used by Schaeffer et al. 2023 to argue that emergence-under-exact-match becomes smooth scaling under continuous metrics. *See also*: [Programme 05](programmes/05-emergence-and-reasoning.md).

### Toy model

A small, controlled network trained on a synthetic task, used to study a phenomenon (superposition, grokking, induction) at a scale where every parameter can be inspected. Programmes 02, 03, 05 all use toy models centrally. *See also*: [Toy Models of Superposition (Elhage et al. 2022)](https://transformer-circuits.pub/2022/toy_model/index.html).

### TransformerLens

An open-source library for white-box transformer analysis, originally maintained by Neel Nanda. The standard tooling stack for much of Programmes 02 and 03.

### Universality (in mechanistic interpretability)

The claim that the *same* feature or circuit motifs appear across model families and scales — induction heads being the best-supported example. A central sub-claim of both Programmes 02 and 03; the strong form is contested. *See also*: [Programme 02](programmes/02-superposition-linear-rep.md), [Programme 03](programmes/03-circuits-and-biology.md).

### Why-LLMs-work programme

Used throughout this repo, after Lakatos's *research programme*: a Hard Core + Protective Belt + Positive Heuristic + Evidence Ledger. Five of them carve up the space; see the README five-row table. *See also*: [`programmes/README.md`](programmes/README.md).
