from pydantic import BaseModel


class ShippingInfo(BaseModel):
    """
    Represents shipping information associated with a payment.
    Contains the recipient's email and country.
    """
    email: str
    country: str
