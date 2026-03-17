from fastapi import APIRouter
from api.services.process_service import ProcessService

router = APIRouter()
process = ProcessService()

@router.post("/prepare")
def prepare():
    return process.prepare()

@router.post("/start_mix")
def start_mix():
    return process.start_mix()

@router.post("/finish")
def finish():
    return process.finish()

@router.get("/status")
def status():
    return process.status()

@router.post("/reset")
def reset():
    return process.reset()
