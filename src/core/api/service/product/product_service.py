import allure

from src import logger
from src.core.api.core.response import ApiResponse
from src.core.api.core.response_validator import ApiResponseValidator
from src.core.api.service.auth.model.basic_auth import BasicAuth
from src.core.api.service.product.controller.product_controller import ProductController
from src.core.api.service.product.controller.products_controller import ProductsController


class ProductService:
    """
    Service class for interacting with ProductService APIs.

    Provides methods to fetch individual products or all products,
    and wraps responses for validation using ApiResponseValidator.

    Uses ProductController and ProductsController internally
    to perform API calls with BasicAuth authentication.
    """

    def __init__(self, base_url: str, auth: BasicAuth, timeout: int = 10):
        self.auth = auth
        self.response: ApiResponse | None = None
        self.product_controller = ProductController(base_url=base_url, auth=auth, timeout=timeout)
        self.products_controller = ProductsController(base_url=base_url, auth=auth, timeout=timeout)

    @allure.step("Retrieve a specific product by ID '{1}'")
    def fetch_product_by_id(self, product_id: int) -> "ProductService":
        """
        Retrieve a specific product by its ID.
        """
        logger.info("Fetching product by ID: %s", product_id)
        self.response = self.product_controller.fetch_product_by_id(product_id)
        return self

    @allure.step("Retrieve all products")
    def fetch_all_products(self) -> "ProductService":
        """
        Retrieve all products in the system.
        """
        logger.info("Fetching all products.")
        self.response = self.products_controller.fetch_all_products()
        return self

    @allure.step("Validate API response")
    def verify_that_response(self) -> ApiResponseValidator:
        """
        Provides a validator for the last API response.
        """
        if self.response is None:
            raise ValueError("No response available. Call one of the fetch methods first.")
        return ApiResponseValidator(self.response)
