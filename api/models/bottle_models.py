from pydantic import BaseModel
from typing import Optional

class Bottle(BaseModel):
    id: str
    name: str
    level: float
    capacity: float
    valve_id: Optional[str] = None
