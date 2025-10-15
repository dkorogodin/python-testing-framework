from typing import Optional

from pydantic import BaseModel


class Product(BaseModel):
    title: str
    price: str
    description: Optional[str] = None
