from abc import ABC

import allure

from src import logger
from src.core.web.pageobject.common.web_base_page import WebBasePage
from src.core.web.pageobject.top_navigation_bar import TopNavigationBar


class WebBaseLoggedInPage(WebBasePage, ABC):
    """Base page for all pages requiring logged-in user context."""

    @allure.step("Go to Top Navigation Bar.")
    def goto_top_navigation_bar(self) -> TopNavigationBar:
        """
        Navigates to the Top Navigation Bar section of the page.

        :return: TopNavigationBar page object
        """
        logger.info("Go to Top Navigation Bar.")
        return TopNavigationBar(self.driver)
