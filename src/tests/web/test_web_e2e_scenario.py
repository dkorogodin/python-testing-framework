import allure
import pytest

from src.core.data.factory.payment.payments_api_data_builder import PaymentsApiDataBuilder
from src.core.data.factory.payment.payments_constant_data_builder import PaymentsConstantDataBuilder
from src.core.data.factory.payment.payments_db_data_builder import PaymentsDbDataBuilder
from src.core.data.factory.payment.payments_factory import PaymentsFactory
from src.core.data.factory.product.products_api_data_builder import ProductsApiDataBuilder
from src.core.data.factory.product.products_constant_data_builder import ProductsConstantDataBuilder
from src.core.data.factory.product.products_db_data_builder import ProductsDbDataBuilder
from src.core.data.factory.product.products_factory import ProductsFactory
from src.core.db.client.payment.paymentdb_client import PaymentdbClient
from src.core.db.client.product.productdb_client import ProductdbClient
from src.core.web.assertions.home_page_assertions import HomePageAssertions


@pytest.mark.web
@pytest.mark.smoke
@pytest.mark.positive
@allure.feature("TMS_TEST_ID-1000")
@allure.description("PRODUCT_ORDER")
class TestWebE2eScenario:

    @pytest.fixture(autouse=True, scope="class")
    def product_db_client(self, product_db_pool):
        return ProductdbClient(product_db_pool.get_available_session())

    @pytest.fixture(autouse=True, scope="class")
    def payment_db_client(self, payment_db_pool):
        return PaymentdbClient(payment_db_pool.get_available_session())

    @pytest.fixture
    def valid_login_data_map(self, api_service_manager, payment_db_client, product_db_client):
        return {
            "constant_data": (
                ProductsFactory.get_random(ProductsConstantDataBuilder()),
                PaymentsFactory.get_random(PaymentsConstantDataBuilder())
            ),
            "api_data": (
                ProductsFactory.get_random(ProductsApiDataBuilder(api_service_manager.get_product_service())),
                PaymentsFactory.get_random(PaymentsApiDataBuilder(api_service_manager.get_payment_service()))
            ),
            "db_data": (
                ProductsFactory.get_random(ProductsDbDataBuilder(product_db_client)),
                PaymentsFactory.get_random(PaymentsDbDataBuilder(payment_db_client))
            )
        }

    @allure.description("E2E Scenario: Verify buying random product.")
    @pytest.mark.parametrize("data_type", ["constant_data", "api_data", "db_data"])
    def test_buy_products(self, data_type, valid_login_data_map, home_page):
        product, payment = valid_login_data_map[data_type]
        allure.dynamic.title(f"Buy product flow [{data_type}]")

        # Add product and verify toast
        (home_page
         .add_product_to_cart(product)
         .assert_that()
         .shows_toast_msg(HomePageAssertions.PRODUCT_ADDED_TO_CART_MSG))

        # Go to Cart and verify product
        cart_page = home_page.goto_top_navigation_bar().goto_cart_page()
        cart_page.assert_that().has_added_product(product)

        # Fill payment
        payment_page = cart_page.checkout()
        payment_page.fill_in_all_payment_details(payment)

        # Place order and go to Orders History
        order_confirmation_page = payment_page.place_order()
        order_confirmation_page.goto_orders_history_page()
