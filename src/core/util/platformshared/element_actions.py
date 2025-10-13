from typing import Dict

from selenium.webdriver.remote.webelement import WebElement

from src import logger
from src.core.util.platformshared.web_driver_wait_conditions import WebDriverWaitConditions


class ElementActions:
    """Utility class for common element actions with logging and waits."""

    def __init__(self, driver, wait_until: WebDriverWaitConditions):
        self.driver = driver
        self.wait_until = wait_until

    # ----------------------------
    # Find element(s)
    # ----------------------------
    def find_element(self, locator: tuple[str, str]) -> WebElement:
        logger.info(f"Finding element: {locator}")
        return self.driver.find_element(*locator)

    def find_visible_element(self, locator: tuple[str, str]) -> WebElement:
        logger.info(f"Finding element: {locator}")
        return self.wait_until.element_visible(locator)

    def find_elements(self, locator: tuple[str, str]) -> list[WebElement]:
        logger.info(f"Finding element: {locator}")
        return self.driver.find_elements(*locator)

    # ----------------------------
    # Clicks
    # ----------------------------
    def click(self, locator: tuple[str, str]) -> "ElementActions":
        logger.info(f"Clicking element: {locator}")
        self.wait_until.element_clickable(locator).click()
        return self

    def click_with_delay(self, locator: tuple[str, str], millis: int) -> "ElementActions":
        logger.info(f"Clicking element with delay ({millis} ms): {locator}")
        self.wait_until.element_clickable_with_delay(locator, millis).click()
        return self

    # ----------------------------
    # Typing / Input
    # ----------------------------
    def type_text(self, locator: tuple[str, str], *keys_to_send: str) -> "ElementActions":
        logger.info(f"Typing text '{''.join(keys_to_send)}' into element: {locator}")
        self.wait_until.element_visible(locator).send_keys(*keys_to_send)
        return self

    def clear_field_then_type_text(self, locator: tuple[str, str], *keys_to_send: str) -> "ElementActions":
        logger.info(f"Clearing and typing text '{''.join(keys_to_send)}' into element: {locator}")
        visible_element = self.wait_until.element_visible(locator)
        visible_element.clear()
        visible_element.send_keys(*keys_to_send)
        return self

    # ----------------------------
    # Getters
    # ----------------------------
    def get_attribute(self, locator: tuple[str, str], attribute: str) -> str:
        logger.info(f"Getting attribute '{attribute}' from element: {locator}")
        return self.wait_until.element_visible(locator).get_attribute(attribute)

    def get_css_value(self, locator: tuple[str, str], property_name: str) -> str:
        logger.info(f"Getting CSS value '{property_name}' from element: {locator}")
        return self.wait_until.element_visible(locator).value_of_css_property(property_name)

    def get_text(self, locator: tuple[str, str]) -> str:
        logger.info(f"Getting text from element: {locator}")
        return self.wait_until.element_visible(locator).text

    def get_location(self, locator: tuple[str, str]) -> Dict[str, int]:
        logger.info(f"Getting location of element: {locator}")
        return self.wait_until.element_visible(locator).location

    def get_size(self, locator: tuple[str, str]) -> Dict[str, int]:
        logger.info(f"Getting size of element: {locator}")
        return self.wait_until.element_visible(locator).size

    # ----------------------------
    # Presence check
    # ----------------------------
    def is_element_present(self, locator: tuple[str, str]) -> bool:
        is_present = bool(self.driver.find_elements(*locator))
        logger.info(f"Element presence check for {locator}: {is_present}")
        return is_present
