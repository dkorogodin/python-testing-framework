import os

import pytest
from pytest_bdd import scenarios, given, when, then, parsers

from src.core.mobile.pageobject.android.catalog_page import CatalogPage
from src.core.mobile.pageobject.android.product_details_page import ProductDetailsPage

CURRENT_DIR = os.path.dirname(__file__)
scenarios(os.path.abspath(os.path.join(CURRENT_DIR, "../features/product.feature")))


@pytest.fixture
def catalog_page(mobile_manager):
    return CatalogPage(mobile_manager.get_driver())


@pytest.fixture
def product_details_page(mobile_manager):
    return ProductDetailsPage(mobile_manager.get_driver())


@given(parsers.parse('I am logged in as "{username}" with password "{password}"'))
def login_as(catalog_page, username, password):
    login_page = catalog_page.expand_navigation_menu().goto_login_page()
    login_page.login(username, password)


@then(parsers.parse('I should see product with title "{title}" and price "{price}"'))
def verify_product_listed(catalog_page, title, price):
    product = catalog_page.get_product_by_title(title)
    assert product.title == title
    assert product.price == price


@when(parsers.parse('I tap product title "{title}"'))
def tap_product_title(catalog_page, title):
    catalog_page.tap_product_by_title(title)


@then(parsers.parse('I should be on Product Details page with title "{title}"'))
def verify_on_product_details(product_details_page, title):
    assert product_details_page.get_header() == title, "Not on Product Details page!"


@then(
    parsers.parse('I should see product details with title "{title}", price "{price}" and description "{description}"'))
def verify_product_details(product_details_page, title, price, description):
    product = product_details_page.get_product_details()
    assert product.title == title
    assert product.price == price
    assert product.description == description
