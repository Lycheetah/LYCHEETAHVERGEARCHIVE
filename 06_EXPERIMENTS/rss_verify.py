#!/usr/bin/env python3
"""Verify canon RSS composition vs cascade_engine per-block Pi logic."""
import math

S0 = 0.05

def block_pi(E, P, S):
    return (E * P) / (S + S0)

def canon_pi_sys(block_pis):
    """Canon: Pi_sys = sqrt(sum Pi(b)^2) over conflicting set K."""
    return math.sqrt(sum(p * p for p in block_pis))

def engine_gate1(new_pi, incumbent_pi, margin=0.3):
    """Engine Gate 1: block wins if Pi_new > Pi_incumbent + margin."""
    return new_pi > incumbent_pi + margin

def main():
    print("=== RSS vs ENGINE DIVERGENCE CHECK ===\n")

    # Scenario: 10 blocks at Pi ~ 1.8 (Kuhnian anomaly accumulation)
    n = 50
    pi_th = 0.8 * math.sqrt(n)  # canon k=0.8
    blocks = [1.8] * 10

    pi_sys = canon_pi_sys(blocks)
    print(f"n={n}  Pi_th={pi_th:.2f}  k=0.8")
    print(f"10 blocks @ Pi=1.8  ->  Pi_sys={pi_sys:.2f}  ({pi_sys/pi_th*100:.0f}% of threshold)")
    print(f"Gate 2 (canon RSS): {'FIRE' if pi_sys > pi_th else 'hold'}\n")

    # Engine uses per-block threshold only (1.5 FOUNDATION, 1.2 THEORY)
    print("Engine behavior (cascade_engine.py):")
    print("  - Pi = (E*P)/uncertainty  [NOT RSS, NOT strain]")
    print("  - Cascade: pairwise contradict + block Gate 1 only")
    print("  - NO Gate 2 system-level Pi_sys check")
    print("  - Coherence: 1 - contradictions/pairs [NOT embedding phi]\n")

    print("DIVERGENCE TABLE:")
    rows = [
        ("Pi formula", "EP/(S+S0) strain", "EP/uncertainty"),
        ("System composition", "RSS sqrt(sum Pi^2)", "none"),
        ("Gate 2", "Pi_sys > k*sqrt(n)", "absent"),
        ("Coherence C", "mean phi embeddings", "1 - contradiction rate"),
        ("Lemma A", "strain-coupled S", "independent uncertainty"),
    ]
    for name, canon, engine in rows:
        print(f"  {name:22} canon={canon:28} engine={engine}")

    print("\nVERDICT: Engine implements block-level adjudication, NOT full two-gate RSS.")
    print("Obligation: revise engine OR revise canon §IV (canon names this).")

if __name__ == "__main__":
    main()