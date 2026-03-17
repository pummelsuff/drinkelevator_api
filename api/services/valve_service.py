class ValveService:
    def open(self, vid: int):
        return {"valve": vid, "state": "open"}

    def close(self, vid: int):
        return {"valve": vid, "state": "closed"}
