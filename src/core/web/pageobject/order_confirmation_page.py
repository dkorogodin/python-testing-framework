import allure
from selenium.webdriver.common.by import By

from src import logger
from src.core.web.pageobject.common.web_base_logged_in_page import WebBaseLoggedInPage
from src.core.web.pageobject.orders_history_page import OrdersHistoryPage


class OrderConfirmationPage(WebBaseLoggedInPage):
    """Page object for the Order Confirmation Page."""
    ORDERS_LINK_LOC = (By.XPATH, "//label[text()=' Orders History Page ']")

    @allure.step("Go to Orders History page.")
    def goto_orders_history_page(self) -> OrdersHistoryPage:
        """Navigate to the Orders History page."""
        logger.info("Go to Orders History page.")
        self.element_actions.click(self.ORDERS_LINK_LOC)
        return OrdersHistoryPage(self.driver)

    def wait_until_page_loaded(self):
        """Wait until the page is fully loaded."""
        self.wait_until.element_visible(self.ORDERS_LINK_LOC)
