from abc import ABC, abstractmethod

from selenium.webdriver.remote.webdriver import WebDriver

from src.core.util.platformshared.element_actions import ElementActions
from src.core.util.platformshared.web_driver_wait_conditions import WebDriverWaitConditions


class BasePageObject(ABC):
    """Abstract base class for all page objects."""

    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.wait_until: WebDriverWaitConditions = WebDriverWaitConditions(driver)
        self.element_actions: ElementActions = ElementActions(driver, self.wait_until)
        self.wait_until_page_loaded()

    @abstractmethod
    def wait_until_page_loaded(self) -> None:
        """Wait until the page is fully loaded."""
        pass
