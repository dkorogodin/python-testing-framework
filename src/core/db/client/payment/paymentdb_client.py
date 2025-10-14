from typing import List

from sqlalchemy.orm import Session

from src.core.api.service.payment.model.credit_card import CreditCard
from src.core.api.service.payment.model.payment import Payment
from src.core.api.service.payment.model.shipping_info import ShippingInfo
from src.core.db.client.payment.dao.credit_card_dao import CreditCardDao
from src.core.db.client.payment.dao.payment_dao import PaymentDao
from src.core.db.client.payment.dao.shipping_info_dao import ShippingInfoDao


class PaymentdbClient:
    """
    High-level client for interacting with the Payment database.
    Provides access to DAOs and convenient methods from tables,
    like CreditCard, Payment, and ShippingInfo.
    """

    def __init__(self, session: Session):
        self.session = session
        self.shipping_info_dao = ShippingInfoDao(session)
        self.credit_card_dao = CreditCardDao(session)
        self.payment_dao = PaymentDao(session)

    # ------------------- ShippingInfo -------------------
    def get_all_shipping_info(self) -> List[ShippingInfo]:
        """Fetch all ShippingInfo records."""
        return [shipping_info.to_model() for shipping_info in self.shipping_info_dao.get_all()]

    def get_shipping_info_by_id(self, id_: int) -> ShippingInfo | None:
        """Fetch ShippingInfo by ID."""
        return self.shipping_info_dao.get(id_).to_model()

    # ------------------- CreditCard -------------------
    def get_all_credit_cards(self) -> List[CreditCard]:
        """Fetch all CreditCard records."""
        return [credit_card.to_model() for credit_card in self.credit_card_dao.get_all()]

    def get_credit_card_by_id(self, id_: int) -> CreditCard | None:
        """Fetch CreditCard by ID."""
        return self.credit_card_dao.get(id_).to_model()

    # ------------------- Payment -------------------
    def get_all_payments(self) -> List[Payment]:
        """Fetch all Payment records as Pydantic models."""
        return [payment.to_model() for payment in self.payment_dao.get_all()]

    def get_payment_by_id(self, id_: int) -> Payment | None:
        """Fetch Payment by ID."""
        return self.payment_dao.get(id_).to_model()
