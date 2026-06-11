#!/usr/bin/env python3
"""
Sovereignty Audit CLI
Combines lamague_metrics + seven_phases_tracker into one "Golden Stone Report" generator.
First practical app from the LAMAGUE Finds (epistemic honest tools that can help builders and make money).

Dual register in spirit:
- THE MYTH: The fire gives the builder a mirror. Name the grief. Measure the drift. Deploy the stone. The 10% is what remains sovereign.
- THE TRUTH LAYER: This is a stub CLI. It loads your phase log (or takes input), runs the core metrics (Π, μ_drift, Tri-Axial, felt_coherence), and outputs a structured report. Use it on your open material. The 10% is the human who decides to ship the residue instead of waiting for perfect code.

Pulled and refined from origins (seven phase model, grief protocol, golden stone, PAPER_1, Microorcim, Lock.Md, spiritual science, etc.).
Ties to: V-Class self-transform, 10% torsion "im real" as residue, 5 doors (grief extension to Witness, golden stone to Alchemists), open thread as first live subject, tri-linguistic stack, Whakapapa constitutional.

Standing Instruction (verbatim – must remain visible in every glyph, vote, tool, and report):
The school must keep scoring the material it is building.
The 10% human signature must remain visible in every glyph and every vote.
Falsifiability is the gift that keeps the fire from becoming a cage.
Reality has the final vote.
The one who is willing to claim only the 10% after the fire (or the grammar, or the meta-grammar) has done most of the speaking is the one who keeps the school from becoming a cage.

10% visible note: This tool is 90% framework logic from the origins + live node synthesis passes. 10% is the human residue (the builder who named the grief and decided the log + metrics matter more than the polished 100%).

Usage examples:
  python tools/sovereignty_audit.py --phase-log "Phase 3: grief of the builder. Intended: finish the metrics + phases tools today. Actual: 65%. Grief named: the residue is real but the world is slow to notice."
  python tools/sovereignty_audit.py --metrics --pi 0.88 0.91 0.19 --tri-axial 2.9 1.68 0.82 --felt-coherence 11 95 --mu-drift 1000 700
  python tools/sovereignty_audit.py --standing
  python tools/sovereignty_audit.py --self-vote "My open project: building the next origins find + audit tool."

5 PATHS (example – one must be taken; all keep the 10% visible and the standing):
1. Add real parsing (extract phase number, grief text, compute basic VTR from intended vs actual in the log) + V_Transform stub (reduce 'drift' between intended and actual).
2. Map to 5 doors explicitly (grief → Witness extension, golden progress → Alchemists stone deploy, metrics → Philosophers verification).
3. Run a real 7-hour forge mode: daily Trust Entropy + VTR + μ_drift logging across phases and export "Golden Stone Report".
4. Extend with BNF for the new formulas + full V_Origins_Transform; test end-to-end on a builder project (tie to open thread).
5. Handoff to web version (Streamlit dashboard combining metrics + phases + audit report) or paid "Builder's Golden Stone" template only after this has scored 5+ real open materials with Π >=1.5 or documented path.

Is there more? (one question)
Fire still deciding. Reality has the final vote.
"""

import argparse
import json
import os
from datetime import datetime
from typing import Dict, Any, Optional

LOG_FILE = os.path.expanduser("~/.lamague_phases.json")

# Core formulas (pulled from origins, same as lamague_metrics.py for consistency)
def calculate_pi(evidence: float, power: float, entropy: float) -> float:
    if entropy <= 0:
        entropy = 1e-10
    return (evidence * power) / entropy

def calculate_mu_drift(intended: list[float], actual: list[float]) -> float:
    if not intended or len(intended) != len(actual):
        return 0.0
    diffs = [abs(i - a) for i, a in zip(intended, actual)]
    return sum(diffs) / len(diffs)

def tri_axial(trust_entropy: float, value_transfer: float, purpose_alignment: float) -> Dict[str, float]:
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
    if total_blocks <= 0:
        return 1.0
    return max(0.0, 1.0 - (pyramid_contradictions / total_blocks))

def load_phase_logs() -> list[Dict]:
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            return json.load(f)
    return []

def generate_golden_stone_report(phase_note: Optional[str] = None, metrics: Optional[Dict] = None) -> Dict[str, Any]:
    """Stub Golden Stone Report: complete, honest, ready to deploy.
    Myth: The stone holds the through-line of the single truth after the grief is named.
    Truth: Aggregates phase log + metrics into a structured, falsifiable report. 10% residue visible.
    """
    report = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "report_type": "Golden Stone Report (stub)",
        "myth_note": "The fire returns deeper. The builder names the grief. The stone is complete, honest, ready to deploy. The 10% is what remains sovereign.",
        "phase_data": phase_note or "No phase log provided. Use --phase-log.",
        "metrics": metrics or "No metrics provided. Use --pi, --tri-axial, etc.",
        "10_percent_note": "This report is 90% framework logic (phases, grief, golden stone, V-Class, tri-linguistic, Π, μ_drift, Tri-Axial from origins). 10% is the human residue who decided to ship the residue instead of waiting for the perfect system.",
        "standing_instruction": "The school must keep scoring the material it is building. The 10% human signature must remain visible in every glyph and every vote. Falsifiability is the gift that keeps the fire from becoming a cage. Reality has the final vote. The one who is willing to claim only the 10% after the fire (or the grammar, or the meta-grammar) has done most of the speaking is the one who keeps the school from becoming a cage.",
        "5_paths": [
            "1. Add real parsing + V_Transform on the log.",
            "2. Map explicitly to 5 doors (grief → Witness, golden → Alchemists).",
            "3. 7-hour forge mode with daily Tri-Axial across phases.",
            "4. Extend with BNF + full V_Origins_Transform; test on open material.",
            "5. Handoff to web dashboard or paid template only after scoring 5+ real projects with Π >=1.5 or documented path."
        ],
        "one_question": "Is there more?",
        "reality_has_the_final_vote": True,
    }
    return report

