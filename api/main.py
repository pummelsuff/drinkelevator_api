from contextlib import asynccontextmanager
import socket

from fastapi import FastAPI
from zeroconf import ServiceInfo, Zeroconf

from api.routes.bottles import router as bottles_router
from api.routes.glass import router as glass_router
from api.routes.lift import router as lift_router
from api.routes.safety import router as safety_router

zeroconf: Zeroconf | None = None


def _local_ip() -> str:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    finally:
        s.close()


def _register_mdns() -> None:
    global zeroconf
    ip = _local_ip()
    zeroconf = Zeroconf()
    info = ServiceInfo(
        "_drinkelevator._tcp.local.",
        "DrinkElevator._drinkelevator._tcp.local.",
        addresses=[socket.inet_aton(ip)],
        port=8000,
        properties={"name": "DrinkElevator", "id": "de-local"},
    )
    zeroconf.register_service(info)


def _unregister_mdns() -> None:
    global zeroconf
    if zeroconf is not None:
        zeroconf.unregister_all_services()
        zeroconf.close()
        zeroconf = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        _register_mdns()
    except Exception:
        pass
    yield
    _unregister_mdns()


app = FastAPI(title="DrinkElevator API", redirect_slashes=False, lifespan=lifespan)

app.include_router(bottles_router)
app.include_router(glass_router)
app.include_router(lift_router)
app.include_router(safety_router)


@app.get("/")
def root():
    return {"message": "DrinkElevator API running"}
