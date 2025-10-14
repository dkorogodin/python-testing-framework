from typing import List

from sqlalchemy.orm import Session

from src import logger
from src.core.db.client.payment.entity.shipping_info_entity import ShippingInfoEntity
from src.core.db.core.base_dao import BaseDao


class ShippingInfoDao(BaseDao[ShippingInfoEntity]):
    def __init__(self, session: Session):
        super().__init__(session, ShippingInfoEntity)

    def get(self, id_: int) -> ShippingInfoEntity:
        logger.info("Database 'paymentdb': 'ShippingInfo' table: Get ShippingInfo by ID.")
        return super().get(id_)

    def get_all(self) -> List[ShippingInfoEntity]:
        logger.info("Database 'productdb': 'ShippingInfo' table: Get all ShippingInfos.")
        return super().get_all()

    def save(self, entity: ShippingInfoEntity):
        logger.info("Saving new ShippingInfo '%s'.", entity)
        super().save(entity)

    def delete(self, entity: ShippingInfoEntity):
        logger.info("Deleting ShippingInfo '%s'.", entity)
        super().delete(entity)
