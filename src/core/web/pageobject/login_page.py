import allure
from selenium.webdriver.common.by import By

from src import logger
from src.core.web.assertions.login_page_assertions import LoginPageAssertions
from src.core.web.pageobject.common.web_base_page import WebBasePage
from src.core.web.pageobject.home_page import HomePage


class LoginPage(WebBasePage):
    """Page object for the Login Page of the web application."""
    USER_EMAIL_FLD = (By.ID, "userEmail")
    USER_PASSWORD_FLD = (By.ID, "userPassword")
    LOGIN_BTN = (By.ID, "login")
    EMAIL_REQUIRED_MSG = (By.XPATH, "//*[text()='*Email is required']")
    PASSWORD_REQUIRED_MSG = (By.XPATH, "//*[text()='*Password is required']")

    @allure.step("Login to app with '{username}' username.")
    def login(self, username: str, password: str) -> "LoginPage":
        """Perform login with specified username and password."""
        logger.info(f"Login to app with username '{username}' and password '{password}'.")
        self.element_actions.type_text(self.USER_EMAIL_FLD, username)
        self.element_actions.type_text(self.USER_PASSWORD_FLD, password)
        self.element_actions.click(self.LOGIN_BTN)
        return self

    def login_then_goto_home_page(self, username: str, password: str) -> HomePage:
        """Perform login and navigate to Home Page."""
        self.login(username, password)
        return HomePage(self.driver)

    def get_email_required_msg(self) -> str:
        return self.element_actions.get_text(self.EMAIL_REQUIRED_MSG)

    def get_password_required_msg(self) -> str:
        return self.element_actions.get_text(self.PASSWORD_REQUIRED_MSG)

    def assert_that(self) -> LoginPageAssertions:
        """Return assertions for the Login Page."""
        return LoginPageAssertions(self)

    def wait_until_page_loaded(self) -> None:
        """Wait until Login Page is loaded."""
        self.wait_until.element_visible(self.USER_EMAIL_FLD)
