from appium.options.common import AppiumOptions
from appium.webdriver.webdriver import WebDriver

from src import logger
from src.core.data.configs.mobile_configs import MobileConfigs
from src.core.mobile.data.enums.mobile_platform import MobilePlatform
from src.core.util.platformshared.driver import Driver
from src.core.util.system.port_util import find_free_port


class XCUITestDriver(Driver):
    def __init__(self, configs: MobileConfigs):
        self.configs = configs

    def initiate_driver(self) -> WebDriver:
        """Initiate Appium WebDriver with XCUITest options."""
        appium_url = self.configs.appium_service_url
        if not appium_url:
            raise ValueError("Appium URL must not be null")

        options = self._get_ios_options()

        logger.info(f"Starting Appium WebDriver at {appium_url} with options: {options.to_capabilities()}")
        driver = WebDriver(appium_url, options=options)
        logger.info(f"Appium WebDriver initiated, session id: {driver.session_id}")
        return driver

    def _get_ios_options(self):
        options = AppiumOptions()
        options.platform_name = MobilePlatform.IOS.value
        options.set_capability("appium:automationName", "XCUITest")

        options.simulator_startup_timeout = 3 * 60 * 1000
        options.app = self.configs.app_name
        options.device_name = self.configs.device_name
        options.platform_version = self.configs.device_platform_version

        if not self.configs.is_cloud:
            wda_port = find_free_port(8201, 8299)
            logger.info(f"Using WDA local port: {wda_port}")
            options.wda_local_port = wda_port
            options.udid = self.configs.device_udid

            if self.configs.xcode_org_id and self.configs.xcode_signing_id:
                options.xcode_org_id = self.configs.xcode_org_id
                options.xcode_signing_id = self.configs.xcode_signing_id
        else:
            options.set_capability("bstack:options", {
                "userName": self.configs.cloud_username,
                "accessKey": self.configs.cloud_access_key,
                "sessionName": self.configs.cloud_session_name,
                "buildName": self.configs.cloud_build_name
            })

        return options
