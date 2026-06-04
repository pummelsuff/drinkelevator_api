from fastapi import APIRouter

from api.services.process_service import ProcessService
from api.services.lift_service import LiftService
from api.services.safety_service import SafetyService
from api.services.weight_service import WeightService

router = APIRouter(prefix="/status", tags=["Status"])


@router.get("/")
def get_status():
    return {
        "mix_state": ProcessService.state,
        "lift_state": LiftService.state(),
        "glass_present": SafetyService.glass_present(),
        "door_closed": SafetyService.door_closed(),
        "weight_ok": SafetyService.weight_ok(),
        "current_weight": WeightService.get_weight(),
    }
