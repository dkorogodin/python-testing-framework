import allure
from selenium.webdriver import Remote

from src import logger
from src.core.data.configs.web_configs import WebConfigs
from src.core.util.system.retry_util import RetryUtil
from src.core.web.driver.driver_factory import DriverFactory


class WebAppLifecycle:
    """Manages the lifecycle of a web application session (browser)."""

    def __init__(self, configs: WebConfigs):
        self._configs = configs
        self._driver: Remote | None = None

    def get_driver(self) -> Remote:
        """Returns the active WebDriver, initiating it if not already created."""
        if self._driver is None:
            self._initiate_driver()
        return self._driver

    @allure.step("Restart browser.")
    def restart_browser(self):
        """Restarts the browser by closing and reinitiating the session."""
        logger.info("Restarting browser...")
        self.close_browser()
        self._initiate_driver()

    @allure.step("Close browser.")
    def close_browser(self):
        """Closes the browser if it's currently running."""
        if self._driver:
            logger.info(f"Closing '{self._configs.browser_name}' browser.")
            try:
                self._driver.quit()
            except Exception as e:
                logger.warning(f"Error while closing browser: {e}")
            finally:
                self._driver = None

    @allure.step("Maximize browser window.")
    def maximize_browser_window(self):
        """Maximizes the browser window."""
        if self._driver:
            logger.info("Maximizing browser window.")
            try:
                self._driver.maximize_window()
            except Exception as e:
                logger.warning(f"Failed to maximize browser window: {e}")

    def _initiate_driver(self):
        """Initiates the WebDriver with retry logic."""
        factory = DriverFactory(self._configs)
        self._driver = RetryUtil.retry(factory.initiate_driver, retries=3, delay=1)
        self.maximize_browser_window()
