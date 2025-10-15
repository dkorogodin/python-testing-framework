import allure
import pytest


@pytest.mark.android
@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.login
class TestAndroidLoginNegative:

    @allure.description("Login validation: Verify login with valid credentials returns Catalog page.")
    def test_valid_login(self, login_page):
        catalog_page = login_page.login_then_goto_catalog_page("bob@example.com", "10203040")
        (catalog_page
         .assert_that()
         .shows_correct_header())
