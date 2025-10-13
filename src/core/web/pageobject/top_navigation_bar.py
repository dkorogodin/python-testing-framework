from __future__ import annotations

from typing import TYPE_CHECKING

import allure
from selenium.webdriver.common.by import By

from src import logger
from src.core.web.pageobject.common.web_base_page import WebBasePage

if TYPE_CHECKING:
    from src.core.web.pageobject.cart_page import CartPage
    from src.core.web.pageobject.home_page import HomePage
    from src.core.web.pageobject.login_page import LoginPage
    from src.core.web.pageobject.orders_history_page import OrdersHistoryPage


class TopNavigationBar(WebBasePage):
    """Page object for the Top Navigation Bar."""
    HOME_BTN = (By.XPATH, "//button[text()=' HOME ']")
    ORDERS_BTN = (By.XPATH, "//button[@routerlink='/dashboard/myorders']")
    CART_BTN = (By.XPATH, "//button[@routerlink='/dashboard/cart']")
    SIGN_OUT_BTN = (By.XPATH, "//button[text()=' Sign Out ']")

    @allure.step("Go to Home page.")
    def goto_home_page(self) -> "HomePage":
        """Navigate to Home Page."""
        from src.core.web.pageobject.home_page import HomePage
        return self._navigate(self.HOME_BTN, HomePage)

    @allure.step("Go to Orders History page.")
    def goto_orders_history_page(self) -> "OrdersHistoryPage":
        """Navigate to Orders History Page."""
        from src.core.web.pageobject.orders_history_page import OrdersHistoryPage
        return self._navigate(self.ORDERS_BTN, OrdersHistoryPage)

    @allure.step("Go to Cart page.")
    def goto_cart_page(self) -> "CartPage":
        """Navigate to Cart Page."""
        from src.core.web.pageobject.cart_page import CartPage
        return self._navigate(self.CART_BTN, CartPage)

    @allure.step("Sign Out.")
    def sign_out(self) -> "LoginPage":
        """Sign out the current user."""
        from src.core.web.pageobject.login_page import LoginPage
        return self._navigate(self.SIGN_OUT_BTN, LoginPage)

    def wait_until_page_loaded(self) -> None:
        """Wait until the Top Navigation Bar is loaded."""
        self.wait_until.element_clickable(self.HOME_BTN)

    def _navigate(self, locator: tuple[str, str], page_class):
        """
        Clicks the given button locator and returns an instance of the target page.

        :param locator: locator of the button
        :param page_class: class of the page to return
        """
        logger.info(f"Navigating to page via button: {locator}")
        self.element_actions.click(locator)
        return page_class(self.driver)
