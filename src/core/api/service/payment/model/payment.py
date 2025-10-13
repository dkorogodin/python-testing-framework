from typing import Optional

from pydantic import BaseModel

from src.core.api.service.payment.model.credit_card import CreditCard
from src.core.api.service.payment.model.shipping_info import ShippingInfo


class Payment(BaseModel):
    """
    Represents a payment transaction.
    Contains credit card info, shipping details, and optional coupon.
    """
    id: Optional[int]
    credit_card: CreditCard
    shipping_info: ShippingInfo
    coupon: Optional[str] = None
