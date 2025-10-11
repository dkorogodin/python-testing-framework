from src import logger
from src.core.api.core.http_client import HttpClient
from src.core.api.core.response import ApiResponse
from src.core.api.service.auth.model.basic_auth import BasicAuth


class ProductsController:
    """
    Controller for operations on multiple products.

    Provides methods to fetch all products.
    Handles authorization using BasicAuth.
    """

    PRODUCTS_ENDPOINT = "/api/v2/products"

    def __init__(self, base_url: str, auth: BasicAuth, timeout: int = 10):
        self.auth = auth
        self.client = HttpClient(
            base_url=base_url,
            basic_auth=(auth.username, auth.password),
            timeout=timeout
        )

    def fetch_all_products(self) -> ApiResponse:
        """
        Fetches all products.
        """
        logger.info("Fetching all products.")
        response = self.client.get(endpoint=self.PRODUCTS_ENDPOINT)
        return ApiResponse(response)
