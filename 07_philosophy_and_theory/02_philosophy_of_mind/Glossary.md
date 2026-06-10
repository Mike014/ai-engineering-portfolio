Here is a glossary (in alphabetical order, with dashes) of recurring terms so far.

* **Abstraction (λ-calculus)**: operator `λx.[…]` that constructs functions by treating `x` as a "hole" variable to be replaced with an argument.

* **AGI (Artificial General Intelligence)**: hypothetical AI capable of performing a wide range of cognitive tasks with human-like flexibility.

* **Algorithm**: finite, unambiguous, and mechanical procedure that transforms input into output.

* **Base_prob**: starting probability in the ENTITY gate, before adjustments (tension, emotion, memory, etc.).

* **Binary (notation)**: number representation with digits 0/1; also used to encode states, instructions, tapes.

* **Blacklist**: list of forbidden words/phrases checked by validator.

* **Boost (temporal)**: probability increase to speak when pauses exceed thresholds (micro/short/long).

* **Church–Turing Thesis**: "computable" = calculable by a Turing machine (or equivalent formalisms).

* **Cooldown**: forced pause after an intervention to avoid bursts of responses.

* **Creative Commons licenses (e.g., BY-NC-ND)**: licenses regulating use/redistribution (attribution, non-commercial, no derivative works).

* **Decidability**: property of a problem for which an algorithm exists that gives correct answer in finite time for every input.

* **Defense-in-depth**: multiple independent security layers (pre-filter → policy → generation → post-validator → fallback).

* **Diagonalization**: Cantor/Turing trick to construct a sequence that differs from every row of a computable table (used in the *halting* proof).

* **Division with remainder (Euclidean algorithm)**: classic procedure for GCD; example of algorithm implementable by TM.

* **EMA (Exponential Moving Average)**: exponential moving average that gives more weight to recent events (used for silence/tension/rhythm).

* **Emotional bias**: probabilistic offset due to emotional state (e.g., *curious* +0.12, *bored* −0.08, *irritated* +0.22).

* **Emotions (states)**: *curious*, *bored*, *irritated*; influence the gate through bias and hysteresis.

* **Encoding (contraction/expansion)**: rules to map binary strings into numerical sequences and vice versa to delimit numbers/instructions on the tape.

* **ENTITY (non-deterministic NPC)**: character that probabilistically decides *if/how/when* to speak, with consistent style and local memory.

* **Entscheidungsproblem**: Hilbert's problem: does a general algorithm exist to decide mathematical truth (in certain classes)? Answer: no.

* **Euclid's algorithm**: see Division with remainder.

* **Expanded binary encoding**: Penrose's convention to separate numbers/markers (2=",", 3,4,5… as symbols) in 0/1 strings.

* **Explainability / Why-log**: internal traces (p, factors, state) that explain why the NPC spoke or remained silent.

* **Fermat's Last Theorem**: example of problem encodable as *halting* of a TM searching for solutions; now known to be true.

* **Flow chart**: graphical representation of an algorithm in steps/branches.

* **Frequency penalty / Presence penalty**: generation penalties to reduce repetitions or reappearances of tokens.

* **Gate (probabilistic)**: decision `speak/stay_silent` by comparing a calculated `p` (0..1) with a random draw.

* **Generation (temperature, top_p)**: sampling parameters to vary creativity/diversity of output.

* **Gödel's theorem**: shows formal limits of axiomatic systems (related to algorithmic limits; context in Penrose's book).

* **Goldbach's conjecture**: another example frameable as *halting*: the TM stops only if it finds a counterexample.

* **Half-life (EMAs)**: time after which past contribution weighs ~50% compared to present.

* **Halting Problem**: given a program and input, does an algorithm exist that always decides if it halts? No (Turing).

* **History buffer (local memory)**: sliding window of recent turns for short-term contextual coherence.

* **Hysteresis**: minimum persistence in an emotional state to avoid bouncing.

* **Input/Output (I/O)**: input/output data; in TMs they are strings on the tape.

* **Jailbreak / role-play**: techniques to bypass filters by inducing the model into roles/contexts that evade policy.

* **Kill switch**: emergency switch to block the system.

* **LISP**: language that inherits from λ-calculus (functions as first-class citizens).

* **Logging & versioning**: tracking of versions, prompts, filters and blocking reasons for audit/diagnosis.

* **Metrics (ENTITY)**: p, speak rate, validator discard rate, time to first speak, coherence, etc.

* **Min_gap (micro/short/long)**: temporal pause thresholds that modulate intervention boost.

* **Non-computable**: function/number that no TM can compute (e.g., certain real sequences).

* **Non-determinism**: behavior with outcome not fixed in advance (in ENTITY, via probability and noise).

* **Ok_ratio**: validator metric (quota of "plausible"/acceptable tokens in output).

* **Operational/mechanical (effective/recursive procedure)**: classic synonyms for "algorithmic" in logical-mathematical contexts.

* **Penrose (view)**: hypothesis that mind/consciousness employs physical processes not (solely) algorithmic; critique of "strong AI".

* **Policy design**: design of rules/filters/thresholds (system prompt, pre/post-filters, fallback) for safety and coherence.

* **Post-filter / Pre-filter**: downstream/upstream checks of generation; eliminate forbidden or non-compliant content.

* **Probability p (gating)**: final estimate 0..1 that ENTITY uses to decide whether to speak.

* **Prob_ceil / Prob_floor**: saturation caps for p (upper/lower limits).

* **Prompt**: instructions/text guiding the model (user/system).

* **Rate control**: feedback that increases/decreases p based on how much one has spoken relative to target.

* **Rate limit**: frequency/volume limits for safety, costs or UX.

* **Red teaming**: adversarial security testing (multilingual, roleplay, obfuscation) to find vulnerabilities.

* **Reinforcement Learning from Human Feedback (RLHF)**: technique to align models with human preferences/safety using human feedback as reinforcement signal.

* **Safety filters**: sets of rules/models that block forbidden or risky content.

* **Sandbox**: confined execution of legacy/experimental components with reduced scope and permissions.

* **Searle – Chinese Room**: argument contesting the equivalence "algorithm = understanding".

* **Speak rate**: EMA of frequency with which ENTITY has recently spoken.

* **Stop tokens**: sequences that signal the generator to interrupt output.

* **Subroutine**: algorithm called by another algorithm (modular reuse).

* **System prompt**: "system" prompt that gives identity/limits to the model before conversation.

* **Tape**: ideal support of the TM, infinite in both directions, made of cells with 0/1 (and "blank").

* **Temperature**: sampling parameter that controls exploration (higher = more variety).

* **Temporal asymmetry**: logic whereby the NPC doesn't always respond immediately; decides *if/when* to speak, not just *what* to say.

* **Tension (tension metric)**: derived measure (often via EMA) representing the "charge" of the scene/pause.

* **Turing Machine (TM)**: abstract model with finite states, infinite tape, read/write/move head and deterministic instructions.

* **Turing Test**: behavioral criterion: if indistinguishable from a human in conversation, it "thinks" (debated).

* **Unary (unary notation)**: number representation as sequences of '1'; simple but inefficient.

* **Universal (UTM)**: see Universal Turing Machine.

* **Universal Turing Machine (UTM)**: TM that, reading the description of another TM, emulates it (concept of "general computer").

* **Validator**: final filter that accepts/discards sentences (length, punctuation, duplicates, ok_ratio, blacklist).

* **Versioning**: version management (model, prompt, filters) for comparisons, audit and rollback.

* **λ-calculus (Lambda calculus)**: Church's formalism for computation using only functions and abstraction; equivalent to Turing machines.