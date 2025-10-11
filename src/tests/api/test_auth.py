from http import HTTPStatus
from typing import cast

import pytest

from src.core.api.service.auth.auth_service import AuthService
from src.core.api.service.auth.model.basic_auth import BasicAuth
from src.core.api.service.auth.model.token import Token
from src.core.data.factory.auth.auth.api_auth_factory import ApiAuthFactory
from src.core.data.factory.auth.auth.basic_auth_data_builder import BasicAuthDataBuilder
from src.core.data.factory.auth.token.api_auth_token_factory import ApiAuthTokenFactory
from src.core.data.factory.auth.token.token_constant_data_builder import TokenConstantDataBuilder


@pytest.fixture
def auth_service(api_service_manager) -> AuthService:
    return api_service_manager.get_auth_service()


def test_auth(auth_service, properties_manager):
    expected_token: Token = ApiAuthTokenFactory.get_token(
        TokenConstantDataBuilder(properties_manager.web_properties.web_username)
    )
    basic_auth = BasicAuthDataBuilder(
        username=properties_manager.web_properties.web_username,
        password=properties_manager.web_properties.web_password
    )
    auth = cast(BasicAuth, ApiAuthFactory.get_api_auth(basic_auth))

    (auth_service
     .login(auth)
     .verify_that_response()
     .status_code_is_equal_to(HTTPStatus.OK)
     .body_is_equal_to(expected_token))
