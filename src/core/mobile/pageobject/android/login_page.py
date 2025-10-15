import allure
from appium.webdriver.common.appiumby import AppiumBy

from src.core.mobile.assertions.android.login_page_assertions import LoginPageAssertions
from src.core.mobile.pageobject.android.base_page import BasePage
from src.core.mobile.pageobject.android.catalog_page import CatalogPage


class LoginPage(BasePage):
    """Page object for the Login Page of the android application."""

    HEADER_LOC = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Login").instance(0)')
    USERNAME_FLD_LOC = (AppiumBy.ACCESSIBILITY_ID, "Username input field")
    PASSWORD_FLD_LOC = (AppiumBy.ACCESSIBILITY_ID, "Password input field")
    LOGIN_BTN_LOC = (AppiumBy.ACCESSIBILITY_ID, "Login button")
    GENERIC_ERROR_MSG_LOC = (AppiumBy.XPATH, '//*[@content-desc="generic-error-message"]/android.widget.TextView')
    USERNAME_ERROR_MSG_LOC = (AppiumBy.XPATH, '//*[@content-desc="Username-error-message"]/android.widget.TextView')
    PASSWORD_ERROR_MSG_LOC = (AppiumBy.XPATH, '//*[@content-desc="Password-error-message"]/android.widget.TextView')

    def enter_username(self, username: str):
        """Enters the provided username."""
        self.element_actions.type_text(self.USERNAME_FLD_LOC, username)
        return self

    def enter_password(self, password: str):
        """Enters the provided password."""
        self.element_actions.type_text(self.PASSWORD_FLD_LOC, password)
        return self

    def tap_login_button(self):
        """Taps the login button."""
        self.element_actions.click(self.LOGIN_BTN_LOC)
        return self

    @allure.step("Logging in to app with '{1}' username and '{2}' password.")
    def login(self, username: str, password: str):
        """Logs in using the provided credentials."""
        return (self.enter_username(username)
                .enter_password(password)
                .tap_login_button())

    def login_then_goto_catalog_page(self, username: str, password: str) -> CatalogPage:
        """Perform login and navigate to Catalog Page."""
        self.login(username, password)
        return CatalogPage(self.driver)

    def get_username_error_msg(self) -> str:
        """Returns the error message for missing username."""
        return self.element_actions.get_text(self.USERNAME_ERROR_MSG_LOC)

    def get_password_error_msg(self) -> str:
        """Returns the error message for missing password."""
        return self.element_actions.get_text(self.PASSWORD_ERROR_MSG_LOC)

    def get_generic_error_msg(self) -> str:
        """Returns the generic login error message."""
        return self.element_actions.get_text(self.GENERIC_ERROR_MSG_LOC)

    def assert_that(self) -> LoginPageAssertions:
        """Returns an instance of LoginPageAssertions for validations."""
        return LoginPageAssertions(self)

    def wait_until_page_loaded(self) -> None:
        self.wait_until.element_visible(self.HEADER_LOC)
