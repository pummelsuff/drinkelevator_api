from fastapi import APIRouter, HTTPException
from typing import List
from api.models.bottle_models import Bottle
from api.storage.bottle_storage import load_bottles, save_bottles

router = APIRouter(prefix="/bottles", tags=["Bottles"])


@router.get("", response_model=List[Bottle])
@router.get("/", response_model=List[Bottle], include_in_schema=False)
def get_bottles():
    return load_bottles()


@router.post("")
@router.post("/", include_in_schema=False)
def save_bottle(bottle: Bottle):
    try:
        bottles = load_bottles()

        updated = False
        for i, b in enumerate(bottles):
            if str(b["id"]) == str(bottle.id):
                bottles[i] = bottle.model_dump()
                updated = True
                break

        if not updated:
            bottles.append(bottle.model_dump())

        save_bottles(bottles)
        return {"status": "ok"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
