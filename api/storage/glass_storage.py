import json
from pathlib import Path

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

GLASS_FILE = DATA_DIR / "glass.json"

def load_glass():
    if not GLASS_FILE.exists():
        # Default-Werte, falls noch nichts gespeichert wurde
        return {"size": 0.2, "empty_weight": 120}
    try:
        return json.loads(GLASS_FILE.read_text(encoding="utf-8"))
    except Exception:
        return {"size": 0.2, "empty_weight": 120}

def save_glass(glass_data):
    GLASS_FILE.write_text(json.dumps(glass_data, indent=2), encoding="utf-8")
