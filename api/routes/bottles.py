from fastapi import APIRouter
from typing import List
from api.models.bottle_models import Bottle
from api.storage.bottle_storage import load_bottles, save_bottles

router = APIRouter()

@router.get("/bottles", response_model=List[Bottle])
def get_bottles():
    return load_bottles()

@router.post("/bottles")
def save_bottle(bottle: Bottle):
    bottles = load_bottles()

    # Bottle ersetzen oder hinzufügen
    updated = False
    for i, b in enumerate(bottles):
        if b.id == bottle.id:
            bottles[i] = bottle
            updated = True
            break

    if not updated:
        bottles.append(bottle)

    save_bottles(bottles)
    return {"status": "ok"}
