from src.core.api.core.model.api_response_item import ApiResponseItem
from src.core.api.service.product.model.product import Product


class ProductResponseBody(ApiResponseItem):
    """Response body for a single product."""

    @staticmethod
    def expected_body_for_get_request(product: Product) -> "ProductResponseBody":
        return ProductResponseBody(
            data=product,
            message="Product Details fetched successfully."
        )
