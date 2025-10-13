import allure
from selenium.webdriver.common.by import By

from src import logger
from src.core.api.service.product.model.product import Product
from src.core.web.assertions.cart_page_assertions import CartPageAssertions
from src.core.web.pageobject.common.web_base_logged_in_page import WebBaseLoggedInPage
from src.core.web.pageobject.payment_page import PaymentPage


class CartPage(WebBaseLoggedInPage):
    """Page object for the Cart Page of the web application."""
    CHECKOUT_BTN = (By.XPATH, "//button[text()='Checkout']")
    PRODUCTS_LIST = (By.CSS_SELECTOR, ".cart .cartWrap")

    @allure.step("Find '{expected_product}' product.")
    def find_product(self, expected_product: Product) -> Product:
        """
        Finds the given product in the cart.

        :param expected_product: Product to find
        :return: Product object with details (name, price, currency)
        """
        product_elem = next(
            (product for product in self.element_actions.find_elements(self.PRODUCTS_LIST)
             if product.find_element(By.CSS_SELECTOR, "h3").text == expected_product.name),
            None
        )

        if not product_elem:
            raise AssertionError(f"Product not found in cart: {expected_product.name}")

        name = product_elem.find_element(By.CSS_SELECTOR, "h3").text
        full_price = product_elem.find_element(By.CSS_SELECTOR, ".prodTotal p").text

        try:
            currency, price_str = full_price.split(" ")
            price = int(price_str.strip())
        except Exception as e:
            raise ValueError(f"Cannot parse currency and price from: '{full_price}'") from e

        return Product(name=name, price=price, currency=currency.strip())

    @allure.step("Proceed checkout.")
    def checkout(self) -> PaymentPage:
        """Proceeds to the checkout page."""
        logger.info("Proceeding to checkout.")
        self.element_actions.click(self.CHECKOUT_BTN)
        return PaymentPage(self.driver)

    def assert_that(self) -> CartPageAssertions:
        """Returns assertions for the Cart Page."""
        return CartPageAssertions(self)

    def wait_until_page_loaded(self) -> None:
        """Wait until the Cart Page is loaded."""
        self.wait_until.element_visible(self.CHECKOUT_BTN)
