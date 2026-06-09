from fastapi import APIRouter
import time

from api.services.lift_service import LiftService
from api.services.valve_service import ValveService
from api.services.bottle_service import BottleService
from api.services.glass_service import GlassService
from api.services.safety_service import SafetyService

router = APIRouter(prefix="/mix", tags=["Mix"])


class ProcessService:
    state = "idle"          # idle, prepare, mixing, done, error, stopped
    lift_state = "UNKNOWN"  # AT_TOP, MOVING_DOWN, AT_BOTTOM, MOVING_UP

    @staticmethod
    def _set_state(new_state: str):
        allowed = {
            "idle": ["prepare", "mixing", "error"],
            "prepare": ["mixing", "error"],
            "mixing": ["done", "error", "stopped"],
            "done": ["idle", "prepare"],
            "error": ["idle", "prepare"],
            "stopped": ["idle", "prepare"]
        }

        if new_state in allowed.get(ProcessService.state, []):
            print(f"STATE: {ProcessService.state} → {new_state}")
            ProcessService.state = new_state
        else:
            print(f"INVALID STATE TRANSITION: {ProcessService.state} → {new_state}")
            ProcessService.state = "error"

    # ------------------------------------------------------------
    # PREPARE
    # ------------------------------------------------------------
    @staticmethod
    def prepare():
        if ProcessService.state == "mixing":
            return {"status": "error", "error": "already_mixing"}

        # Safety Checks
        if not SafetyService.door_closed():
            ProcessService._set_state("error")
            return {"status": "error", "error": "door_open"}

        if not SafetyService.glass_present():
            ProcessService._set_state("error")
            return {"status": "error", "error": "no_glass"}

        if not SafetyService.weight_ok():
            ProcessService._set_state("error")
            return {"status": "error", "error": "glass_not_empty"}

        ProcessService._set_state("prepare")
        return {"status": "prepare"}

    # ------------------------------------------------------------
    # START MIX
    # ------------------------------------------------------------
    @staticmethod
    def start_mix(ingredients: dict):
        if ProcessService.state not in ["prepare", "idle"]:
            return {"status": "error", "error": "not_ready"}

        # kleine Verzögerung für UI
        time.sleep(0.3)

        ProcessService._set_state("mixing")
    

        # Lift runter
        LiftService.down()
        time.sleep(1.5)
        ProcessService.lift_state = "AT_BOTTOM"

        # Zutaten dosieren
        for valve_id, percent in ingredients.items():
            ValveService.open(valve_id)
            time.sleep(percent / 10)  # Beispielzeit
            ValveService.close(valve_id)

        # Lift hoch
        LiftService.up()
        time.sleep(1.5)
        ProcessService.lift_state = "AT_TOP"

        # Bottle-Level aktualisieren
        BottleService.update_after_mix(ingredients)
        ProcessService._set_state("done")

        return {"status": "done"}

    # ------------------------------------------------------------
    # STOP MIX
    # ------------------------------------------------------------
    @staticmethod
    def stop_mix():
        ValveService.close_all()
        LiftService.stop()
        ProcessService._set_state("stopped")
        return {"status": "stopped"}

    # ------------------------------------------------------------
    # STATUS
    # ------------------------------------------------------------
    @staticmethod
    def status():
        return {
            "status": ProcessService.state,
            "lift_state": ProcessService.lift_state,
            "glass_present": SafetyService.glass_present()
        }


# ------------------------------------------------------------
# ROUTES
# ------------------------------------------------------------
@router.post("/prepare")
def prepare():
    return ProcessService.prepare()


@router.post("/start")
def start_mix(request: dict):
    return ProcessService.start_mix(request.get("ingredients", {}))


@router.post("/stop")
def stop_mix():
    return ProcessService.stop_mix()


@router.get("/status")
def get_status():
    return ProcessService.status()
