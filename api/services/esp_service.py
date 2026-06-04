# esp_service.py

import requests

class ESPService:
    def __init__(self, ip="192.168.178.70"):
        self.base = f"http://{ip}"

    def status(self):
        try:
            r = requests.get(f"{self.base}/lift/status", timeout=2)
            return r.json()
        except Exception as e:
            return {"state": "ERROR", "error": str(e)}

    def command(self, cmd: str):
        try:
            if cmd in ["MOVE_UP", "MOVE_DOWN"]:
                # ESP kennt nur /lift/start
                r = requests.post(f"{self.base}/lift/start", timeout=2)
                return {"ok": True, "command": cmd}

            # STOP & RESET existieren nicht
            return {"ok": False, "error": "not_supported"}

        except Exception as e:
            return {"ok": False, "error": str(e)}
