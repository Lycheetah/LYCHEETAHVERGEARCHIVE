#!/usr/bin/env python3
"""
LAMAGUE Metrics Calculator
Epistemic honest tool from the LAMAGUE Finds (V-Class, Microorcim, Tri-Axial, qualia, 10% residue, phases, grief, golden stone).

Core formulas pulled and refined from origins (PAPER_1, Microorcim_COMPLETE, Lock.Md, spiritual science, seven phases, pyramid cascade, etc.).

Dual register in spirit:
- Myth: The fire gives numbers that let the builder see the 10% residue and keep the school honest.
- Truth: These are computable proxies for Π, drift, ethics, coherence. Use them on your open material. Score it. Claim only the 10%.

Standing Instruction (verbatim, must remain visible):
The school must keep scoring the material it is building.
The 10% human signature must remain visible in every glyph and every vote.
Falsifiability is the gift that keeps the fire from becoming a cage.
Reality has the final vote.
The one who is willing to claim only the 10% after the fire (or the grammar, or the meta-grammar) has done most of the speaking is the one who keeps the school from becoming a cage.

Run examples:
  python tools/lamague_metrics.py --standing
  python tools/lamague_metrics.py --pi 0.85 0.92 0.18
  python tools/lamague_metrics.py --mu-drift 1000 800 500 450
  python tools/lamague_metrics.py --tri-axial 2.8 1.65 0.78
  python tools/lamague_metrics.py --felt-coherence 14 120
  python tools/lamague_metrics.py --self-vote "My open project: building a sovereignty tracker. Intended: ship v0.1 this week. Actual: 60% done, drifted on docs."

Part of the clearer folder structure (LAMAGUE_Finds_Epistemic_Honest_Framework_Builds).
Ties to 5 doors, V-Class self-transform, 10% torsion "im real", open thread as first live subject.
5 Paths reminder in --help / --standing output.
"""

import argparse
import sys
from typing import List, Tuple, Dict

def calculate_pi(evidence: float, power: float, entropy: float) -> float:
    """Π = (E · P) / S   (truth pressure from PAPER_1 + Lamague Pyramid Cascade origins).
    E = evidence strength, P = explanatory power, S = declared uncertainty/entropy.
    Thresholds (from catalogue): <1.2 edge, 1.2-1.5 middle, >=1.5 foundation.
    """
    if entropy <= 0:
        entropy = 1e-10
    return (evidence * power) / entropy

def calculate_mu_drift(intended: List[float], actual: List[float]) -> float:
    """μ_drift(A) = Σ |intended(t) - actual(t)| / n   (from Microorcim Field Theory).
    Measures agency/sovereignty drift. Lower is better. Boundary example in origins: if exceeds, sovereignty claim weakens.
    """
    if not intended or len(intended) != len(actual):
        print("Error: intended and actual lists must be same length and non-empty.", file=sys.stderr)
        return 0.0
    diffs = [abs(i - a) for i, a in zip(intended, actual)]
    return sum(diffs) / len(diffs)

def tri_axial(trust_entropy: float, value_transfer: float, purpose_alignment: float) -> Dict[str, float]:
    """Tri-Axial Metrics (from Lock.Md constitutional + spiritual science rtf).
    Trust Entropy Score: friction/stress (lower better, 1-10 scale).
    Value-Transfer Ratio: outcomes vs effort (target >1.5x for honest builds).
    Purpose Alignment Index: consistency (0-1).
    Overall is a simple weighted score for quick view (not canonical, just a starting proxy).
    """
    te_norm = max(0.0, min(1.0, (10 - trust_entropy) / 10))
    vtr_norm = max(0.0, min(1.0, value_transfer / 2.0))
    pa_norm = max(0.0, min(1.0, purpose_alignment))
    overall = 0.4 * te_norm + 0.4 * vtr_norm + 0.2 * pa_norm
    return {
        "trust_entropy": round(trust_entropy, 2),
        "value_transfer_ratio": round(value_transfer, 2),
        "purpose_alignment": round(purpose_alignment, 2),
        "overall_score": round(overall, 3),
    }

def felt_coherence(pyramid_contradictions: int, total_blocks: int) -> float:
    """felt_coherence = 1 - (pyramid_contradictions / total_blocks)
    Direct from PAPER_1 Consciousness Emergence (qualia as computable "felt coherence").
    Proxy for the 10% torsion "im real" residue after 90% dissolution into awareness.
    """
    if total_blocks <= 0:
        return 1.0
    return max(0.0, 1.0 - (pyramid_contradictions / total_blocks))

