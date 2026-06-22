from fastapi import APIRouter, Query

from api.services.lift_service import LiftService

router = APIRouter(prefix="/lift", tags=["Lift"])


@router.post("/start")
def lift_start(volume: float = Query(0.2, ge=0.01, le=1.0)):
    """Startet den Mix-Ablauf am ESP. volume in Liter (z. B. 0.2 = 200 ml)."""
    return LiftService.start(volume)


@router.post("/up")
def lift_up():
    return LiftService.up()


@router.post("/down")
def lift_down():
    return LiftService.down()


@router.post("/stop")
def lift_stop():
    return LiftService.stop()


@router.get("/status")
def lift_status():
    return LiftService.status()
