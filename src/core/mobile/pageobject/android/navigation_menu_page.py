from __future__ import annotations

from typing import TYPE_CHECKING

import allure
from appium.webdriver.common.appiumby import AppiumBy

from src.core.mobile.pageobject.mobile_base_page import MobileBasePage

if TYPE_CHECKING:
    from src.core.mobile.pageobject.android.catalog_page import CatalogPage
    from src.core.mobile.pageobject.android.login_page import LoginPage


class NavigationMenuPage(MobileBasePage):
    """Page object for the Navigation Menu of the android application."""

    CATALOG_MENU_ITEM_LOC = (AppiumBy.ACCESSIBILITY_ID, "menu item catalog")
    LOGIN_MENU_ITEM_LOC = (AppiumBy.ACCESSIBILITY_ID, "menu item log in")

    @allure.step("Go to Catalog Page.")
    def goto_catalog_page(self) -> "CatalogPage":
        """Go to Catalog Page."""
        self.element_actions.click(self.CATALOG_MENU_ITEM_LOC)
        from src.core.mobile.pageobject.android.catalog_page import CatalogPage
        return CatalogPage(self.driver)

    @allure.step("Go to Login Page.")
    def goto_login_page(self) -> "LoginPage":
        """Go to Login Page."""
        self.element_actions.click(self.LOGIN_MENU_ITEM_LOC)
        from src.core.mobile.pageobject.android.login_page import LoginPage
        return LoginPage(self.driver)

    def wait_until_page_loaded(self):
        self.wait_until.element_visible(self.CATALOG_MENU_ITEM_LOC)
