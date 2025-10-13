import allure
import pytest

from src.core.web.assertions.login_page_assertions import LoginPageAssertions
from src.core.web.data.dataprovider.invalid_login_data_provider import invalid_login_json_to_map, \
    invalid_login_simple_data


@pytest.mark.web
@pytest.mark.negative
@pytest.mark.login
@allure.feature("TMS_TEST_ID-1001")
@allure.description("LOGIN")
class TestWebLoginNegative:

    @allure.description("Login validation: Verify login with invalid credentials returns specific error toast msg.")
    @pytest.mark.parametrize("username,password", invalid_login_simple_data())
    def test_invalid_login(self, login_page, username, password):
        (login_page
         .login(username, password)
         .assert_that()
         .shows_toast_msg(LoginPageAssertions.INCORRECT_CREDENTIALS_MSG))

    @allure.description(
        "Login validation: Verify login with invalid credentials from JSON file returns specific error toast msg.")
    @pytest.mark.parametrize("username,password", invalid_login_json_to_map())
    def test_invalid_login_with_json_data(self, login_page, username, password):
        (login_page
         .login(username, password)
         .assert_that()
         .shows_toast_msg(LoginPageAssertions.INCORRECT_CREDENTIALS_MSG))

    @allure.description(
        "Login validation: Verify login with empty credentials returns specific error msg below fields.")
    def test_empty_login(self, login_page):
        (login_page
         .login("", "")
         .assert_that()
         .shows_email_required_msg()
         .and_().shows_password_required_msg())
