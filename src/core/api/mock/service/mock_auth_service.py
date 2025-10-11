from src.core.api.mock.service.base_mock_service import BaseMockService
from src.core.api.service.auth.controller.auth_controller import AuthController
from src.core.data.factory.auth.token.api_auth_token_factory import ApiAuthTokenFactory
from src.core.data.factory.auth.token.token_constant_data_builder import TokenConstantDataBuilder


class MockAuthService(BaseMockService):
    """Mocks authentication login endpoint."""

    def __init__(self, base_url: str, username: str):
        super().__init__(base_url)
        self.username = username

    def stub_all_api(self):
        self._stub_login()

    def _stub_login(self):
        token = ApiAuthTokenFactory.get_token(TokenConstantDataBuilder(self.username))
        if token is None:
            raise RuntimeError(f"Token generation failed for user: {self.username}")

        self._stub_request(
            method="POST",
            url=AuthController.LOGIN_ENDPOINT,
            body_obj=token,
            status=200
        )
