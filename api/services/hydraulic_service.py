from api.services.esp_service import ESPService

class HydraulicService:
    def __init__(self):
        self.esp = ESPService()

    def down(self):
        return self.esp.command("MOVE_DOWN")

    def up(self):
        return self.esp.command("MOVE_UP")
