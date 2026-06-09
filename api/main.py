from fastapi import FastAPI

# Routen importieren
from api.routes.bottles import router as bottles_router
from api.routes.glass import router as glass_router
from api.routes.lift import router as lift_router
from api.routes.process import router as process_router
from api.routes.safety import router as safety_router
from api.routes.valve import router as valve_router
# Falls du eine Status-Route hast:
# from api.routes.status import router as status_router

app = FastAPI(title="DrinkElevator API")

# Router registrieren
app.include_router(bottles_router)
app.include_router(glass_router)
app.include_router(lift_router)
app.include_router(process_router)
app.include_router(safety_router)
app.include_router(valve_router)
# app.include_router(status_router)

@app.get("/")
def root():
    return {"message": "DrinkElevator API running"}
