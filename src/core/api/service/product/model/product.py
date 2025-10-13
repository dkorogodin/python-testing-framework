from typing import Optional

from pydantic import BaseModel


class Product(BaseModel):
    """
    Represents a product in the system.
    Contains product attributes such as name, price, details, and currency.
    """
    id: Optional[int] = 0
    name: str
    price: int
    details: Optional[str] = None
    currency: str = "$"
