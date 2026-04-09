import threading
import time

from api.services.safety_service import SafetyService
from api.services.hydraulic_service import HydraulicService
from api.services.valve_service import ValveService
from api.services.weight_service import WeightService
from api.services.esp_service import ESPService



class ProcessService:
    def __init__(self):
        self.safety = SafetyService()
        self.hydraulic = HydraulicService()
        self.valves = ValveService()
        self.weight = WeightService()
        self.esp = ESPService() 
        self.state = "idle"
        self.current_thread = None

    # ------------------------------------------------------------
    # PREPARE
    # ------------------------------------------------------------
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

    # ------------------------------------------------------------
    # START MIX (Simulation)
    # ------------------------------------------------------------
    def start_mix(self):
        if self.state != "prepare":
            self.state = "error"
            return {"status": "error", "error": "not_ready"}

        self.state = "mixing"

        # Simulation in separatem Thread starten
        self.current_thread = threading.Thread(target=self._simulate_mix)
        self.current_thread.start()

        return {"status": "mixing"}

    # ------------------------------------------------------------
    # SIMULATION DES MIXVORGANGS
    # ------------------------------------------------------------
    def _simulate_mix(self):
        try:
            # 1. Hydraulik runter
            time.sleep(1.5)

            # 2. Zutaten simulieren
            #    Jede Zutat dauert 1 Sekunde
            #    (später ersetzt durch echte Ventilsteuerung)
            for i in range(3):  # 3 Zutaten simuliert
                time.sleep(1.0)

            # 3. Hydraulik hoch
            time.sleep(1.5)

            # 4. Fertig
            self.state = "done"

        except Exception as e:
            self.state = "error"
            print("Simulation error:", e)

    # ------------------------------------------------------------
    # FINISH (wird von der Simulation gesetzt)
    # ------------------------------------------------------------
    def finish(self):
        self.state = "done"
        return {"status": "done"}

    # ------------------------------------------------------------
    # STATUS
    # ------------------------------------------------------------
    def status(self):
        try:
            esp_status = self.esp.get_status()

            response = {
                "status": self.state,  # ← Prozesszustand bleibt führend
                "lift_state": None,
                "glass_present": None
            }

            if esp_status:
                response["lift_state"] = esp_status.get("state")
                response["glass_present"] = esp_status.get("glass_present")

            return response

        except Exception as e:
            print("ESP error:", e)
            return {
                "status": self.state,
                "lift_state": None,
                "glass_present": None
            }




    # ------------------------------------------------------------
    # RESET
    # ------------------------------------------------------------
    def reset(self):
        self.state = "idle"
        return {"status": "idle"}
