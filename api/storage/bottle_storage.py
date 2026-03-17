import json
from pathlib import Path

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

BOTTLES_FILE = DATA_DIR / "bottles.json"

def load_bottles():
    if not BOTTLES_FILE.exists():
        return []
    try:
        return json.loads(BOTTLES_FILE.read_text(encoding="utf-8"))
    except Exception:
        return []

def save_bottles(bottles):
    BOTTLES_FILE.write_text(json.dumps(bottles, indent=2), encoding="utf-8")
