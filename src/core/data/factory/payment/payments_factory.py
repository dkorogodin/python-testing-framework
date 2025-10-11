import random
from typing import List, Optional

from src import logger
from src.core.api.service.payment.model.payment import Payment
from src.core.data.factory.common.data_list import DataList


class PaymentsFactory:
    """
    Provides utility methods for retrieving Payment data
    from any data source (API, constants, database).
    """

    @staticmethod
    def get_all(payments_data: DataList) -> List[Payment]:
        all_payments = payments_data.get_all() or []
        logger.info(f"Fetched '{len(all_payments)}' payments from PaymentsFactory.")
        return all_payments

    @staticmethod
    def get_random(payments_data: DataList) -> Optional[Payment]:
        all_payments = PaymentsFactory.get_all(payments_data)

        if not all_payments:
            logger.warning("No payments available in the data source.")
            return None

        payment = random.choice(all_payments)
        logger.info(f"Fetched random payment from PaymentsFactory: '{payment}'.")
        return payment
