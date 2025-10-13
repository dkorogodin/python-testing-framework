import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from src import logger

DEFAULT_WAIT_SECONDS = 30


class WebDriverWaitConditions:
    """Utility wrapper for WebDriverWait conditions."""

    def __init__(self, driver, timeout: int = DEFAULT_WAIT_SECONDS):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        logger.info(f"Initialized WebDriverWaitConditions with {timeout}s timeout")

    # ----------------------------
    # Configuration
    # ----------------------------
    def change_driver_wait_duration(self, seconds: int):
        """Change the WebDriverWait timeout duration."""
        logger.info(f"Changing WebDriver wait duration to '{seconds}' seconds")
        self.wait = WebDriverWait(self.driver, seconds)

    # ----------------------------
    # Element visibility / presence
    # ----------------------------
    def elements_visible(self, elements: tuple[str, str]):
        """Wait until all given elements are visible."""
        return self.wait.until(EC.visibility_of_all_elements_located(elements))

    def element_present(self, locator: tuple[str, str]):
        """Wait until element located by the locator is present."""
        return self.wait.until(EC.presence_of_element_located(locator))

    def element_visible(self, locator: tuple[str, str]):
        """Wait until the element (locator) is visible."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def text_to_be_present_in_element(self, locator: tuple[str, str], text_: str):
        """Wait until given text is present in the specified element."""
        return self.wait.until(EC.text_to_be_present_in_element(locator, text_))

    # ----------------------------
    # Element invisibility
    # ----------------------------
    def element_invisible(self, locator: tuple[str, str]):
        """Wait until element (locator) is invisible."""
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def element_invisible_if_present(self, element):
        """Wait until element is invisible if currently displayed."""
        try:
            if element.is_displayed():
                self.wait.until(EC.invisibility_of_element(element))
        except Exception as e:
            logger.info(f"Element not present or already invisible: {e}")

    # ----------------------------
    # Clickability
    # ----------------------------
    def element_clickable(self, locator: tuple[str, str]):
        """Wait until element (locator) is clickable."""
        return self.wait.until(EC.element_to_be_clickable(locator))

    def element_clickable_with_delay(self, locator, millis: int):
        """Wait until element is clickable, then wait an additional delay."""
        element = self.element_clickable(locator)
        time.sleep(millis / 1000)
        return element
