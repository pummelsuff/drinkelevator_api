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
            self.state = "error"
            return {"status": "error", "error": "door_open"}

        if not self.safety.glass_present():
            self.state = "error"
            return {"status": "error", "error": "no_glass"}

        if not self.safety.weight_ok():
            self.state = "error"
            return {"status": "error", "error": "glass_not_empty"}

        self.state = "prepare"
        return {"status": "prepare"}

    def start_mix(self):
        if self.state != "prepare":
            self.state = "error"
            return {"status": "error", "error": "not_ready"}

        self.hydraulic.down()
        self.state = "mixing"
        return {"status": "mixing"}

    def finish(self):
        self.hydraulic.up()
        self.state = "done"
        return {"status": "done"}

    def status(self):
        return {"status": self.state}

    def reset(self):
        self.state = "idle"
        return {"status": "idle"}
