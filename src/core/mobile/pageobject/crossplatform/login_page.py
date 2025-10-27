import allure
from appium.webdriver.common.appiumby import AppiumBy

from src.core.mobile.assertions.crossplatform.login_page_assertions import LoginPageAssertions
from src.core.mobile.pageobject.crossplatform.base_page import BasePage
from src.core.mobile.pageobject.crossplatform.catalog_page import CatalogPage


class LoginPage(BasePage):
    """Page object for the Login Page of the (cross-platform iOS + Android) application."""

    HEADER_LOC = {
        "ios": (AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeStaticText[`name == \"Login\"`][1]"),
        "android": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Login").instance(0)')
    }

    USERNAME_FLD_LOC = {
        "ios": (AppiumBy.XPATH,
                "//*[@name=\"User Name\"]/following-sibling::XCUIElementTypeOther[1]/XCUIElementTypeTextField"),
        "android": (AppiumBy.ACCESSIBILITY_ID, "Username input field")
    }

    PASSWORD_FLD_LOC = {
        "ios": (AppiumBy.XPATH,
                "//*[@name=\"Password\"]/following-sibling::XCUIElementTypeOther[1]/XCUIElementTypeSecureTextField"),
        "android": (AppiumBy.ACCESSIBILITY_ID, "Password input field")
    }

    LOGIN_BTN_LOC = {
        "ios": (AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton[`name == \"Login\"`]"),
        "android": (AppiumBy.ACCESSIBILITY_ID, "Login button")
    }

    GENERIC_ERROR_MSG_LOC = {
        "ios": (),
        "android": (AppiumBy.XPATH, '//*[@content-desc="generic-error-message"]/android.widget.TextView')
    }

    USERNAME_ERROR_MSG_LOC = {
        "ios": (),
        "android": (AppiumBy.XPATH, '//*[@content-desc="Username-error-message"]/android.widget.TextView')
    }

    PASSWORD_ERROR_MSG_LOC = {
        "ios": (),
        "android": (AppiumBy.XPATH, '//*[@content-desc="Password-error-message"]/android.widget.TextView')
    }

    FIRST_VALID_HARDCODED_USER_LOC = {
        "ios": (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name=\"bob@example.com\"]"),
        "android": ()
    }

    @allure.step("Logging in to app with '{1}' username and '{2}' password.")
    def login(self, username: str, password: str) -> "LoginPage":
        """Logs in using the provided credentials."""
        return (self.enter_username(username)
                .enter_password(password)
                .tap_login_button())

    @allure.step("Logging in to app with hardcoded user that app provided on the screen.")
    def login_with_first_hardcoded_user(self) -> "LoginPage":
        """Logs in using the hardcoded user that app provided on the screen."""
        locator = self._get_platform_locator(self.FIRST_VALID_HARDCODED_USER_LOC)
        self.element_actions.click(locator)
        return self.tap_login_button()

    def login_then_goto_catalog_page(self, username: str, password: str) -> CatalogPage:
        """Perform login and navigate to Catalog Page."""
        if self._is_ios():
            self.login_with_first_hardcoded_user()
        else:
            self.login(username, password)
        return CatalogPage(self.driver)

    def enter_username(self, username: str) -> "LoginPage":
        """Enters the provided username."""
        locator = self._get_platform_locator(self.USERNAME_FLD_LOC)
        self.element_actions.type_text(locator, username)
        return self

    def enter_password(self, password: str) -> "LoginPage":
        """Enters the provided password."""
        locator = self._get_platform_locator(self.PASSWORD_FLD_LOC)
        self.element_actions.type_text(locator, password)
        return self

    def tap_login_button(self) -> "LoginPage":
        """Taps the login button."""
        locator = self._get_platform_locator(self.LOGIN_BTN_LOC)
        self.element_actions.click(locator)
        return self

    def get_username_error_msg(self) -> str:
        """Returns the error message for missing username."""
        locator = self._get_platform_locator(self.USERNAME_ERROR_MSG_LOC)
        return self.element_actions.get_text(locator)

    def get_password_error_msg(self) -> str:
        """Returns the error message for missing password."""
        locator = self._get_platform_locator(self.PASSWORD_ERROR_MSG_LOC)
        return self.element_actions.get_text(locator)

    def get_generic_error_msg(self) -> str:
        """Returns the generic login error message."""
        locator = self._get_platform_locator(self.GENERIC_ERROR_MSG_LOC)
        return self.element_actions.get_text(locator)

    def assert_that(self) -> LoginPageAssertions:
        """Returns an instance of LoginPageAssertions for validations."""
        return LoginPageAssertions(self)

    def wait_until_page_loaded(self):
        locator = self._get_platform_locator(self.HEADER_LOC)
        self.wait_until.element_visible(locator)
