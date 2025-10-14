import allure
from selenium.webdriver import Remote

from src import logger
from src.core.data.configs.web_configs import WebConfigs
from src.core.web.pageobject.login_page import LoginPage


class PageNavigator:
    """Provides navigation to different pages of the web application."""

    def __init__(self, driver: Remote, configs: WebConfigs):
        self.driver = driver
        self.configs = configs

    @allure.step("Go to Login Page.")
    def goto_login_page(self) -> LoginPage:
        """Navigate to the Login Page."""
        logger.info("Go to Login page.")
        self.driver.get(self.configs.web_base_url)
        return LoginPage(self.driver)
