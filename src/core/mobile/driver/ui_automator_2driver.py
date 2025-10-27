from appium.options.common import AppiumOptions
from appium.webdriver.webdriver import WebDriver

from src import logger
from src.core.data.configs.mobile_configs import MobileConfigs
from src.core.mobile.data.enums.mobile_platform import MobilePlatform
from src.core.util.platformshared.driver import Driver


class UIAutomator2Driver(Driver):

    def __init__(self, configs: MobileConfigs):
        self.configs = configs

    def initiate_driver(self) -> WebDriver:
        """Initiate Appium WebDriver with UIAutomator2 options."""
        appium_url = self.configs.appium_service_url
        if not appium_url:
            raise ValueError("Appium URL must not be null")

        options = self._get_android_options()

        logger.info(f"Starting Appium WebDriver at {appium_url} with options: {options.to_capabilities()}")
        driver = WebDriver(appium_url, options=options)
        logger.info(f"Appium WebDriver initiated, session id: {driver.session_id}")
        return driver

    def _get_android_options(self) -> AppiumOptions:
        options = AppiumOptions()
        options.platform_name = MobilePlatform.ANDROID.appium_name
        options.set_capability("appium:automationName", "UIAutomator2")
        options.avd_launch_timeout = 3 * 60 * 1000
        options.set_capability("appium:app", self.configs.app_name)
        options.set_capability("appium:platformVersion", self.configs.device_platform_version)

        if not self.configs.is_cloud:
            options.udid = self.configs.device_udid
            options.app_package = self.configs.app_package_or_bundle_id
        else:
            options.set_capability("appium:deviceName", self.configs.device_name)
            options.set_capability("bstack:options", {
                "userName": self.configs.cloud_username,
                "accessKey": self.configs.cloud_access_key,
                "sessionName": self.configs.cloud_session_name,
                "buildName": self.configs.cloud_build_name
            })

        return options
