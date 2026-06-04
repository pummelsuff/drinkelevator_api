import requests

ESP_BASE = "http://192.168.178.70"   # später in config.json

class LiftService:

    @staticmethod
    def up():
        try:
            r = requests.post(f"{ESP_BASE}/lift/up", timeout=2)
            return r.json()
        except Exception:
            return {"error": "esp_unreachable"}

    @staticmethod
    def down():
        try:
            r = requests.post(f"{ESP_BASE}/lift/down", timeout=2)
            return r.json()
        except Exception:
            return {"error": "esp_unreachable"}

    @staticmethod
    def stop():
        try:
            r = requests.post(f"{ESP_BASE}/lift/stop", timeout=2)
            return r.json()
        except Exception:
            return {"error": "esp_unreachable"}

    @staticmethod
    def state():
        try:
            r = requests.get(f"{ESP_BASE}/lift/status", timeout=2)
            data = r.json()
            return data.get("state", "UNKNOWN")
        except Exception:
            return "ERROR"
