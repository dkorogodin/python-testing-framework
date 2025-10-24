from src import logger
from src.core.db.client.product.entity.product_entity import ProductEntity
from src.core.db.core.base_dao import BaseDao


class ProductDao(BaseDao[ProductEntity]):
    def __init__(self, session):
        super().__init__(session, ProductEntity)

    def get(self, id_: int) -> ProductEntity:
        logger.info("Database 'productdb': 'Product' table: Get Product by ID.")
        return super().get(id_)

    def get_all(self) -> list[ProductEntity]:
        logger.info("Database 'productdb': 'Product' table: Get all Products.")
        return super().get_all()

    def save(self, entity: ProductEntity):
        logger.info("Saving new Product '%s'.", entity)
        super().save(entity)

    def delete(self, entity: ProductEntity):
        logger.info("Deleting Product '%s'.", entity)
        super().delete(entity)
