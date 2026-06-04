import requests

ESP_BASE = "http://192.168.178.70"

class ValveService:

    @staticmethod
    def open(valve_id: str):
        try:
            r = requests.post(f"{ESP_BASE}/valve/open?id={valve_id}", timeout=2)
            return r.json()
        except:
            return {"error": "esp_unreachable"}

    @staticmethod
    def close(valve_id: str):
        try:
            r = requests.post(f"{ESP_BASE}/valve/close?id={valve_id}", timeout=2)
            return r.json()
        except:
            return {"error": "esp_unreachable"}

    @staticmethod
    def close_all():
        try:
            r = requests.post(f"{ESP_BASE}/valve/close_all", timeout=2)
            return r.json()
        except:
            return {"error": "esp_unreachable"}
