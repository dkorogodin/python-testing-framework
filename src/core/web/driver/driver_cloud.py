from selenium.webdriver import ChromeOptions, FirefoxOptions, Remote

from src import logger
from src.core.data.properties.web_properties import WebProperties
from src.core.util.platformshared.driver import Driver


class DriverCloud(Driver):
    def __init__(self, properties: WebProperties):
        self.properties = properties

    def initiate_driver(self) -> Remote:
        logger.info("Initializing Cloud RemoteWebDriver...")
        browser = self.properties.browser_name.lower()
        if browser == "chrome":
            options = ChromeOptions()
        elif browser == "firefox":
            options = FirefoxOptions()
        else:
            logger.warning(f"Unknown browser '{browser}', defaulting to Chrome.")
            options = ChromeOptions()

        # Add BrowserStack or cloud service capabilities
        options.set_capability("browserVersion", self.properties.browser_version)
        options.set_capability("bstack:options", {
            "os": self.properties.cloud_os_name,
            "osVersion": self.properties.cloud_os_version,
            "sessionName": self.properties.cloud_session_name,
            "buildName": self.properties.cloud_build_name
        })

        driver = Remote(
            command_executor=self.properties.remote_address,
            options=options
        )

        logger.info(f"Cloud RemoteWebDriver initialized at {self.properties.cloud_remote_address}")
        return driver
