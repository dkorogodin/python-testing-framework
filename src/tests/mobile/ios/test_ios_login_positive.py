import allure
import pytest


@pytest.mark.ios
@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.login
class TestIosLoginPositive:

    @allure.description("Login validation: Verify login with valid credentials returns Catalog page.")
    def test_valid_login(self, login_page):
        catalog_page = login_page.login_then_goto_catalog_page()
        (catalog_page
         .assert_that()
         .shows_at_least_one_product())
