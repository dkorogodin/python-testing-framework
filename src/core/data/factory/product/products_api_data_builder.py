from src import logger
from src.core.api.service.product.body_content.response.products_response_body import ProductsResponseBody
from src.core.api.service.product.model.product import Product
from src.core.api.service.product.product_service import ProductService
from src.core.data.factory.common.data_list import DataList


class ProductsApiDataBuilder(DataList):
    """
    Builds Product data by fetching it from the product API.
    """

    def __init__(self, product_service: ProductService):
        self.product_service = product_service

    def get_all(self) -> list[Product]:
        product_service = self.product_service.fetch_all_products()
        raw_body = product_service.response.get_json()
        body = ProductsResponseBody(**raw_body)

        if not body or not body.data:
            logger.warning("No products returned from API.")
            return []

        logger.info(f"Fetched '{len(body.data)}' products from API.")
        return [Product(**item) for item in body.data]
