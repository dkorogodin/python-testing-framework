from datetime import datetime
from typing import List

from src import logger
from src.core.api.service.payment.model.credit_card import CreditCard
from src.core.api.service.payment.model.payment import Payment
from src.core.api.service.payment.model.shipping_info import ShippingInfo
from src.core.data.factory.common.data_list import DataList


class PaymentsConstantDataBuilder(DataList):
    """
    Provides static Payment data for deterministic testing.
    """

    def __init__(self):
        self._payments = [
            self._build_payment(1, "5203013923806946", "946", "2028-11-12"),
            self._build_payment(2, "5203013923806888", "888", "2028-12-01")
        ]

    def get_all(self) -> List[Payment]:
        logger.info(f"Returning '{len(self._payments)}' static payments from constants.")
        return self._payments

    def _build_payment(self, id: int, number: str, cvv: str, expiry_date: str) -> Payment:
        date = datetime.strptime(expiry_date, "%Y-%m-%d")

        return Payment(
            id=id,
            credit_card=CreditCard(
                number=number,
                expiry_date=date,
                cvv=cvv,
                name_on_card=f"Tester_{cvv}"
            ),
            coupon="",
            shipping_info=ShippingInfo(
                email=f"tester_aqa_{cvv}@mail.com",
                country="United Kingdom"
            )
        )
