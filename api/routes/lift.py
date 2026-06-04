from fastapi import APIRouter
from api.services.lift_service import LiftService

router = APIRouter(prefix="/lift", tags=["Lift"])

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
    return {"state": LiftService.state()}
