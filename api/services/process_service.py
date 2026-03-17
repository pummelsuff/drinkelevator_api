from api.services.safety_service import SafetyService
from api.services.hydraulic_service import HydraulicService
from api.services.valve_service import ValveService
from api.services.weight_service import WeightService

class ProcessService:
    def __init__(self):
        self.safety = SafetyService()
        self.hydraulic = HydraulicService()
        self.valves = ValveService()
        self.weight = WeightService()
        self.state = "idle"

    def prepare(self):
        if not self.safety.door_closed():
            return {"error": "Tür ist offen"}

        if not self.safety.glass_present():
            return {"error": "Kein Glas erkannt"}

        if not self.safety.weight_ok():
            return {"error": "Gewicht außerhalb Toleranz"}

        self.state = "ready"
        return {"status": "bereit"}

    def start_mix(self):
        if self.state != "ready":
            return {"error": "Nicht bereit"}

        self.hydraulic.down()
        self.state = "mixing"
        return {"status": "mixing"}

    def finish(self):
        self.hydraulic.up()
        self.state = "finished"
        return {"status": "finished"}

    def status(self):
        return {"status": self.state}

    def reset(self):
        self.state = "idle"
        return {"status": "reset"}
