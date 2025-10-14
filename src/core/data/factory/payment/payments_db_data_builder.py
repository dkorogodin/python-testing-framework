from src import logger
from src.core.api.service.payment.model.payment import Payment
from src.core.data.factory.common.data_list import DataList
from src.core.db.client.payment.paymentdb_client import PaymentdbClient


class PaymentsDbDataBuilder(DataList):
    """
    Builds Payment data by fetching it from the Payment DB.
    """

    def __init__(self, db_client: PaymentdbClient):
        self.db_client = db_client

    def get_all(self) -> list[Payment]:
        payments = self.db_client.get_all_payments()
        logger.info(f"Fetched '{len(payments)}' Payment from DB.")
        return payments
