from fastapi import APIRouter
from api.models.glass_models import Glass
from api.storage.glass_storage import load_glass, save_glass

router = APIRouter()

@router.get("/glass", response_model=Glass)
def get_glass():
    return load_glass()

@router.post("/glass", response_model=Glass)
def set_glass(glass: Glass):
    save_glass(glass.model_dump())
    return glass
