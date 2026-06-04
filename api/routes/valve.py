from fastapi import APIRouter
from api.services.valve_service import ValveService

router = APIRouter(prefix="/valve", tags=["Valve"])

@router.post("/open")
def valve_open(id: str):
    return ValveService.open(id)

@router.post("/close")
def valve_close(id: str):
    return ValveService.close(id)

@router.post("/close_all")
def valve_close_all():
    return ValveService.close_all()
