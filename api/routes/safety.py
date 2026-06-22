from fastapi import APIRouter

from api.services.lift_service import LiftService

router = APIRouter(tags=["Safety"])


@router.get("/safety/check_glass")
def check_glass():
    status = LiftService.status()
    if status.get("state") == "ERROR":
        return {"status": "error", "glass_present": False}

    return {
        "status": "ok",
        "glass_present": status.get("glass_present", False),
    }
