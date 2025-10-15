from appium.webdriver.common.appiumby import AppiumBy

from src.core.mobile.model.product import Product
from src.core.mobile.pageobject.android.base_page import BasePage


class ProductDetailsPage(BasePage):
    """Page object for the Product Details Page of the android application."""

    HEADER_LOC = (AppiumBy.XPATH, '//*[@content-desc="container header"]//android.widget.TextView')
    PRODUCT_PRICE_LOC = (AppiumBy.ACCESSIBILITY_ID, "product price")
    PRODUCT_DESCRIPTION_LOC = (AppiumBy.ACCESSIBILITY_ID, "product description")

    def get_header(self) -> str:
        """Returns the page header text."""
        return self.element_actions.get_text(self.HEADER_LOC)

    def get_product_details(self) -> Product:
        """Returns product details displayed on this page."""
        return Product(
            title=self.element_actions.get_text(self.HEADER_LOC),
            price=self.element_actions.get_text(self.PRODUCT_PRICE_LOC),
            description=self.element_actions.get_text(self.PRODUCT_DESCRIPTION_LOC)
        )

    def wait_until_page_loaded(self) -> None:
        self.wait_until.element_visible(self.HEADER_LOC)
