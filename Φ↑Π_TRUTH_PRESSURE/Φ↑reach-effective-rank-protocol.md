# REACH · Effective Rank Measurement Protocol
**Move:** REACH · **Date:** June 11 2026 · **Status:** ready  
**Source:** `TRUTH_PRESSURE_CANON.md` §III · `PI_THRESHOLD_DERIVATION.md` §3.4

---

## I. Why this is highest leverage

Canon states: if effective rank of interaction matrix G ≈ √n, then Π_th = k·√n graduates from ASSUMED to **MEASURED**.

If rank ~ n, √n claim is **killed outright**.

---

## II. Objects

**Interaction matrix G:** Jacobian J_ij = φ_ij − 0.5 from belief compatibility graph.

**Effective rank (participation ratio):**
```
r_eff = (Σᵢ σᵢ)² / Σᵢ σᵢ²
```
where σᵢ are singular values of G.

**Prediction:** r_eff / n ≈ 1/√n  →  r_eff ≈ √n

---

## III. Protocol

1. Sample CASCADE knowledge bases at n ∈ {10, 25, 50, 100}
2. Build φ_ij matrix (embedding cosine or contradiction graph)
3. Compute SVD → r_eff
4. Plot r_eff vs √n
5. Fit slope; compare to 1.0

**Falsifier:** r_eff scales linearly with n (dense coupling)

---

## IV. Implementation path

| Step | Tool | Status |
|------|------|--------|
| Synthetic KB generator | cascade_engine.py | exists |
| φ matrix from contradictions | engine `contradicts()` | partial |
| Embedding φ | EMPIRICAL_RESULTS spec | not wired |
| SVD r_eff | new `effective_rank.py` | queued |

---

## V. Handoff

Run after RSS/engine alignment decision. Blocks CR1-CR4 meaningfully.