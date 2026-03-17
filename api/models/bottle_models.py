from pydantic import BaseModel

class Bottle(BaseModel):
    id: int
    name: str
    level: float  # Liter
