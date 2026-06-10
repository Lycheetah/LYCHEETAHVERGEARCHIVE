# REACH · S Definition Divergence Table
**Move:** REACH · **Date:** June 11 2026 · **Status:** ready

---

## Three definitions of S in the corpus

| Source | S means | Formula |
|--------|---------|---------|
| TRUTH_PRESSURE_CANON | Coherence strain / H(X\|Y) | Σ(1−φ_ij) or conditional entropy |
| PI_DERIVATION | Coherence strain | Σ_ij (1−φ_ij)·\|b_i∧b_j\| |
| cascade_engine.py | Per-block uncertainty | `block.uncertainty` ∈ (0,1] |

---

## Impact chain

```
S definition → Π value → Gate 1 winner → Lemma A validity → C(Ψ) metric
```

Independent S (engine) enabled Lemma A counterexample.  
Strain-coupled S (canon) requires Lemma A′.

---

## Resolution options

| Option | Action |
|--------|--------|
| A | Align engine S to strain(φ) per block |
| B | Split symbols: S_strain vs S_uncertainty in canon |
| C | Retire block-level Π; use RSS only |

**Recommendation:** Option B short-term (honest naming), Option A long-term (unification).

---

## Handoff

Canon edit + engine audit in same PR. Verge does not edit canon — MAP to Claude.