import allure

from src import logger
from src.core.web.pageobject.common.web_base_page import WebBasePage


class BasePageAssertions:
    """
    Base class for page-level assertions, providing common verification methods for web pages.

    Supports fluent API style by returning the assertion object itself for chaining.
    """

    def __init__(self, page: WebBasePage):
        self.page = page

    @allure.step("Verify toast msg is equal to '{1}'.")
    def shows_toast_msg(self, expected_text: str) -> "BasePageAssertions":
        """
        Verifies that a toast message is equal to the expected text.

        :param expected_text: expected toast message text
        :return: self (for fluent chaining)
        """
        logger.info(f"Verify toast msg is equal to '{expected_text}'")
        actual_text = self.page.get_toast_msg()
        logger.info(f"Actual toast msg: '{actual_text}'")
        assert actual_text == expected_text, f"Expected toast message '{expected_text}', but got '{actual_text}'"
        return self

    def and_(self) -> "BasePageAssertions":
        """Allows fluent API chaining."""
        return self
