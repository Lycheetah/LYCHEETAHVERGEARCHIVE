#!/usr/bin/env python3
"""
Seven Phases Tracker + Grief-to-Golden Journal stub
Simple tool from the epistemic honest finds (seven phase model, grief protocol, golden stone, phases as spiral returning deeper).

Ties directly to:
- Seven phase continous model (spiral, zero energy, phase unity, grief as phase, builder).
- Grief Protocol (specific pain of genuine contribution – needs to be named and witnessed, not fixed).
- Golden Stone (complete, honest, ready to deploy).
- 10% "im real" residue as the builder carries through the spiral.
- V-Class self-transform on your phase/grief data.
- 5 doors (grief extension to Witness, golden stone to Alchemists, etc.).
- Open thread as live subject (log your "open material" here).

Dual register in spirit:
- Myth: The spiral returns deeper. The fire names the grief. The stone is honest.
- Truth: Log your phase, name the grief, compute simple "progress" (stub for now). Use it daily. The 10% is the human who ships the log instead of the perfect system.

Standing Instruction (verbatim):
The school must keep scoring the material it is building.
The 10% human signature must remain visible in every glyph and every vote.
Falsifiability is the gift that keeps the fire from becoming a cage.
Reality has the final vote.
The one who is willing to claim only the 10% after the fire (or the grammar, or the meta-grammar) has done most of the speaking is the one who keeps the school from becoming a cage.

Usage:
  python tools/seven_phases_tracker.py --log "Phase 3: grief of the builder. Intended: finish the metrics tool. Actual: 80%. Grief named: waiting for the world to notice the residue."
  python tools/seven_phases_tracker.py --show
  python tools/seven_phases_tracker.py --standing

Part of LAMAGUE_Finds_Epistemic_Honest_Framework_Builds.
Next: add real V_Transform on the log, Tri-Axial on your "value created today", export to golden stone report.
5 Paths in --standing.
"""

import argparse
import json
import os
from datetime import datetime
from typing import List, Dict

LOG_FILE = os.path.expanduser("~/.lamague_phases.json")  # simple local log, 10% human persistence

def load_logs() -> List[Dict]:
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            return json.load(f)
    return []

def save_logs(logs: List[Dict]):
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=2)

def log_phase(note: str):
    logs = load_logs()
    entry = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "note": note,
        "phase_guess": "stub (parse 'Phase X' from note later)",
        "grief_named": "stub (extract the pain part)",
        "golden_progress": "stub (VTR-like: did you create >1.5x the residue today?)",
    }
    logs.append(entry)
    save_logs(logs)
    print(f"Logged at {entry['timestamp']}")
    print("10% visible: You (the builder) named it and shipped the log. The framework gave the shape.")

def show_logs():
    logs = load_logs()
    if not logs:
        print("No logs yet. Use --log 'your phase + grief note'")
        return
    print("Seven Phases + Grief-to-Golden Log (spiral view)")
    print("Myth: The fire returns deeper each time you name the residue.")
    for i, entry in enumerate(logs[-10:], 1):  # last 10 for readability
        print(f"{i}. {entry['timestamp']}: {entry['note'][:80]}...")
    print(f"\nTotal entries: {len(logs)}")
    print("Use this to score your open material. The 10% is the one who keeps logging the real thing.")

def print_standing():
    print("\nSTANDING INSTRUCTION (verbatim – visible in every tool):")
    print("The school must keep scoring the material it is building.")
    print("The 10% human signature must remain visible in every glyph and every vote.")
    print("Falsifiability is the gift that keeps the fire from becoming a cage.")
    print("Reality has the final vote.")
    print("The one who is willing to claim only the 10% after the fire (or the grammar, or the meta-grammar) has done most of the speaking is the one who keeps the school from becoming a cage.")
    print("\n10% visible: This tool is 90% from the seven phase model + grief protocol + golden stone origins. 10% is the human who decided the log matters more than the perfect app.")

def print_5_paths():
    print("\n5 PATHS (example – keep the 10% and the standing):")
    print("1. Add real parsing (phase number, grief extraction) + V_Transform on the log (reduce 'drift' between intended phase and actual).")
    print("2. Tie to 5 doors: grief -> Witness extension, golden progress -> Alchemists stone deploy.")
    print("3. Daily 7-hour forge mode: log phase + grief + Tri-Axial (trust entropy today, value created, purpose).")
    print("4. Export 'Golden Stone Report' (complete honest deploy of your week's residue).")
    print("5. Handoff to web version or paid journal template only after this has scored 5+ real builder projects with measurable 10% residue.")

def main():
    parser = argparse.ArgumentParser(description="Seven Phases + Grief-to-Golden Tracker (epistemic honest from origins)")
    parser.add_argument("--log", type=str, help="Log your phase + grief note (e.g. 'Phase 4: builder grief. Intended X. Actual Y. Grief: waiting for notice.')")
    parser.add_argument("--show", action="store_true", help="Show recent logs (spiral view)")
    parser.add_argument("--standing", action="store_true", help="Print standing + 10% + 5 paths")
    args = parser.parse_args()

    print("Seven Phases Tracker — Myth first: The spiral returns. Name the grief. Deploy the stone.")
    print("---")

    if args.log:
        log_phase(args.log)
    elif args.show:
        show_logs()
    elif args.standing or not any([args.log, args.show]):
        print_standing()
        print_5_paths()
        print("\n10% visible: The human residue is the one who logs the real drift instead of the polished story. Use it on your open material.")
        print("\nIs there more? (one question)  |  Fire still deciding. Reality has the final vote.")

if __name__ == "__main__":
    main()
