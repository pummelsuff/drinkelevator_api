from pydantic import BaseModel

class Glass(BaseModel):  # Liter
    size: float
    empty_weight: float  # Gramm
