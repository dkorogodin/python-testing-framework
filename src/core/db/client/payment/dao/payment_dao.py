from typing import List

from sqlalchemy.orm import Session

from src import logger
from src.core.db.client.payment.entity.payment_entity import PaymentEntity
from src.core.db.core.base_dao import BaseDao


class PaymentDao(BaseDao[PaymentEntity]):
    def __init__(self, session: Session):
        super().__init__(session, PaymentEntity)

    def get(self, id_: int) -> PaymentEntity:
        logger.info("Database 'paymentdb': 'Payment' table: Get Payment by ID.")
        return super().get(id_)

    def get_all(self) -> List[PaymentEntity]:
        logger.info("Database 'productdb': 'Payment' table: Get all Payments.")
        return super().get_all()

    def save(self, entity: PaymentEntity):
        logger.info("Saving new Payment '%s'.", entity)
        super().save(entity)

    def delete(self, entity: PaymentEntity):
        logger.info("Deleting Payment '%s'.", entity)
        super().delete(entity)
