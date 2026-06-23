from typing import List, Optional

from fastapi import APIRouter
from pydantic import BaseModel, Field

from api.services.lift_service import LiftService

router = APIRouter(prefix="/lift", tags=["Lift"])


class MixIngredient(BaseModel):
    valve_id: str
    volume: float = Field(ge=0.01, le=1.0)


class LiftStartRequest(BaseModel):
    volume: float = Field(ge=0.01, le=1.0)
    ingredients: Optional[List[MixIngredient]] = None


@router.post("/start")
def lift_start(body: LiftStartRequest):
    """Startet den Mix-Ablauf am ESP mit optionalem Zutaten-Ablauf."""
    ingredients = None
    if body.ingredients:
        ingredients = [
            {"valve_id": item.valve_id, "volume": item.volume}
            for item in body.ingredients
        ]
    return LiftService.start(body.volume, ingredients)


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
