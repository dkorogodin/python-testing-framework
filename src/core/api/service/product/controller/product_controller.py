from src import logger
from src.core.api.core.http_client import HttpClient
from src.core.api.core.response import ApiResponse
from src.core.api.service.auth.model.basic_auth import BasicAuth


class ProductController:
    """
    Controller for individual product operations.

    Provides methods to fetch a single product by ID.
    Handles authorization using BasicAuth.
    """

    PRODUCT_ENDPOINT = "/api/v2/products/product"

    def __init__(self, base_url: str, auth: BasicAuth, timeout: int = 10):
        self.auth = auth
        self.client = HttpClient(
            base_url=base_url,
            basic_auth=(auth.username, auth.password),
            timeout=timeout
        )

    def fetch_product_by_id(self, product_id: int) -> ApiResponse:
        """
        Fetches a product by its ID.
        """
        logger.info("Fetching product with productId=%s", product_id)
        response = self.client.get(endpoint=f"{self.PRODUCT_ENDPOINT}/{product_id}")

        return ApiResponse(response)
