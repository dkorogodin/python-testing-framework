from selenium.webdriver import ChromeOptions, FirefoxOptions, Remote

from src import logger
from src.core.data.configs.web_configs import WebConfigs
from src.core.util.platformshared.driver import Driver


class DriverCloud(Driver):
    def __init__(self, configs: WebConfigs):
        self.configs = configs

    def initiate_driver(self) -> Remote:
        logger.info("Initializing Cloud RemoteWebDriver...")
        cloud_url = f"https://{self.configs.cloud_username}:{self.configs.cloud_access_key}@{self.configs.cloud_remote_address}"
        self.configs.remote_address = cloud_url

        browser = self.configs.browser_name.lower()
        if browser == "chrome":
            options = ChromeOptions()
        elif browser == "firefox":
            options = FirefoxOptions()
        else:
            logger.warning(f"Unknown browser '{browser}', defaulting to Chrome.")
            options = ChromeOptions()

        # Add BrowserStack or cloud service capabilities
        options.set_capability("browserVersion", self.configs.browser_version)
        options.set_capability("bstack:options", {
            "os": self.configs.cloud_os_name,
            "osVersion": self.configs.cloud_os_version,
            "sessionName": self.configs.cloud_session_name,
            "buildName": self.configs.cloud_build_name
        })

        driver = Remote(
            command_executor=self.configs.remote_address,
            options=options
        )

        logger.info(f"Cloud RemoteWebDriver initialized at {self.configs.cloud_remote_address}")
        return driver
