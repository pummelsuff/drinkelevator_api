from fastapi import APIRouter
from api.services.lift_service import LiftService
from api.services.valve_service import ValveService
from api.services.weight_service import WeightService
from api.services.safety_service import SafetyService

router = APIRouter()

lift = LiftService()
valves = ValveService()
weight = WeightService()
safety = SafetyService()

@router.post("/lift/down")
def lift_down():
    return lift.down()

@router.post("/lift/up")
def lift_up():
    return lift.up()

@router.post("/valve/open/{vid}")
def valve_open(vid: int):
    return valves.open(vid)

@router.post("/valve/close/{vid}")
def valve_close(vid: int):
    return valves.close(vid)

@router.get("/weight")
def get_weight():
    return weight.read()

@router.get("/door")
def door_status():
    return safety.door_status()
