from fastapi import FastAPI
from api.routes import process, drinks, hardware
from api.routes.bottles import router as bottles_router
from api.routes.glass import router as glass_router
from api.routes.safety import router as safety_router

app = FastAPI(title="DrinkElevator API")

# Routen registrieren
app.include_router(bottles_router)
app.include_router(glass_router)
app.include_router(safety_router)
app.include_router(process.router)
app.include_router(drinks.router)
app.include_router(hardware.router)

@app.get("/")
def root():
    return {"status": "DrinkElevator API läuft"}
