from src import logger
from src.core.api.core.http_client import HttpClient
from src.core.api.core.response import ApiResponse
from src.core.api.service.auth.model.basic_auth import BasicAuth


class AuthController:
    """
    Controller for authentication API endpoints.

    Provides methods to send authentication requests, such as logging in
    with basic credentials, and returns ApiResponse objects.
    """

    LOGIN_ENDPOINT = "/api/v2/auth/login"

    def __init__(self, base_url: str, timeout: int = 10):
        self.client = HttpClient(base_url=base_url, timeout=timeout)

    def login(self, credentials: BasicAuth) -> ApiResponse:
        """
        Sends a login request with the given credentials.

        :param credentials: BasicAuth object containing username and password
        :return: ApiResponse object containing authentication result
        """
        logger.info("Sending login request to get auth token.")

        response = self.client.post(
            endpoint=self.LOGIN_ENDPOINT,
            headers={"Content-Type": "application/json"},
            json=credentials.__dict__
        )

        return ApiResponse(response)
