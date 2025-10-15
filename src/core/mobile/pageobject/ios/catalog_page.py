from appium.webdriver.common.appiumby import AppiumBy

from src.core.mobile.assertions.ios.catalog_page_assertions import CatalogPageAssertions
from src.core.mobile.pageobject.ios.base_page import BasePage


class CatalogPage(BasePage):
    """Page object for the Catalog Page of the ios application."""

    PRODUCT_LOC = (AppiumBy.XPATH, "//XCUIElementTypeOther[@name=\"ProductItem\"]")

    def get_products_number(self) -> int:
        """Returns the page header text."""
        return len(self.element_actions.find_elements(self.PRODUCT_LOC))

    def assert_that(self) -> CatalogPageAssertions:
        """Returns an instance of CatalogPageAssertions for validations."""
        return CatalogPageAssertions(self)

    def wait_until_page_loaded(self) -> None:
        self.wait_until.element_visible(self.PRODUCT_LOC)
