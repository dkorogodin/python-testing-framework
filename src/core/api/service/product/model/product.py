from typing import Optional

from pydantic import BaseModel


class Product(BaseModel):
    """
    Represents a product in the system.
    Contains product attributes such as name, price, details, and currency.
    """
    id: Optional[int]
    name: str
    price: int
    details: str
    currency: str = "$"
