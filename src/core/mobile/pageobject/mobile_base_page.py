from abc import ABC
from typing import Optional

from appium.webdriver.webdriver import WebDriver

from src import logger
from src.core.mobile.data.enums.mobile_platform import MobilePlatform
from src.core.mobile.util.actions.context_actions import ContextActions
from src.core.mobile.util.actions.keyboard_actions import KeyboardActions
from src.core.mobile.util.gestures.ui_automator_2driver_gestures import UIAutomator2DriverGestures
from src.core.mobile.util.gestures.xcui_test_driver_gestures import XCUITestDriverGestures
from src.core.util.platformshared.base_page_object import BasePageObject


class MobileBasePage(BasePageObject, ABC):
    """Generic base Page Object for mobile screens."""

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self._keyboard_actions: Optional[KeyboardActions] = None
        self._context_actions: Optional[ContextActions] = None
        self._gestures: Optional[object] = None  # UIAutomator2DriverGestures | XCUITestDriverGestures

    def perform_keyboard_actions(self) -> KeyboardActions:
        if self._keyboard_actions is None:
            self._keyboard_actions = KeyboardActions(self.driver)
        return self._keyboard_actions

    def perform_context_actions(self) -> ContextActions:
        if self._context_actions is None:
            self._context_actions = ContextActions(self.driver)
        return self._context_actions

    def perform_gestures(self):
        if self._gestures is None:
            if self._is_ios():
                logger.info("Initializing iOS XCUITest gestures.")
                self._gestures = XCUITestDriverGestures(self.driver)
            else:
                logger.info("Initializing Android UIAutomator2 gestures.")
                self._gestures = UIAutomator2DriverGestures(self.driver)
        return self._gestures

    def _is_ios(self) -> bool:
        """Checks if current platform is iOS."""
        return self.driver.capabilities.get("platformName", "").lower() == MobilePlatform.IOS.value.lower()

    def _get_platform_locator(self, locator_map: dict) -> tuple[str, str]:
        """Returns locator tuple based on platform name."""
        platform = self.driver.capabilities.get("platformName", "").lower()
        if "ios" in platform:
            return locator_map["ios"]
        return locator_map["android"]
