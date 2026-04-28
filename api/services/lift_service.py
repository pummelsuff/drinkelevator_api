from api.services.esp_service import ESPService

class LiftService:
    def __init__(self):
        self.esp = ESPService()

    def up(self):
        # Motor hochfahren
        return self.esp.command("MOVE_UP")

    def down(self):
        # Motor runterfahren
        return self.esp.command("MOVE_DOWN")

    def stop(self):
        # Sofort stoppen
        return self.esp.command("STOP")

    def reset(self):
        # Fehler zurücksetzen
        return self.esp.command("RESET_ERROR")

    def status(self):
        # Status vom ESP holen
        return self.esp.status()
