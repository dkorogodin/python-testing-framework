from typing import List

from src import logger
from src.core.api.service.product.model.product import Product
from src.core.data.factory.common.data_list import DataList


class ProductsConstantDataBuilder(DataList):
    """
    Provides static Product data for deterministic testing.
    """

    def __init__(self):
        self._products = [
            Product(id=1, name="ADIDAS ORIGINAL", price=11500, details="Adidas shoes for Men"),
            Product(id=2, name="ZARA COAT 3", price=11500, details="Zara coat for Women and girls"),
            Product(id=3, name="IPHONE 13 PRO", price=55000,
                    details="Latest Apple iPhone 13 Pro with 200MP front camera")
        ]

    def get_all(self) -> List[Product]:
        logger.info(f"Returning '{len(self._products)}' static products from constants.")
        return self._products
