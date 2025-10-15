from __future__ import annotations  # allow forward type references

from typing import TYPE_CHECKING

import allure

from src import logger

if TYPE_CHECKING:
    # Only imported for type hints, not at runtime
    from src.core.mobile.pageobject.android.catalog_page import CatalogPage


class CatalogPageAssertions:
    """Asserts for Catalog Page."""

    EXPECTED_HEADER = "Products"

    def __init__(self, page: "CatalogPage"):
        self.page = page

    @allure.step("Verify Catalog page header matches the expected text.")
    def shows_correct_header(self) -> "CatalogPageAssertions":
        """ Verifies that the Catalog page header matches the expected text """
        logger.info(f"Verifying if '{self.EXPECTED_HEADER}' header is displayed.")
        actual_header = self.page.get_header()
        assert actual_header == self.EXPECTED_HEADER, \
            f"Header mismatch: expected {self.EXPECTED_HEADER}, got {actual_header}"
        return self
