import os

import pytest
from pytest_bdd import scenarios, given, when, then, parsers

from src.core.mobile.pageobject.android.catalog_page import CatalogPage

CURRENT_DIR = os.path.dirname(__file__)
scenarios(os.path.abspath(os.path.join(CURRENT_DIR, "../features/login.feature")))


@pytest.fixture
def catalog_page(mobile_manager):
    return CatalogPage(mobile_manager.get_driver())


@pytest.fixture
def login_page(catalog_page):
    return catalog_page.expand_navigation_menu().goto_login_page()


@given("I am on Login page")
def open_login_page(login_page):
    """Ensure we are on login page (fixture handles navigation)."""
    return login_page


@when(parsers.parse('I enter username "{username}"'))
def enter_username(login_page, username):
    login_page.enter_username(username)


@when(parsers.parse('I enter password "{password}"'))
def enter_password(login_page, password):
    login_page.enter_password(password)


@when("I tap login button")
def tap_login_button(login_page):
    login_page.tap_login_button()


@then(parsers.parse('I should see error message "{message}"'))
def verify_error_message(login_page, message):
    actual = login_page.get_generic_error_msg()
    assert actual == message, f"Expected '{message}', got '{actual}'"


@then(parsers.parse('I should see Catalog Page with title "{title}"'))
def verify_catalog_title(catalog_page, title):
    actual = catalog_page.get_header()
    assert actual == title, f"Expected title '{title}', got '{actual}'"
