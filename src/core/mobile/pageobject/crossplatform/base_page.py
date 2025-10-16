from abc import ABC

import allure
from appium.webdriver.common.appiumby import AppiumBy

from src.core.mobile.pageobject.crossplatform.navigation_menu_page import NavigationMenuPage
from src.core.mobile.pageobject.mobile_base_page import MobileBasePage


class BasePage(MobileBasePage, ABC):
    """Base page for all (cross-platform iOS + Android) pages."""
    MENU_BTN_LOC = {
        "ios": (AppiumBy.ACCESSIBILITY_ID, "More-tab-item"),
        "android": (AppiumBy.ACCESSIBILITY_ID, "open menu")
    }

    @allure.step("Go to Top Navigation Bar.")
    def expand_navigation_menu(self) -> NavigationMenuPage:
        """Expand navigation menu."""
        locator = self._get_platform_locator(self.MENU_BTN_LOC)
        self.element_actions.click(locator)
        return NavigationMenuPage(self.driver)
