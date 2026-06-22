from fastapi import FastAPI

from api.routes.bottles import router as bottles_router
from api.routes.glass import router as glass_router
from api.routes.lift import router as lift_router
from api.routes.safety import router as safety_router

app = FastAPI(title="DrinkElevator API")

app.include_router(bottles_router)
app.include_router(glass_router)
app.include_router(lift_router)
app.include_router(safety_router)


@app.get("/")
def root():
    return {"message": "DrinkElevator API running"}
