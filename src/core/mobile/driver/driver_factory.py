from appium.webdriver.webdriver import WebDriver

from src.core.data.configs.mobile_configs import MobileConfigs
from src.core.mobile.data.enums.mobile_platform import MobilePlatform
from src.core.mobile.driver.ui_automator_2driver import UIAutomator2Driver
from src.core.mobile.driver.xcui_test_driver import XCUITestDriver


class DriverFactory:
    """Factory for creating Appium drivers based on platform (Android/iOS)."""

    def __init__(self, mobile_configs: MobileConfigs):
        self.mobile_configs = mobile_configs

    def initiate_driver(self) -> WebDriver:
        """Initiate and return an Appium driver."""
        platform = self.mobile_configs.mobile_platform

        if platform == MobilePlatform.ANDROID:
            return UIAutomator2Driver(self.mobile_configs).initiate_driver()
        elif platform == MobilePlatform.IOS:
            return XCUITestDriver(self.mobile_configs).initiate_driver()
        else:
            raise ValueError(f"Unsupported platform: {platform}")
