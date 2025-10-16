from typing import List

import allure
from appium.webdriver import WebElement
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException, StaleElementReferenceException

from src.core.mobile.assertions.android.catalog_page_assertions import CatalogPageAssertions
from src.core.mobile.data.enums.mobile_gesture_direction import MobileGestureDirection
from src.core.mobile.model.product import Product
from src.core.mobile.pageobject.android.base_page import BasePage
from src.core.mobile.pageobject.android.product_details_page import ProductDetailsPage
from src.core.mobile.util.gestures.model.android.swipe_gesture import SwipeGesture


class CatalogPage(BasePage):
    """Page object for the Catalog Page of the android application."""

    HEADER_LOC = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Products\")")
    SCROLL_VIEW_LOC = (AppiumBy.CLASS_NAME, "android.widget.ScrollView")
    PRODUCTS_LOC = (AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc=\"store item\"]")
    PRODUCT_TITLE_LOC = (AppiumBy.XPATH, ".//android.widget.TextView[@content-desc=\"store item text\"]")
    PRODUCT_PRICE_LOC = (AppiumBy.XPATH, ".//android.widget.TextView[@content-desc=\"store item price\"]")

    def get_header(self) -> str:
        """Returns the page header text."""
        return self.element_actions.get_text(self.HEADER_LOC)

    def tap_product_by_title(self, title: str):
        """Taps the product with the specified title in the catalog."""
        self._scroll_until_product_found(title).click()
        return ProductDetailsPage(self.driver)

    @allure.step("Find '{1}' product.")
    def get_product_by_title(self, title: str) -> Product:
        """Retrieves a product from the catalog by its title."""
        product_elem = self._scroll_until_product_found(title)
        title_text = product_elem.find_element(*self.PRODUCT_TITLE_LOC).text.strip()
        price_text = product_elem.find_element(*self.PRODUCT_PRICE_LOC).text.strip()
        return Product(title=title_text, price=price_text)

    def assert_that(self) -> CatalogPageAssertions:
        """Returns an instance of CatalogPageAssertions for validations."""
        return CatalogPageAssertions(self)

    def wait_until_page_loaded(self) -> None:
        self.wait_until.element_visible(self.HEADER_LOC)

    def _scroll_until_product_found(self, title: str) -> WebElement:
        """Scrolls down until the product with the given title is found."""
        attempts = 0
        can_scroll_more = True
        max_scroll_attempts = 10

        while attempts < max_scroll_attempts:
            product = self._find_product(title)
            if product:
                return product
            if not can_scroll_more:
                break
            can_scroll_more = self._scroll_down()
            attempts += 1

        raise NoSuchElementException(
            f"Product '{title}' not found after {attempts} scroll attempts (direction: {MobileGestureDirection.DOWN}).")

    def _scroll_down(self) -> bool:
        """Performs a downward swipe on the catalog."""
        gesture = SwipeGesture(
            element=self.element_actions.find_element(self.SCROLL_VIEW_LOC),
            direction=MobileGestureDirection.DOWN,
            percent=0.5)
        return self.perform_gestures().can_scroll_more(gesture)

    def _find_product(self, title: str) -> WebElement | None:
        """Searches for a product element by its title among currently visible items."""
        products: List[WebElement] = self.driver.find_elements(*self.PRODUCTS_LOC)

        for product in products:
            try:
                titles = product.find_elements(*self.PRODUCT_TITLE_LOC)
                if titles and titles[0].text == title:
                    return product
            except (StaleElementReferenceException, NoSuchElementException):
                continue
        return None
