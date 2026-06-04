import requests

ESP_BASE = "http://192.168.178.70"   # später in config.json

class LedService:

    @staticmethod
    def on():
        try:
            r = requests.post(f"{ESP_BASE}/led/on", timeout=2)
            return r.json()
        except Exception:
            return {"error": "esp_unreachable"}

    @staticmethod
    def off():
        try:
            r = requests.post(f"{ESP_BASE}/led/off", timeout=2)
            return r.json()
        except Exception:
            return {"error": "esp_unreachable"}

    @staticmethod
    def set_color(hex_color: str):
        try:
            r = requests.post(f"{ESP_BASE}/led/color?hex={hex_color}", timeout=2)
            return r.json()
        except Exception:
            return {"error": "esp_unreachable"}

    @staticmethod
    def blink(times: int = 3, color: str = "FFFFFF"):
        """Optional: LED blinkt für Feedback."""
        for _ in range(times):
            LedService.set_color(color)
            time.sleep(0.2)
            LedService.off()
            time.sleep(0.2)
        return {"ok": True}
