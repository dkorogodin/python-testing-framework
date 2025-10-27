import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from src import logger
from src.core.api.service.product.model.product import Product
from src.core.web.assertions.home_page_assertions import HomePageAssertions
from src.core.web.pageobject.common.web_base_logged_in_page import WebBaseLoggedInPage


class HomePage(WebBaseLoggedInPage):
    """Page object for the Home Page."""
    PRODUCTS_LIST_LOC = (By.CSS_SELECTOR, ".card .card-body")
    PRODUCT_ADD_TO_CART_BTN_LOC = (By.XPATH, ".//button[text()=' Add To Cart']")
    PRODUCT_NAME_LOC = (By.CSS_SELECTOR, "b")
    SPINNER_LOC = (By.CLASS_NAME, "ngx-spinner-overlay")

    @allure.step("Add '{1}' product to cart.")
    def add_product_to_cart(self, product: Product) -> "HomePage":
        """
        Adds a product to the cart.

        :param product: Product object to add
        :return: HomePage instance (fluent API)
        """
        logger.info(f"Add '{product.name}' product to cart.")
        product_elem = self._find_product(product.name)
        add_btn = product_elem.find_element(*self.PRODUCT_ADD_TO_CART_BTN_LOC)
        add_btn.click()

        # Wait for spinner to appear and disappear
        self.wait_until.element_visible(self.SPINNER_LOC)
        self.wait_until.element_invisible(self.SPINNER_LOC)
        return self

    def assert_that(self) -> HomePageAssertions:
        """Return HomePageAssertions instance for fluent assertions."""
        return HomePageAssertions(self)

    def wait_until_page_loaded(self):
        self.wait_until.element_visible(self.PRODUCTS_LIST_LOC)

    def _find_product(self, expected_product_name: str) -> WebElement:
        """
        Finds a product element by name.

        :param expected_product_name: Name of the product
        :return: WebElement of the product
        """
        for product in self.element_actions.find_elements(self.PRODUCTS_LIST_LOC):
            product_name = product.find_element(*self.PRODUCT_NAME_LOC).text
            if product_name == expected_product_name:
                return product
        raise AssertionError(f"Product not found: {expected_product_name}")
