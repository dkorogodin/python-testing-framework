from selenium.webdriver import ChromeOptions, FirefoxOptions, Remote

from src import logger
from src.core.data.properties.web_properties import WebProperties
from src.core.util.platformshared.driver import Driver


class DriverRemote(Driver):
    def __init__(self, properties: WebProperties):
        self.properties = properties

    def initiate_driver(self) -> Remote:
        logger.info("Initializing RemoteWebDriver...")

        browser = self.properties.browser_name.lower()

        if browser == "chrome":
            options = ChromeOptions()
        elif browser == "firefox":
            options = FirefoxOptions()
        else:
            logger.warning(f"Unknown browser '{browser}', defaulting to Chrome.")
            options = ChromeOptions()

        driver = Remote(
            command_executor=self.properties.remote_address,
            options=options
        )

        logger.info(f"RemoteWebDriver initialized for browser '{browser}' at {self.properties.remote_address}")
        return driver
