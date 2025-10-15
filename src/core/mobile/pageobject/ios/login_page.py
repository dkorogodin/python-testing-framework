import allure
from appium.webdriver.common.appiumby import AppiumBy

from src.core.mobile.pageobject.ios.base_page import BasePage
from src.core.mobile.pageobject.ios.catalog_page import CatalogPage


class LoginPage(BasePage):
    """Page object for the Login Page of the ios application."""

    HEADER_LOC = (AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeStaticText[`name == \"Login\"`][1]")
    USERNAME_FLD_LOC = (AppiumBy.XPATH,
                        "//*[@name=\"User Name\"]/following-sibling::XCUIElementTypeOther[1]/XCUIElementTypeTextField")
    PASSWORD_FLD_LOC = (AppiumBy.XPATH,
                        "//*[@name=\"Password\"]/following-sibling::XCUIElementTypeOther[1]/XCUIElementTypeSecureTextField")
    FIRST_VALID_HARDCODED_USER_LOC = (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name=\"bob@example.com\"]")
    LOGIN_BTN_LOC = (AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton[`name == \"Login\"`]")

    @allure.step("Logging in to app with '{1}' username and '{2}' password.")
    def login(self, username: str, password: str):
        """Logs in using the provided credentials."""
        (self.enter_username(username)
         .enter_password(password)
         .tap_login_button())

    def login_with_first_hardcoded_user(self):
        """Logs in using the provided credentials."""
        self.element_actions.click(self.FIRST_VALID_HARDCODED_USER_LOC)
        self.tap_login_button()

    def login_then_goto_catalog_page(self) -> CatalogPage:
        """Perform login and navigate to Catalog Page."""
        self.login_with_first_hardcoded_user()
        return CatalogPage(self.driver)

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

    def wait_until_page_loaded(self) -> None:
        self.wait_until.element_visible(self.HEADER_LOC)
