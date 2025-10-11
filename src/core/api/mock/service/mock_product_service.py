from src.core.api.mock.service.base_mock_service import BaseMockService
from src.core.api.service.auth.model.basic_auth import BasicAuth
from src.core.api.service.product.body_content.response.product_response_body import ProductResponseBody
from src.core.api.service.product.body_content.response.products_response_body import ProductsResponseBody
from src.core.api.service.product.controller.product_controller import ProductController
from src.core.api.service.product.controller.products_controller import ProductsController
from src.core.data.factory.product.products_constant_data_builder import ProductsConstantDataBuilder
from src.core.data.factory.product.products_factory import ProductsFactory


class MockProductService(BaseMockService):
    """Mocks all product endpoints with BasicAuth."""

    def __init__(self, base_url: str, basic_auth: BasicAuth):
        super().__init__(base_url)
        self.basic_auth = basic_auth
        self.all_products = ProductsFactory.get_all(ProductsConstantDataBuilder())

    def stub_all_api(self):
        self._stub_get_all_products()
        self._stub_get_product()

    def _stub_get_all_products(self):
        self._stub_request(
            "GET",
            ProductsController.PRODUCTS_ENDPOINT,
            ProductsResponseBody.expected_body_for_get_request(self.all_products),
            auth_header="Authorization",
            auth_value=self._get_basic_auth_header(self.basic_auth.username, self.basic_auth.password)
        )

    def _stub_get_product(self):
        for product in self.all_products:
            self._stub_request(
                "GET",
                f"{ProductController.PRODUCT_ENDPOINT}/{product.id}",
                ProductResponseBody.expected_body_for_get_request(product),
                auth_header="Authorization",
                auth_value=self._get_basic_auth_header(self.basic_auth.username, self.basic_auth.password)
            )
