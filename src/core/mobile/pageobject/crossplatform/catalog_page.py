from appium.webdriver.common.appiumby import AppiumBy

from src.core.mobile.assertions.crossplatform.catalog_page_assertions import CatalogPageAssertions
from src.core.mobile.pageobject.crossplatform.base_page import BasePage


class CatalogPage(BasePage):
    """Page object for the Catalog Page of the (cross-platform iOS + Android) application."""

    PRODUCTS_LOC = {
        "ios": (AppiumBy.XPATH, "//XCUIElementTypeOther[@name=\"ProductItem\"]"),
        "android": (AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc=\"store item\"]")
    }

    def get_products_number(self) -> int:
        """Returns the page header text."""
        locator = self._get_platform_locator(self.PRODUCTS_LOC)
        return len(self.element_actions.find_elements(locator))

    def assert_that(self) -> CatalogPageAssertions:
        """Returns an instance of CatalogPageAssertions for validations."""
        return CatalogPageAssertions(self)

    def wait_until_page_loaded(self) -> None:
        locator = self._get_platform_locator(self.PRODUCTS_LOC)
        self.wait_until.element_visible(locator)
