from fastapi import APIRouter
from api.storage.safety_storage import check_glass_status

router = APIRouter()

@router.get("/safety/check_glass")
def check_glass():
    return check_glass_status()
