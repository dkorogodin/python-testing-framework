from http import HTTPStatus

import pytest

from src.core.api.service.product.body_content.response.product_response_body import ProductResponseBody
from src.core.api.service.product.body_content.response.products_response_body import ProductsResponseBody
from src.core.api.service.product.product_service import ProductService
from src.core.data.factory.product.products_constant_data_builder import ProductsConstantDataBuilder
from src.core.data.factory.product.products_factory import ProductsFactory


@pytest.mark.api
@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.product
class TestApiProduct:

    @pytest.fixture
    def product_service(self, api_service_manager) -> ProductService:
        return api_service_manager.get_product_service()

    def test_get_product(self, product_service):
        random_product = ProductsFactory.get_random(ProductsConstantDataBuilder())
        expected_product = ProductResponseBody.expected_body_for_get_request(random_product)

        (product_service
         .fetch_product_by_id(random_product.id)
         .verify_that_response()
         .status_code_is_equal_to(HTTPStatus.OK)
         .body_is_equal_to(expected_product))

    def test_get_all_products(self, product_service):
        expected_products = ProductsResponseBody.expected_body_for_get_request(
            ProductsFactory.get_all(ProductsConstantDataBuilder())
        )

        (product_service
         .fetch_all_products()
         .verify_that_response()
         .status_code_is_equal_to(HTTPStatus.OK)
         .body_is_equal_to(expected_products))
