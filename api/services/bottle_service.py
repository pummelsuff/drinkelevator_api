import json
from pathlib import Path

BOTTLES_FILE = Path("data/bottles.json")
GLASS_FILE = Path("data/glass.json")


class BottleService:

    @staticmethod
    def load_bottles():
        if not BOTTLES_FILE.exists():
            return []
        with open(BOTTLES_FILE, "r") as f:
            return json.load(f)

    @staticmethod
    def save_bottles(bottles):
        with open(BOTTLES_FILE, "w") as f:
            json.dump(bottles, f, indent=2)

    @staticmethod
    def load_glass():
        if not GLASS_FILE.exists():
            return {"size": 300, "empty_weight": 150}
        with open(GLASS_FILE, "r") as f:
            return json.load(f)

    @staticmethod
    def percent_to_ml(percent):
        glass = BottleService.load_glass()
        size = glass.get("size", 300)
        return size * (percent / 100.0)

    @staticmethod
    def update_after_mix(ingredients):
        bottles = BottleService.load_bottles()

        for bottle in bottles:
            bid = bottle["id"]
            if bid in ingredients:
                percent = ingredients[bid]
                used_ml = BottleService.percent_to_ml(percent)
                bottle["level"] = max(bottle["level"] - used_ml, 0)

        BottleService.save_bottles(bottles)
