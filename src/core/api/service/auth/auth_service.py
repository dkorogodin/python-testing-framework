import allure

from src.core.api.core.response import ApiResponse
from src.core.api.core.response_validator import ApiResponseValidator
from src.core.api.service.auth.controller.auth_controller import AuthController
from src.core.api.service.auth.model.basic_auth import BasicAuth


class AuthService:
    """
    High-level service for authentication API interactions.

    Wraps the AuthController to provide convenient methods for
    logging in, storing responses, and validating API results.
    """

    def __init__(self, base_url: str, timeout: int = 10):
        self.controller = AuthController(base_url=base_url, timeout=timeout)
        self.response: ApiResponse | None = None

    @allure.step("Login and retrieve token")
    def login(self, credentials: BasicAuth) -> "AuthService":
        """
        Logs in using the provided credentials and stores the response.
        Enables fluent method chaining.

        :param credentials: BasicAuth object with username and password
        :return: self
        """
        self.response = self.controller.login(credentials)
        return self

    @allure.step("Validate API response")
    def verify_that_response(self) -> ApiResponseValidator:
        """
        Returns a validator for the last API response.

        :return: ApiResponseValidator instance for asserting response contents
        """
        if self.response is None:
            raise ValueError("No response available. Call login() first.")
        return ApiResponseValidator(self.response)
