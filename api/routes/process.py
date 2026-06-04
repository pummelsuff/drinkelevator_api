from fastapi import APIRouter
from api.services.process_service import ProcessService

router = APIRouter(prefix="/mix", tags=["Mix"])

@router.post("/prepare")
def prepare():
    return ProcessService.prepare()

@router.post("/start")
def start_mix(request: dict):
    return ProcessService.start_mix(request.get("ingredients", {}))

@router.post("/stop")
def stop_mix():
    return ProcessService.stop_mix()

@router.get("/status")
def get_status():
    return ProcessService.status()