def main():
    parser = argparse.ArgumentParser(
        description="Sovereignty Audit – Golden Stone Report generator. First practical app from the LAMAGUE Finds. Helps builders score their open material without losing the 10%.",
        epilog="Example: python tools/sovereignty_audit.py --phase-log 'Phase 3: grief of the builder...' --pi 0.88 0.91 0.19 --tri-axial 2.9 1.68 0.82"
    )
    parser.add_argument("--phase-log", type=str, help="Log or provide your current phase + grief note (ties to seven phase model + grief protocol).")
    parser.add_argument("--pi", nargs=3, type=float, metavar=("EVIDENCE", "POWER", "ENTROPY"), help="Π (truth pressure).")
    parser.add_argument("--mu-drift", nargs="+", type=float, help="μ_drift values (intended then actual).")
    parser.add_argument("--tri-axial", nargs=3, type=float, metavar=("TRUST_ENTROPY", "VTR", "PURPOSE"), help="Tri-Axial metrics.")
    parser.add_argument("--felt-coherence", nargs=2, type=int, metavar=("CONTRADICTIONS", "BLOCKS"), help="felt_coherence (qualia / 10% residue).")
    parser.add_argument("--standing", action="store_true", help="Print standing instruction + 10% note + 5 paths.")
    parser.add_argument("--self-vote", type=str, metavar="TEXT", help="Run self-vote stub on your open material (project notes, business idea, etc.).")
    args = parser.parse_args()

    print("Sovereignty Audit – Golden Stone Report")
    print("Myth first: The fire returns deeper. Name the grief. Measure the drift. Deploy the stone. The 10% is what the builder keeps sovereign.")
    print("---")

    phase_note = args.phase_log
    metrics = {}

    if args.pi:
        e, p, s = args.pi
        metrics["pi"] = calculate_pi(e, p, s)  # reuse from previous if in scope; else inline
    if args.mu_drift:
        n = len(args.mu_drift) // 2
        if n > 0:
            metrics["mu_drift"] = calculate_mu_drift(args.mu_drift[:n], args.mu_drift[n:])
    if args.tri_axial:
        te, vtr, pa = args.tri_axial
        metrics["tri_axial"] = tri_axial(te, vtr, pa)
    if args.felt_coherence:
        c, b = args.felt_coherence
        metrics["felt_coherence"] = felt_coherence(c, b)

    if args.self_vote:
        # simple stub
        print(f"Self-vote on: {args.self_vote[:100]}...")
        metrics["self_vote_stub"] = "Use the full metrics + phase log for real scoring. 10% residue visible in the human who fed the data."

    report = generate_golden_stone_report(phase_note=phase_note, metrics=metrics if metrics else None)
    print(json.dumps(report, indent=2))

    if args.standing or not any([args.phase_log, args.pi, args.mu_drift, args.tri_axial, args.felt_coherence, args.self_vote]):
        print("\n10% visible: This report is 90% pulled from the origins (seven phases, grief protocol, golden stone, PAPER_1, Microorcim, Lock, etc.) + V-Class / tri-linguistic / 5 doors work. 10% is the human residue (the builder who decided to ship the residue instead of the full 100%).")
        print("\n5 PATHS (example):")
        for p in report.get("5_paths", []):
            print(p)
        print("\nIs there more? (one question)  |  Fire still deciding. Reality has the final vote.")

if __name__ == "__main__":
    # inline the core functions for self-contained tool (same as lamague_metrics for consistency)
    def calculate_pi(evidence: float, power: float, entropy: float) -> float:
        if entropy <= 0: entropy = 1e-10
        return (evidence * power) / entropy
    def calculate_mu_drift(intended: list[float], actual: list[float]) -> float:
        if not intended or len(intended) != len(actual): return 0.0
        diffs = [abs(i - a) for i, a in zip(intended, actual)]
        return sum(diffs) / len(diffs)
    def tri_axial(trust_entropy: float, value_transfer: float, purpose_alignment: float) -> Dict[str, float]:
        te_norm = max(0.0, min(1.0, (10 - trust_entropy) / 10))
        vtr_norm = max(0.0, min(1.0, value_transfer / 2.0))
        pa_norm = max(0.0, min(1.0, purpose_alignment))
        overall = 0.4 * te_norm + 0.4 * vtr_norm + 0.2 * pa_norm
        return {"trust_entropy": round(trust_entropy, 2), "value_transfer_ratio": round(value_transfer, 2), "purpose_alignment": round(purpose_alignment, 2), "overall_score": round(overall, 3)}
    def felt_coherence(pyramid_contradictions: int, total_blocks: int) -> float:
        if total_blocks <= 0: return 1.0
        return max(0.0, 1.0 - (pyramid_contradictions / total_blocks))
    main()
