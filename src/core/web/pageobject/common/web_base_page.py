from abc import ABC

from selenium.webdriver.common.by import By

from src.core.util.platformshared.base_page_object import BasePageObject


class WebBasePage(BasePageObject, ABC):
    """Base page for all web pages, with toast message handling."""
    TOAST_MSG_LOC = (By.CSS_SELECTOR, ".toast-message")

    def get_toast_msg(self) -> str:
        """
        Retrieves the text of a toast message displayed on the page.

        Retries multiple times if a StaleElementReferenceException occurs.
        """
        text = self.element_actions.get_text(self.TOAST_MSG_LOC)
        self.wait_until.element_invisible(self.TOAST_MSG_LOC)
        return text
