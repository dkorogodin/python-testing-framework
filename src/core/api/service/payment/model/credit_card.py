from datetime import date

from pydantic import BaseModel


class CreditCard(BaseModel):
    """
    Represents a credit card used for payment processing.
    Contains the card number, expiry date, CVV, and the cardholder's name.
    """
    number: str
    expiry_date: date
    cvv: str
    name_on_card: str

    model_config = {
        "from_attributes": True  # Enables parsing from SQLAlchemy objects
    }
