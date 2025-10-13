from selenium import webdriver
from selenium.webdriver import ChromeOptions, Remote

from src import logger
from src.core.data.properties.web_properties import WebProperties
from src.core.util.platformshared.driver import Driver


class DriverLocal(Driver):
    def __init__(self, properties: WebProperties):
        self.properties = properties

    def initiate_driver(self) -> Remote:
        browser = self.properties.browser_name
        logger.info(f"Initializing local WebDriver: {browser}")

        if browser in ["chrome", "chromeheadless"]:
            options = ChromeOptions()
            if "headless" in browser:
                options.add_argument("--headless=new")
            driver = webdriver.Chrome(options=options)
        elif browser == "firefox":
            driver = webdriver.Firefox()
        else:
            logger.warning(f"Unknown browser '{browser}', defaulting to Chrome.")
            driver = webdriver.Chrome()

        logger.info(f"Local {browser} WebDriver initialized.")
        return driver
