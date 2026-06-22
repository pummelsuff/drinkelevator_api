from fastapi import APIRouter, HTTPException
from api.models.glass_models import Glass
from api.storage.glass_storage import load_glass, save_glass

router = APIRouter(prefix="/glass", tags=["Glass"])


@router.get("", response_model=Glass)
@router.get("/", response_model=Glass, include_in_schema=False)
def get_glass():
    return load_glass()


@router.post("", response_model=Glass)
@router.post("/", response_model=Glass, include_in_schema=False)
def set_glass(glass: Glass):
    try:
        save_glass(glass.model_dump())
        return glass
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
