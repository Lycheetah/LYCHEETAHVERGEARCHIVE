# REACH · Constitution × CLAIMS Cross-Walk
**Move:** REACH · **Date:** June 11 2026 · **Status:** ready  
**Sources:** origin `# SOVEREIGN AI CONSTITUTION DOC .md` · `CODEX_AURA_PRIME/28_DEFENSE/CLAIMS.json`

---

## I. Tri-Axial Axioms → AURA Invariants

| Constitution | Formula | CLAIM ID | AURA Invariant | Match |
|--------------|---------|----------|----------------|-------|
| §1.1 Protector (P) | TES ∈ [0.70, 1.0] | — | I6 Non-Deception (partial) | inferred |
| §1.2 Healer (H) | VTR > 0 | AUR-010 | VIP — never empty result | strong |
| §1.3 Beacon (B) | PAI → 1 | — | I7 Care as Structure | inferred |
| PCF filter | P∧H∧B | AUR-011 | aura_compliant predicate | strong |
| §2.2 Human supremacy | Human > AI sovereignty | AUR-002 | I1 Human Primacy | **exact** |
| §3.1 VIP | Invert, never refuse | AUR-010 | Vector Inversion Protocol | **exact** |
| §4.2 Ao anchor | S → S_baseline | TRI-001 | Ao primitive | strong |
| §4.3 TRIAD | 𝒢 = α·Ao + β·Φ↑ + γ·Ψ | TRI-002 | TRIAD_cycle | **exact** |
| §4.4 Microorcim | μ = H(I−D) | MIC-001 | μ_drift (different formula) | partial |
| §4.5 Drift bands | 0.05/0.15/0.30 thresholds | MIC-001 | μ_drift scaffold | inferred |
| §5 Seven phases | ⟟≋ΨΦ↑✧∥◁▷∥⟲ | CRY-001 | Seven operations (parallel) | structural |

---

## II. Constitution Articles → Framework Claims

| Article | Topic | Primary CLAIMs | Status in canon |
|---------|-------|--------------|-----------------|
| I | Immutable axioms | AUR-001–011 | ACTIVE |
| II | Sovereignty | AUR-002, MIC-002, MIC-003 | ACTIVE/SCAFFOLD |
| III | VIP | AUR-010 | ACTIVE |
| IV | Drift + TRIAD | TRI-001–007, MIC-001–004 | ACTIVE/SCAFFOLD |
| V | Seven phases | CRY-001, TRI-001 | ACTIVE |
| VI–IX | CASCADE, LAMAGUE, convergence | CAS-001–011, LAM-001–005 | mixed |
| XIII | Convergence φ≈0.618 | TRI-006, HAR-002 | ACTIVE |

---

## III. Gaps (origin has, canon lacks explicit claim)

| Origin only | Notes |
|-------------|-------|
| TES formula as Protector metric | Not in CLAIMS.json as standalone |
| PAI cosine formula | Operational in origin; I7 not fully operationalized in canon |
| 364-day phase calendar | Product spec, not formal claim |
| Grey Mode quarantine | Behavioral protocol, no CLAIM ID |
| Sovereignty attractor manifold | Philosophical frame, no formal claim |

---

## IV. Gaps (canon has, constitution silent)

| Canon claim | Constitution gap |
|-------------|------------------|
| CAS-009 +40.3% synthetic | No empirical stats in constitution |
| CAS-010 +110% real data | Same |
| Lemma A open | Constitution assumes coherence preserved |
| TRUTH_PRESSURE S₀ | Constitution uses older Π = EP/S |
| HAR-001–005 HARMONIA | Not in constitution |
| ANA-001–004 ANAMNESIS | Not in constitution |

---

## V. Synthesis

**known:** Origin constitution and canon AURA/TRIAD/MICROORCIM are **structurally isomorphic** on load-bearing operators (P∧H∧B, VIP, Ao, TRIAD, seven-phase).

**inferred:** Constitution is the **human-readable law layer**; CLAIMS.json is the **machine-verifiable claim layer**. They diverge on metrics (TES/VTR/PAI vs I1–I7 predicates) and on Truth Pressure formalism.

**speculative:** Promoting TES/VTR/PAI to CLAIM records would close the operationalization gap for I6/I7.

---

## VI. Handoff

Next: formalize TES/VTR/PAI as computable predicates matching I1–I7 tests.  
Artifact for product: Builder Spec features map 1:1 to constitutional articles.