from __future__ import annotations  # allow forward type references

from typing import TYPE_CHECKING

import allure

from src import logger

if TYPE_CHECKING:
    # Only imported for type hints, not at runtime
    from src.core.mobile.pageobject.android.login_page import LoginPage


class LoginPageAssertions:
    """Assertion class for LoginPage, providing login page-specific verification methods."""

    INVALID_USERNAME_AND_PASSWORD_MSG = "Provided credentials do not match any user in this service."
    USERNAME_REQUIRED_MSG = "Username is required"
    PASSWORD_REQUIRED_MSG = "Password is required"

    def __init__(self, page: "LoginPage"):
        self.page = page

    @allure.step("Verify 'Username is required' msg displayed.")
    def shows_username_required_msg(self) -> "LoginPageAssertions":
        expected = self.USERNAME_REQUIRED_MSG
        logger.info(f"Verify '{expected}' message displayed.")
        actual = self.page.get_username_error_msg()
        assert actual == expected, f"Expected '{expected}', got '{actual}'"
        return self

    @allure.step("Verify 'Password is required' msg displayed.")
    def shows_password_required_msg(self) -> "LoginPageAssertions":
        expected = self.PASSWORD_REQUIRED_MSG
        logger.info(f"Verify '{expected}' message displayed.")
        actual = self.page.get_password_error_msg()
        assert actual == expected, f"Expected '{expected}', got '{actual}'"
        return self

    @allure.step("Verify 'Provided credentials do not match any user in this service.' msg displayed.")
    def shows_credentials_do_not_match_msg(self) -> "LoginPageAssertions":
        expected = self.INVALID_USERNAME_AND_PASSWORD_MSG
        logger.info(f"Verify '{expected}' message displayed.")
        actual = self.page.get_generic_error_msg()
        assert actual == expected, f"Expected '{expected}', got '{actual}'"
        return self
