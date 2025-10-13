import allure
from selenium.webdriver import Remote

from src import logger
from src.core.data.properties.web_properties import WebProperties
from src.core.web.pageobject.login_page import LoginPage


class PageNavigator:
    """Provides navigation to different pages of the web application."""

    def __init__(self, driver: Remote, properties: WebProperties):
        self.driver = driver
        self.properties = properties

    @allure.step("Go to Login Page.")
    def goto_login_page(self) -> LoginPage:
        """Navigate to the Login Page."""
        logger.info("Go to Login page.")
        self.driver.get(self.properties.web_base_url)
        return LoginPage(self.driver)
