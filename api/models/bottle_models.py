from pydantic import BaseModel
from typing import Optional

class Bottle(BaseModel):
    id: str
    name: str
    level: float
    capacity: Optional[float] = None
    valve_id: Optional[str] = None
