from pydantic import BaseModel

class Bottle(BaseModel):
    id: str
    name: str
    level: float  # Liter