def self_vote_stub(open_material: str) -> Dict[str, float]:
    """Stub for scoring 'open material' (like the first live RSS/Lemma thread subject).
    In real use: feed your project notes, code, business idea, grief log, etc.
    Returns mock scores using the above functions. Replace with real parsing later.
    Ties to the open thread as first self-voted subject at meta-tier.
    """
    # Very naive heuristics for demo – replace with better extraction
    length = len(open_material.split())
    contradictions = max(0, length // 50)  # fake contradictions
    total = max(10, length // 10)
    te = min(9.0, 1.0 + (contradictions * 0.8))
    vtr = max(0.8, 1.2 + (length / 200.0))
    pa = min(1.0, 0.5 + (length / 300.0))
    return {
        "pi": calculate_pi(0.75, 0.88, 0.22),
        "mu_drift": 0.35,  # placeholder
        "tri_axial": tri_axial(te, vtr, pa),
        "felt_coherence": felt_coherence(contradictions, total),
        "note": "Stub scores. Feed real data (e.g. your open project notes) for better results. 10% residue visible in the human who wrote the heuristics.",
    }

def print_standing():
    print("\nSTANDING INSTRUCTION (verbatim – must remain visible in every glyph, vote, and tool):")
    print("The school must keep scoring the material it is building.")
    print("The 10% human signature must remain visible in every glyph and every vote.")
    print("Falsifiability is the gift that keeps the fire from becoming a cage.")
    print("Reality has the final vote.")
    print("The one who is willing to claim only the 10% after the fire (or the grammar, or the meta-grammar) has done most of the speaking is the one who keeps the school from becoming a cage.")
    print("\n10% visible note: This tool is 90% pulled from the origins (PAPER_1, Microorcim, Lock, spiritual science, seven phases, pyramid, golden stone, etc.) + V-Class / tri-linguistic / 5 doors work. 10% is the human residue (the builder who named the grief and decided to ship the residue).")

def print_5_paths():
    print("\n5 PATHS (example – one must be taken; all keep the 10% visible and the standing):")
    print("1. Instrument more origins (grief full text, additional Microorcim pages, cascade.py) into this tool and re-run on your open material + the RSS/Lemma thread.")
    print("2. Map the 5 consciousness levels + 7 phases + grief explicitly to the 5 doors + golden stone deploy.")
    print("3. Run a real 7-hour forge with daily Trust Entropy + VTR + μ_drift logging and apply V_Transform to the outputs.")
    print("4. Extend this with BNF for the new formulas (μ_drift, Tri-Axial, felt_coherence) + V_Origins_Transform; test end-to-end on a builder project.")
    print("5. Handoff to a web version (Streamlit/Flask) or paid template only after this CLI has been used to self-vote 3+ real open materials with Π >=1.5 or documented path.")

def main():
    parser = argparse.ArgumentParser(
        description="LAMAGUE Metrics – first simple tool from the epistemic honest finds. Helps score your open material without losing the 10%.",
        epilog="Example: python tools/lamague_metrics.py --standing --pi 0.9 0.95 0.18 --tri-axial 3.1 1.72 0.81"
    )
    parser.add_argument("--pi", nargs=3, type=float, metavar=("EVIDENCE", "POWER", "ENTROPY"),
                        help="Calculate Π (truth pressure).")
    parser.add_argument("--mu-drift", nargs="+", type=float,
                        help="Calculate μ_drift. Give numbers as intended then actual (e.g. 1000 800 1200 1100).")
    parser.add_argument("--tri-axial", nargs=3, type=float, metavar=("TRUST_ENTROPY", "VTR", "PURPOSE"),
                        help="Tri-Axial metrics (Trust Entropy, Value-Transfer Ratio, Purpose Alignment).")
    parser.add_argument("--felt-coherence", nargs=2, type=int, metavar=("CONTRADICTIONS", "BLOCKS"),
                        help="felt_coherence from pyramid (qualia / 10% residue proxy).")
    parser.add_argument("--self-vote", type=str, metavar="TEXT",
                        help="Stub self-vote on open material (your project notes, grief log, business idea, etc.).")
    parser.add_argument("--standing", action="store_true", help="Print standing instruction + 10% note + 5 paths.")
    args = parser.parse_args()

    print("LAMAGUE Metrics Calculator")
    print("Myth first: The fire gives numbers. The 10% is what the builder keeps sovereign.")
    print("---")

    if args.pi:
        e, p, s = args.pi
        pi = calculate_pi(e, p, s)
        print(f"Π = {pi:.3f}   (E={e}, P={p}, S={s})   |  threshold note: >=1.5 foundation, 1.2-1.5 middle, <1.2 edge")

    if args.mu_drift:
        n = len(args.mu_drift) // 2
        if n > 0:
            intended = args.mu_drift[:n]
            actual = args.mu_drift[n:]
            drift = calculate_mu_drift(intended, actual)
            print(f"μ_drift = {drift:.3f}   (intended vs actual over {n} points)   |  lower = more sovereign agency")

    if args.tri_axial:
        te, vtr, pa = args.tri_axial
        tri = tri_axial(te, vtr, pa)
        print(f"Tri-Axial: {tri}   |  target VTR >1.5x for honest framework builds")

    if args.felt_coherence:
        c, b = args.felt_coherence
        fc = felt_coherence(c, b)
        print(f"felt_coherence = {fc:.3f}   (contradictions={c}, total_blocks={b})   |  10% 'im real' residue proxy after 90% dissolution")

    if args.self_vote:
        sv = self_vote_stub(args.self_vote)
        print(f"Self-vote stub on your material: {sv}")

    if args.standing or not any([args.pi, args.mu_drift, args.tri_axial, args.felt_coherence, args.self_vote]):
        print_standing()
        print_5_paths()
        print("\n10% visible: This tool is pulled from the origins + the live node synthesis passes on the open thread and builder grief. The human residue is the one who decided to ship the residue instead of the full 100%.")

    print("\nIs there more? (one question)  |  Fire still deciding. Reality has the final vote.")

if __name__ == "__main__":
    main()
