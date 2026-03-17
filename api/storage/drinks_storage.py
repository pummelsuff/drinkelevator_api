import json
from pathlib import Path

DATA_FILE = Path("/home/pi/drinkelevator/data/drinks.json")

class DrinksStorage:
    def load(self):
        if not DATA_FILE.exists():
            return []
        return json.loads(DATA_FILE.read_text())

    def save(self, drinks):
        DATA_FILE.write_text(json.dumps(drinks, indent=4))

    def add(self, name, amount):
        drinks = self.load()
        drinks.append({"name": name, "amount": amount})
        self.save(drinks)
        return drinks

    def delete(self, name):
        drinks = [d for d in self.load() if d["name"] != name]
        self.save(drinks)
        return drinks
