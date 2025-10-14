from src import logger
from src.core.api.service.payment.body_content.response.payments_response_body import PaymentsResponseBody
from src.core.api.service.payment.model.payment import Payment
from src.core.api.service.payment.payment_service import PaymentService
from src.core.data.factory.common.data_list import DataList


class PaymentsApiDataBuilder(DataList):
    """
    Builds Payment data by fetching it from the payment API.
    """

    def __init__(self, payment_service: PaymentService):
        self.payment_service = payment_service

    def get_all(self) -> list[Payment]:
        payment_service = self.payment_service.fetch_all_payments()
        raw_body = payment_service.response.get_json()
        body = PaymentsResponseBody(**raw_body)

        if not body or not body.data:
            logger.warning("No payments returned from API.")
            return []

        logger.info(f"Fetched '{len(body.data)}' payments from API.")
        return [Payment(**item) for item in body.data]
