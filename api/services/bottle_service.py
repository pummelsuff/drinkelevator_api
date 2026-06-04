from api.storage.bottle_storage import load_bottles, save_bottles

class BottleService:

    @staticmethod
    def get_all():
        """Lädt alle Flaschen aus dem Storage."""
        return load_bottles()

    @staticmethod
    def update(bottle: dict):
        """Aktualisiert eine einzelne Flasche."""
        bottles = load_bottles()
        for b in bottles:
            if b["id"] == bottle["id"]:
                b.update(bottle)
        save_bottles(bottles)
        return {"ok": True}

    @staticmethod
    def update_after_mix(ingredients: dict):
        """
        ingredients = {"valve1": 40, "valve2": 60}
        Prozent → ml → Level reduzieren
        """
        bottles = load_bottles()

        for valve_id, percent in ingredients.items():
            for b in bottles:
                if b["id"] == valve_id:
                    used_ml = BottleService.percent_to_ml(percent)
                    b["level"] = max(b["level"] - used_ml, 0)

        save_bottles(bottles)
        return {"ok": True}

    @staticmethod
    def percent_to_ml(percent: float):
        """Konvertiert Prozent in ml basierend auf Glasgröße."""
        glass = load_glass()
        size_ml = glass.get("size_ml", 300)
        return size_ml * (percent / 100)
