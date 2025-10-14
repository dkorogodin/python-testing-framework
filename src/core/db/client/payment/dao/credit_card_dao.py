from typing import List

from sqlalchemy.orm import Session

from src import logger
from src.core.db.client.payment.entity.credit_card_entity import CreditCardEntity
from src.core.db.core.base_dao import BaseDao


class CreditCardDao(BaseDao[CreditCardEntity]):
    def __init__(self, session: Session):
        super().__init__(session, CreditCardEntity)

    def get(self, id_: int) -> CreditCardEntity:
        logger.info("Database 'paymentdb': 'CreditCard' table: Get CreditCard by ID.")
        return super().get(id_)

    def get_all(self) -> List[CreditCardEntity]:
        logger.info("Database 'productdb': 'CreditCard' table: Get all CreditCards.")
        return super().get_all()

    def save(self, entity: CreditCardEntity):
        logger.info("Saving new CreditCard '%s'.", entity)
        super().save(entity)

    def delete(self, entity: CreditCardEntity):
        logger.info("Deleting CreditCard '%s'.", entity)
        super().delete(entity)
