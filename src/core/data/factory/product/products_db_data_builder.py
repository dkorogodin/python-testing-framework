from src import logger
from src.core.api.service.product.model.product import Product
from src.core.data.factory.common.data_list import DataList
from src.core.db.client.product.productdb_client import ProductdbClient


class ProductsDbDataBuilder(DataList):
    """
    Builds Product data by fetching it from the Product DB.
    """

    def __init__(self, db_client: ProductdbClient):
        self.db_client = db_client

    def get_all(self) -> list[Product]:
        products = self.db_client.get_all_products()
        logger.info(f"Fetched '{len(products)}' Product from DB.")
        return products
