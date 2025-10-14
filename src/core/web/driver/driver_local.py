from selenium import webdriver
from selenium.webdriver import ChromeOptions, Remote

from src import logger
from src.core.data.configs.web_configs import WebConfigs
from src.core.util.platformshared.driver import Driver


class DriverLocal(Driver):
    def __init__(self, configs: WebConfigs):
        self.configs = configs

    def initiate_driver(self) -> Remote:
        browser = self.configs.browser_name
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
