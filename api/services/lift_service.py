import requests
from typing import Any, Dict, Optional

from api.config import ESP_BASE_URL


class LiftService:
    @staticmethod
    def _post(path: str, params: Optional[Dict[str, Any]] = None, timeout: float = 2):
        try:
            r = requests.post(
                f"{ESP_BASE_URL}{path}",
                params=params,
                timeout=timeout,
            )
            if r.status_code != 200:
                return {
                    "error": "esp_error",
                    "status": r.status_code,
                    "details": r.text,
                }
            return r.json()
        except Exception as e:
            return {"error": "esp_unreachable", "details": str(e)}

    @staticmethod
    def start(volume: float):
        return LiftService._post("/lift/start", params={"volume": volume}, timeout=5)

    @staticmethod
    def up():
        return LiftService._post("/lift/up")

    @staticmethod
    def down():
        return LiftService._post("/lift/down")

    @staticmethod
    def stop():
        return LiftService._post("/lift/stop")

    @staticmethod
    def status():
        try:
            r = requests.get(f"{ESP_BASE_URL}/lift/status", timeout=2)
            data = r.json()
            return {
                "state": data.get("state", "UNKNOWN"),
                "glass_present": data.get("glass_present", False),
            }
        except Exception:
            return {"state": "ERROR", "glass_present": False}
