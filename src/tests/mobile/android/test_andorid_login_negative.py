import allure
import pytest

from src.core.mobile.data.dataprovider.login_data_provider import invalid_login_credentials


@pytest.mark.android
@pytest.mark.negative
@pytest.mark.login
class TestAndroidLoginNegative:

    @allure.description("Login validation: Verify login with invalid credentials returns specific error msg.")
    @pytest.mark.parametrize("username,password", invalid_login_credentials())
    def test_invalid_credentials(self, username, password, login_page):
        (login_page
         .login(username, password)
         .assert_that()
         .shows_credentials_do_not_match_msg())

    @allure.description("Login validation: Verify login with empty username returns specific error msg.")
    def test_empty_username(self, login_page):
        (login_page
         .login("", "10203040")
         .assert_that()
         .shows_username_required_msg())

    @allure.description("Login validation: Verify login with empty password returns specific error msg.")
    def test_empty_password(self, login_page):
        (login_page
         .login("bob@example.com", "")
         .assert_that()
         .shows_password_required_msg())
