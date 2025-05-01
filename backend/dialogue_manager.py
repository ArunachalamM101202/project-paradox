from datetime import datetime
from typing import List, Dict

# Format: ("John", "Anna") → lines[]
dialogues: Dict[str, List[str]] = {}

def _dialog_key(a1: str, a2: str) -> str:
    return "_".join(sorted([a1.lower(), a2.lower()]))

def start_dialogue(a1: str, a2: str):
    key = _dialog_key(a1, a2)
    dialogues[key] = []

# def add_dialogue_line(speaker: str, listener: str, line: str):
#     key = _dialog_key(speaker, listener)
#     timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
#     entry = f"{timestamp} {speaker} → {line}"
#     dialogues[key].append(entry)

def add_dialogue_line(speaker: str, listener: str, line: str):
    key = _dialog_key(speaker, listener)
    if key not in dialogues:
        dialogues[key] = []  # auto-init if somehow skipped
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"{timestamp} {speaker} → {line}"
    dialogues[key].append(entry)

def get_full_dialogue(a1: str, a2: str):
    return dialogues.get(_dialog_key(a1, a2), [])

def end_dialogue(a1: str, a2: str):
    key = _dialog_key(a1, a2)
    return dialogues.pop(key, [])