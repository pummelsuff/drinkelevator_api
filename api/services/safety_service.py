class SafetyService:
    @staticmethod
    def door_closed():
        return True  # Simulation

    @staticmethod
    def glass_present():
        return True  # Simulation

    @staticmethod
    def weight_ok():
        return True  # Simulation

    @staticmethod
    def door_status():
        return {"door_closed": True}
