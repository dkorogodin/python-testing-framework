import allure
from selenium.webdriver.common.by import By

from src import logger
from src.core.web.assertions.login_page_assertions import LoginPageAssertions
from src.core.web.pageobject.common.web_base_page import WebBasePage
from src.core.web.pageobject.home_page import HomePage


class LoginPage(WebBasePage):
    """Page object for the Login Page of the web application."""
    USER_EMAIL_FLD_LOC = (By.ID, "userEmail")
    USER_PASSWORD_FLD_LOC = (By.ID, "userPassword")
    LOGIN_BTN_LOC = (By.ID, "login")
    EMAIL_REQUIRED_MSG_LOC = (By.XPATH, "//*[text()='*Email is required']")
    PASSWORD_REQUIRED_MSG_LOC = (By.XPATH, "//*[text()='*Password is required']")

    @allure.step("Login to app with '{username}' username.")
    def login(self, username: str, password: str) -> "LoginPage":
        """Perform login with specified username and password."""
        logger.info(f"Login to app with username '{username}' and password '{password}'.")
        self.element_actions.type_text(self.USER_EMAIL_FLD_LOC, username)
        self.element_actions.type_text(self.USER_PASSWORD_FLD_LOC, password)
        self.element_actions.click(self.LOGIN_BTN_LOC)
        return self

    def login_then_goto_home_page(self, username: str, password: str) -> HomePage:
        """Perform login and navigate to Home Page."""
        self.login(username, password)
        return HomePage(self.driver)

    def get_email_required_msg(self) -> str:
        return self.element_actions.get_text(self.EMAIL_REQUIRED_MSG_LOC)

    def get_password_required_msg(self) -> str:
        return self.element_actions.get_text(self.PASSWORD_REQUIRED_MSG_LOC)

    def assert_that(self) -> LoginPageAssertions:
        """Return assertions for the Login Page."""
        return LoginPageAssertions(self)

    def wait_until_page_loaded(self):
        """Wait until Login Page is loaded."""
        self.wait_until.element_visible(self.USER_EMAIL_FLD_LOC)
