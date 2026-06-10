# REACH · Lemma A Stress Map
**Move:** REACH · **Date:** June 11 2026 · **Status:** ready  
**Sources:** `CODEX_AURA_PRIME/TRUTH_PRESSURE/TRUTH_PRESSURE_CANON.md` §V · `cascade_engine.py`

---

## I. Lemma A (canonical statement)

> Higher Π against the **same evidence** implies higher **mean compatibility** with the evidence-consistent subset, with margin monotone in the Π gap.

**Blocks:** Cascade Coherence Theorem — canon says "demonstrably" (200/200), never "provably" until Lemma A closes.

---

## II. Formal setup

**Block-level pressure (canon):**
```
Π(b) = (E · P) / (S + S₀)     S₀ = 0.05
```

**Coherence (canon):**
```
C(Ψ) = mean pairwise φᵢⱼ over belief pairs
```

**Lemma A claim (expansion step):** If Π(b_new) > Π(b_old) + ε with fixed evidence (E,P), then mean φ(b_new, R) > mean φ(b_old, R) + f(ε) for retained set R.

---

## III. Counterexample search — the E·P masking hypothesis

**Attack vector:** Two blocks share identical (E, P) but differ in S and in compatibility with R.

| Block | E | P | S | Π = EP/(S+0.05) | mean φ with R |
|-------|---|---|---|-----------------|---------------|
| b_old | 0.8 | 2.0 | 0.40 | 3.90 | 0.72 |
| b_new | 0.8 | 2.0 | 0.10 | 12.31 | 0.35 |

**Same evidence. Higher Π. Lower compatibility.**

**Confidence:** known (arithmetic). This is a **toy counterexample** to the naive reading: Π alone does not encode φ.

---

## IV. Rescue condition (minimal sufficient)

Lemma A is true if additionally:

```
Π(b) = (E·P) / (S_strain(b) + S₀)
S_strain(b) = Σⱼ (1 − φᵢⱼ) · wᵢⱼ   over pairs involving b
```

Then high Π **requires** low strain, which **requires** high mean φ — counterexample in §III fails because S was independent of φ.

**Confidence:** inferred — this is the proof sketch canon implies but does not state.

---

## V. Implementation divergence (load-bearing)

| Object | Canon TRUTH_PRESSURE | cascade_engine.py |
|--------|---------------------|-------------------|
| S in Π | Coherence strain Σ(1−φ) or H(X\|Y) | Per-block `uncertainty` |
| φ in C(Ψ) | Embedding cosine similarity | Binary `contradicts()` only |
| Lemma A relevance | Gates formal theorem | Empirical 200/200 on simplified metric |

**Impact:** Lemma A must be proven in **canon semantics**. Engine may satisfy theorem empirically for different reasons.

---

## VI. Stress protocol (executable)

1. Fix (E,P) across candidate blocks
2. Sweep S ∈ {0.05, 0.1, 0.2, 0.4}
3. For each, assign φ grids with mean φ ∈ {0.3, 0.5, 0.7, 0.9}
4. Record: does higher Π always imply higher mean φ?
5. Repeat with S = f(φ) coupled (strain form)

**Script:** `06_EXPERIMENTS/lemma_a_search.py`

---

## VII. Verdict

| Reading | Status |
|---------|--------|
| Π with independent S | **COUNTEREXAMPLE EXISTS** |
| Π with S = strain(φ) | **PLAUSIBLE** — proof sketch, not closed |
| Engine implementation | **CONSISTENT** with 200/200 but not Lemma A in canon form |

**Recommendation:** Retire naive Lemma A. Replace with **Lemma A′ (strain-coupled):** Π computed from strain that includes φ → compatibility margin monotone.

---

## VIII. Handoff

**Canon edit (Claude/Mac):** Clarify S definition in §V; state Lemma A′ or coupling assumption explicitly.  
**Verge next:** Run `lemma_a_search.py` sweep; log to FINDINGS.