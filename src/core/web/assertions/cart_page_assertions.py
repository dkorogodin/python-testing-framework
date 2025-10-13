from __future__ import annotations  # allow forward type references

from typing import TYPE_CHECKING

import allure

from src import logger
from src.core.api.service.product.model.product import Product
from src.core.web.assertions.base_page_assertions import BasePageAssertions

if TYPE_CHECKING:
    # Only imported for type hints, not at runtime
    from src.core.web.pageobject.cart_page import CartPage


class CartPageAssertions(BasePageAssertions):
    """Assertion class for CartPage, providing cart-specific verification methods."""

    def __init__(self, page: "CartPage"):
        super().__init__(page)
        self.page = page  # keep IDE type support

    @allure.step("Verify {expected_product}' product added to cart.")
    def has_added_product(self, expected_product: Product) -> "CartPageAssertions":
        """
        Verifies that a specific product has been added to the cart.

        :param expected_product: Product expected in the cart
        :return: self (for fluent API)
        """
        logger.info(f"Verify '{expected_product.name}' product added to cart.")
        actual_product = self.page.find_product(expected_product)

        assert actual_product.name == expected_product.name, \
            f"Product name mismatch: expected {expected_product.name}, got {actual_product.name}"
        assert actual_product.price == expected_product.price, \
            f"Price mismatch: expected {expected_product.price}, got {actual_product.price}"
        assert actual_product.currency == expected_product.currency, \
            f"Currency mismatch: expected {expected_product.currency}, got {actual_product.currency}"

        logger.info(f"Product '{expected_product.name}' verified in cart successfully.")
        return self
