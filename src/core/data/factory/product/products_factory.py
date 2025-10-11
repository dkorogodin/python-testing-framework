import random
from typing import List, Optional

from src import logger
from src.core.api.service.product.model.product import Product
from src.core.data.factory.common.data_list import DataList


class ProductsFactory:
    """
    Provides utility methods for retrieving Product data
    from any data source (API, constants, database, etc.).
    """

    @staticmethod
    def get_all(products_data: DataList) -> List[Product]:
        all_products = products_data.get_all() or []
        logger.info(f"Fetched '{len(all_products)}' products from ProductsFactory.")
        return all_products

    @staticmethod
    def get_random(products_data: DataList) -> Optional[Product]:
        all_products = ProductsFactory.get_all(products_data)

        if not all_products:
            logger.warning("No products available in the data source.")
            return None

        product = random.choice(all_products)
        logger.info(f"Fetched random product from ProductsFactory: '{product}'.")
        return product
