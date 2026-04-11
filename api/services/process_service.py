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

        # Prozess-State (Mix-Logik)
        self.state = "idle"

        # Lift-State (Mechanik)
        self.lift_state = "UNKNOWN"

        self.current_thread = None

    # ------------------------------------------------------------
    # STATE MACHINE HELPERS
    # ------------------------------------------------------------
    def _set_state(self, new_state):
        allowed = {
            "idle": ["prepare", "mixing", "error"],
            "prepare": ["mixing", "error"],
            "mixing": ["done", "error"],
            "done": ["idle", "prepare"],
            "error": ["idle", "prepare"]
        }

        if new_state in allowed.get(self.state, []):
            print(f"STATE: {self.state} → {new_state}")
            self.state = new_state
        else:
            print(f"INVALID STATE TRANSITION: {self.state} → {new_state}")
            self.state = "error"

    # ------------------------------------------------------------
    # PREPARE
    # ------------------------------------------------------------
    def prepare(self):
        # Nur verbieten, wenn gerade aktiv gemischt wird
        if self.state == "mixing":
            return {"status": "error", "error": "already_mixing"}

        if not self.safety.door_closed():
            self._set_state("error")
            return {"status": "error", "error": "door_open"}

        if not self.safety.glass_present():
            self._set_state("error")
            return {"status": "error", "error": "no_glass"}

        if not self.safety.weight_ok():
            self._set_state("error")
            return {"status": "error", "error": "glass_not_empty"}

        self._set_state("prepare")
        return {"status": "prepare"}

    # ------------------------------------------------------------
    # START MIX
    # ------------------------------------------------------------
    def start_mix(self):
        # Toleranter: auch aus idle starten, falls prepare-Race
        if self.state not in ["prepare", "idle"]:
            return {"status": "error", "error": "not_ready"}

        # kleine Verzögerung, damit "prepare" sichtbar bleibt
        time.sleep(0.3)

        self._set_state("mixing")

        self.current_thread = threading.Thread(target=self._simulate_mix)
        self.current_thread.start()

        return {"status": "mixing"}

    # ------------------------------------------------------------
    # SIMULATION
    # ------------------------------------------------------------
    def _simulate_mix(self):
        try:
            # Lift runter
            self.lift_state = "MOVING_DOWN"
            time.sleep(1.5)
            self.lift_state = "AT_BOTTOM"

            # Zutaten simulieren
            for i in range(3):
                time.sleep(1.0)

            # Lift hoch
            self.lift_state = "MOVING_UP"
            time.sleep(1.5)
            self.lift_state = "AT_TOP"

            self._set_state("done")

            # WICHTIG: nicht automatisch zurück auf idle,
            # UI soll "Fertig!" sehen und dann ggf. resetten
        except Exception as e:
            print("Simulation error:", e)
            self._set_state("error")

    # ------------------------------------------------------------
    # STATUS
    # ------------------------------------------------------------
    def status(self):
        try:
            esp_status = self.esp.get_status()

            if esp_status:
                self.lift_state = esp_status.get("state", self.lift_state)
                glass_present = esp_status.get("glass_present", None)
            else:
                glass_present = None

        except Exception as e:
            print("ESP error:", e)
            glass_present = None

        return {
            "status": self.state,
            "lift_state": self.lift_state,
            "glass_present": glass_present
        }

    # ------------------------------------------------------------
    # RESET
    # ------------------------------------------------------------
    def reset(self):
        self._set_state("idle")
        return {"status": "idle"}
