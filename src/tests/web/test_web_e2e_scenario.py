import allure
import pytest

from src.core.web.assertions.home_page_assertions import HomePageAssertions
from src.core.web.data.dataprovider.valid_login_data_provider import valid_login_data


@pytest.mark.web
@pytest.mark.smoke
@pytest.mark.positive
@allure.feature("TMS_TEST_ID-1000")
@allure.description("PRODUCT_ORDER")
class TestWebE2eScenario:

    @allure.description("E2E Scenario: Verify buying random product.")
    @pytest.mark.parametrize("product,payment", valid_login_data())
    def test_buy_products(self, home_page, product, payment):
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
