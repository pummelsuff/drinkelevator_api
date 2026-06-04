from fastapi import APIRouter
from api.models.glass_models import Glass
from api.storage.glass_storage import load_glass, save_glass

router = APIRouter(prefix="/glass", tags=["Glass"])

@router.get("/", response_model=Glass)
def get_glass():
    return load_glass()

@router.post("/", response_model=Glass)
def set_glass(glass: Glass):
    save_glass(glass.model_dump())
    return glass
