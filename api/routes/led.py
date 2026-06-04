from fastapi import APIRouter
from api.services.led_service import LedService

router = APIRouter(prefix="/led", tags=["LED"])

@router.post("/on")
def led_on():
    return LedService.on()

@router.post("/off")
def led_off():
    return LedService.off()

@router.post("/color")
def led_color(hex: str):
    return LedService.set_color(hex)
