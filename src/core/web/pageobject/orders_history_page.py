from selenium.webdriver.common.by import By

from src import logger
from src.core.web.pageobject.common.web_base_logged_in_page import WebBaseLoggedInPage


class OrdersHistoryPage(WebBaseLoggedInPage):
    """Page object for the Orders History Page."""
    HEADER_LOC = (By.XPATH, "//h1[text()='Your Orders']")

    def wait_until_page_loaded(self):
        """Wait until the Orders History page is fully loaded."""
        logger.info("Waiting for Orders History page to load...")
        self.wait_until.element_visible(self.HEADER_LOC)
