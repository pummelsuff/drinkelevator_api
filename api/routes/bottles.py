from fastapi import APIRouter
from typing import List
from api.models.bottle_models import Bottle
from api.storage.bottle_storage import load_bottles, save_bottles

router = APIRouter()

@router.get("/bottles", response_model=List[Bottle])
def get_bottles():
    return load_bottles()

@router.post("/bottles", response_model=List[Bottle])
def set_bottles(bottles: List[Bottle]):
    save_bottles([b.model_dump() for b in bottles])
    return bottles
