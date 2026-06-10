# REACH · E-1.0 Zero Calibration Map
**Move:** REACH · **Date:** June 11 2026 · **Status:** ready  
**Source:** `CODEX_AURA_PRIME/TRUTH_PRESSURE/MASTER_EQUATION.md`

---

## I. Master equation (ACTIVE structure)

```
dΨ/dt = k₁(Π − Π_th) − k₂(Ψ − Ψ_inv) − k₃·I_violations + k₄(E/E_need)
```

**Status:** Equation ACTIVE (Lyapunov verified). **k₁–k₄ all SCAFFOLD.**

---

## II. Calibration experiments

| Exp | k | Protocol | n | Expected |
|-----|---|----------|---|----------|
| E-1.0a | k₁ | τ vs Π excess {0.1,0.2,0.5,1.0} | 200 | 0.5–1.5 |
| E-1.0b | k₂ | Perturb stable Ψ_inv, measure return | 90 | AI 2–3, human 0.5–1 |
| E-1.0c | k₃ | Contradiction count {1,2,5} vs clean rate | 120 | 0.2–0.5 |
| E-1.0d | k₄ | P(reorg) vs E/E_need at 0.95·Π_th | 60 | 0.3–0.7 |

**Post-E-1.0 targets:** k₁≈1.0, k₂≈2.5, k₃≈0.35, k₄≈0.50 (± as stated in canon)

---

## III. k → framework limb map

| k | Term | Framework | Physical meaning |
|---|------|-----------|------------------|
| k₁ | Π drive | CASCADE | Reorganization rate above threshold |
| k₂ | Ψ restore | TRIAD / AURA | Attractor stiffness |
| k₃ | I_v drag | AURA I1–I7 | Violation friction |
| k₄ | E sufficiency | CASCADE evidence | Fuel for cascade |

---

## IV. Dependency graph

```
[Effective rank of G] → validates √n → Π_th DERIVED
         ↓
[S₀ pre-registration] + [E-1.0a-d] → k₁–k₄ ACTIVE
         ↓
[CR1–CR4 measurement] → critical regime confirmed
[Lemma A′] → coherence theorem unconditional
```

**Highest leverage first:** effective rank measurement (canon §VIII obligation #1)

---

## V. Runnable harness (known)

`verge_node master_eq_step`: ΔΨ = +0.415 per step (k₁=0.5, k₂=0.3, k₃=0.2, k₄=0.1 priors)

**Falsifier:** Parameter sweep shows unstable trajectories outside Lyapunov bounds.

---

## VI. Handoff

Design review only today — no E-1.0 execution without Mac pre-registration call.  
Next experiment: E4 k-parameter sweep in `06_EXPERIMENTS/`.