from typing import List

from src.core.api.core.model.api_response_list import ApiResponseList
from src.core.api.service.product.model.product import Product


class ProductsResponseBody(ApiResponseList):
    """Response body for multiple products."""

    @staticmethod
    def expected_body_for_get_request(expected_products: List[Product]) -> "ProductsResponseBody":
        return ProductsResponseBody(
            data=expected_products or [],
            count=len(expected_products) if expected_products else 0,
            message="All Products fetched successfully."
        )
