from api.storage.glass_storage import load_glass, save_glass
from api.storage.safety_storage import check_glass_status

class GlassService:

    @staticmethod
    def get():
        """Gibt die gespeicherten Glasdaten zurück."""
        return load_glass()

    @staticmethod
    def set(glass: dict):
        """Speichert neue Glasdaten."""
        save_glass(glass)
        return {"ok": True}

    @staticmethod
    def is_present():
        """Fragt den ESP über safety_storage ab."""
        status = check_glass_status()
        return status.get("glass_present", False)
