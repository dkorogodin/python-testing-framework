from __future__ import annotations  # allow forward type references

from typing import TYPE_CHECKING

import allure

from src import logger

if TYPE_CHECKING:
    # Only imported for type hints, not at runtime
    from src.core.mobile.pageobject.crossplatform.catalog_page import CatalogPage


class CatalogPageAssertions:
    """Asserts for Catalog Page."""

    def __init__(self, page: "CatalogPage"):
        self.page = page

    @allure.step("Verify Catalog page shows at least one product.")
    def shows_at_least_one_product(self) -> "CatalogPageAssertions":
        """ Verifies Catalog page shows at least one product"""
        logger.info("Verifying Catalog page shows at least one product.")
        product_number = self.page.get_products_number()
        assert product_number >= 1, "Catalog page shows no products."
        return self
