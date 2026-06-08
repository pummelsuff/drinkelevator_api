from fastapi import APIRouter
import requests

router = APIRouter(prefix="/lift", tags=["Lift"])

# IP des ESP32 – bitte anpassen falls nötig
ESP_IP = "http://192.168.178.70"


@router.post("/up")
def lift_up():
    try:
        r = requests.post(f"{ESP_IP}/lift/up", timeout=1)
        return r.json()
    except Exception as e:
        return {"error": "ESP unreachable", "details": str(e)}


@router.post("/down")
def lift_down():
    try:
        r = requests.post(f"{ESP_IP}/lift/down", timeout=1)
        return r.json()
    except Exception as e:
        return {"error": "ESP unreachable", "details": str(e)}


@router.post("/stop")
def lift_stop():
    try:
        r = requests.post(f"{ESP_IP}/lift/stop", timeout=1)
        return r.json()
    except Exception as e:
        return {"error": "ESP unreachable", "details": str(e)}


@router.get("/status")
def lift_status():
    """
    Holt den echten Status vom ESP:
    {
      "state": "IDLE",
      "glass_present": true/false
    }
    """
    try:
        r = requests.get(f"{ESP_IP}/lift/status", timeout=1)
        data = r.json()

        return {
            "state": data.get("state", "UNKNOWN"),
            "glass_present": data.get("glass_present", False)
        }

    except Exception as e:
        print("ESP unreachable:", e)
        return {
            "state": "ERROR",
            "glass_present": False
        }
