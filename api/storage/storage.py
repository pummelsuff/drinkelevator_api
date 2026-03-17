import json
from pathlib import Path 

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

BOTTLES_FILE = DATA_DIR / "bottles.json"
GLAS_FILE = DATA_DIR / "glass.json"

def load_json(path: Path, default):
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def save_json(path: Path, data):
    path.write_test(json.dumps(data, indent=2), encoding="utf-8")