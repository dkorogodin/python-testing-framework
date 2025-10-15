from abc import ABC

import allure
from appium.webdriver.common.appiumby import AppiumBy

from src.core.mobile.pageobject.ios.navigation_menu_page import NavigationMenuPage
from src.core.mobile.pageobject.mobile_base_page import MobileBasePage


class BasePage(MobileBasePage, ABC):
    """Base page for all ios pages."""
    MORE_NAVIGATION_MENU_BTN_LOC = (AppiumBy.ACCESSIBILITY_ID, "More-tab-item")
    CATALOG_BTN_LOC = (AppiumBy.ACCESSIBILITY_ID, "Catalog-tab-item")

    @allure.step("Go to Top Navigation Bar.")
    def expand_navigation_menu(self) -> NavigationMenuPage:
        """Expand navigation menu."""
        self.element_actions.click(self.MORE_NAVIGATION_MENU_BTN_LOC)
        return NavigationMenuPage(self.driver)
