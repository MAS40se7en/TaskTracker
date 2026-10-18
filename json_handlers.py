import sys
import json
from pathlib import Path
from datetime import datetime

TASKS_FILE = Path("tasks.json")

def load_tasks():
    if not TASKS_FILE.exists():
        save_tasks([])
        return []

    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Error: tasks.json is not valid JSON.")
        sys.exit(1)

def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)

def now():
    return datetime.now().isoformat(timespec="seconds")