import requests

class ESPService:
    def __init__(self, ip="192.168.178.70"):
        self.base = f"http://{ip}/hub"

    def get_status(self):
        try:
            r = requests.get(f"{self.base}/status", timeout=2)
            return r.json()
        except Exception as e:
            return {"state": "ERROR", "error": str(e)}

    def command(self, cmd: str):
        try:
            r = requests.post(
                f"{self.base}/command",
                json={"command": cmd},
                timeout=2
            )
            return {"ok": True, "command": cmd}
        except Exception as e:
            return {"ok": False, "error": str(e)}
