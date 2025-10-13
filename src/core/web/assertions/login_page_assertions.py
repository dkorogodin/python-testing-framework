from __future__ import annotations  # allow forward type references

from typing import TYPE_CHECKING

import allure

from src import logger
from src.core.web.assertions.base_page_assertions import BasePageAssertions

if TYPE_CHECKING:
    # Only imported for type hints, not at runtime
    from src.core.web.pageobject.login_page import LoginPage


class LoginPageAssertions(BasePageAssertions):
    """Assertion class for LoginPage, providing login page-specific verification methods."""

    INCORRECT_CREDENTIALS_MSG = "Incorrect email or password."
    EMAIL_REQUIRED_MSG = "*Email is required"
    PASSWORD_REQUIRED_MSG = "*Password is required"

    def __init__(self, page: "LoginPage"):
        super().__init__(page)
        self.page = page  # keep IDE type support

    @allure.step("Verify '*Email is required' msg displayed.")
    def shows_email_required_msg(self) -> "LoginPageAssertions":
        logger.info("Verify '*Email is required' message displayed.")
        actual = self.page.get_email_required_msg()
        assert actual == self.EMAIL_REQUIRED_MSG, (
            f"Expected '{self.EMAIL_REQUIRED_MSG}', got '{actual}'"
        )
        return self

    @allure.step("Verify '*Password is required' msg displayed.")
    def shows_password_required_msg(self) -> "LoginPageAssertions":
        logger.info("Verify '*Password is required' message displayed.")
        actual = self.page.get_password_required_msg()
        assert actual == self.PASSWORD_REQUIRED_MSG, (
            f"Expected '{self.PASSWORD_REQUIRED_MSG}', got '{actual}'"
        )
        return self
