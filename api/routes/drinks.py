from fastapi import APIRouter
from api.storage.drinks_storage import DrinksStorage

router = APIRouter()
storage = DrinksStorage()

@router.get("/drinks")
def get_drinks():
    return storage.load()

@router.post("/add_drink")
def add_drink(name: str, amount: int):
    return storage.add(name, amount)

@router.post("/delete_drink")
def delete_drink(name: str):
    return storage.delete(name)

@router.post("/mix_request")
def mix_request(request: dict):
    return {"message": "Mix Request empfangen", "data": request}
