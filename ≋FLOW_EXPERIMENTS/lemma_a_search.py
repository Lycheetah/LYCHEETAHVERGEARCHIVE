#!/usr/bin/env python3
"""Lemma A counterexample search — pure Python, no deps."""
S0 = 0.05

def pi(E, P, S):
    return (E * P) / (S + S0)

def strain_from_phi(mean_phi, n_pairs=10):
    return sum(1.0 - mean_phi for _ in range(n_pairs)) / n_pairs

def main():
    E, P = 0.8, 2.0
    print("=== LEMMA A STRESS SEARCH ===")
    print(f"Fixed evidence: E={E}, P={P}\n")

    print("--- Attack: independent S (counterexample hunt) ---")
    cases = [
        ("b_old", 0.40, 0.72),
        ("b_new", 0.10, 0.35),
        ("b_alt", 0.20, 0.55),
    ]
    for name, S, phi in cases:
        print(f"  {name}: S={S:.2f}  Pi={pi(E,P,S):.2f}  mean_phi={phi:.2f}")

    pi_old = pi(E, P, 0.40)
    pi_new = pi(E, P, 0.10)
    print(f"\n  Same E,P: Pi rises {pi_old:.2f} -> {pi_new:.2f} but phi drops 0.72 -> 0.35")
    print("  VERDICT: COUNTEREXAMPLE under independent S\n")

    print("--- Rescue: strain-coupled S = f(phi) ---")
    for mean_phi in [0.3, 0.5, 0.7, 0.9]:
        S = strain_from_phi(mean_phi)
        print(f"  mean_phi={mean_phi:.1f}  S_strain={S:.3f}  Pi={pi(E,P,S):.2f}")

    print("\n  Under coupling: higher phi -> lower S -> higher Pi")
    print("  VERDICT: Lemma A' (strain-coupled) PLAUSIBLE\n")

    print("--- Monotone check: coupled sweep ---")
    ok = True
    prev_pi, prev_phi = 0, 0
    for mean_phi in [0.2, 0.35, 0.5, 0.65, 0.8, 0.95]:
        S = strain_from_phi(mean_phi)
        p = pi(E, P, S)
        if prev_pi and p < prev_pi and mean_phi > prev_phi:
            ok = False
        prev_pi, prev_phi = p, mean_phi
        print(f"  phi={mean_phi:.2f}  Pi={p:.2f}")
    print(f"\n  Monotone Pi vs phi (coupled): {'PASS' if ok else 'FAIL'}")

if __name__ == "__main__":
    main()