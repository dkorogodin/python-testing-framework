from __future__ import annotations

from typing import TYPE_CHECKING

from src.core.web.assertions.base_page_assertions import BasePageAssertions

if TYPE_CHECKING:
    from src.core.web.pageobject.home_page import HomePage


class HomePageAssertions(BasePageAssertions):
    """Assertion class for HomePage, providing home page-specific verification methods."""

    PRODUCT_ADDED_TO_CART_MSG = "Product Added To Cart"

    def __init__(self, page: "HomePage"):
        super().__init__(page)
        self.page = page  # keep IDE type support
