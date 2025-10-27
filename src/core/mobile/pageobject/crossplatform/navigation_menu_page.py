from __future__ import annotations

from typing import TYPE_CHECKING

import allure
from appium.webdriver.common.appiumby import AppiumBy

from src.core.mobile.pageobject.mobile_base_page import MobileBasePage

if TYPE_CHECKING:
    from src.core.mobile.pageobject.crossplatform.login_page import LoginPage


class NavigationMenuPage(MobileBasePage):
    """Page object for the Navigation Menu of the (cross-platform iOS + Android) application."""

    LOGIN_MENU_ITEM_LOC = {
        "ios": (AppiumBy.ACCESSIBILITY_ID, "LogOut-menu-item"),
        "android": (AppiumBy.ACCESSIBILITY_ID, "menu item log in")
    }

    @allure.step("Go to Login Page.")
    def goto_login_page(self) -> "LoginPage":
        """Go to Login Page."""
        locator = self._get_platform_locator(self.LOGIN_MENU_ITEM_LOC)
        self.element_actions.click(locator)
        from src.core.mobile.pageobject.crossplatform.login_page import LoginPage
        return LoginPage(self.driver)

    def wait_until_page_loaded(self):
        locator = self._get_platform_locator(self.LOGIN_MENU_ITEM_LOC)
        self.wait_until.element_visible(locator)
