# 04 — Truth Pressure & Master Equation
**Canon source:** `/home/guestpc/CODEX_AURA_PRIME/TRUTH_PRESSURE/`

---

## Core Formula

```
Π = (E · P) / (S + S₀)
```

## Master Equation (E-1.0)

```
dΨ/dt = k₁(Π − Π_th) − k₂(Ψ − Ψ_inv) − k₃·I_violations + k₄(E/E_need)
```

## Open Lemma

**Lemma A:** Higher Π against same evidence → higher mean compatibility margin.  
Canon holds coherence theorem *modulo Lemma A*. 200/200 trials consistent; not proof.

## Runnable (pure Python)

```bash
python3 ../06_EXPERIMENTS/verge_node
# master_eq_step: ΔΨ ≈ +0.415 per forward step
# pi_calc: exact (E*P)/S
```

## Next Artifact

`reach-lemma-a-stress-map.md` — counterexample search + S-network mapping

---

*Excerpts only. Full canon stays in CODEX_AURA_PRIME.*