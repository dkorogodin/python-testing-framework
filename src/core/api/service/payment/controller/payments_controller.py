from src import logger
from src.core.api.core.http_client import HttpClient
from src.core.api.core.response import ApiResponse
from src.core.api.service.auth.model.token_auth import TokenAuth


class PaymentsController:
    """
    Controller for operations on multiple payments.

    Provides methods to fetch all payments.
    Handles authorization using token-based authentication.
    """

    PAYMENTS_ENDPOINT = "/api/v2/payments"

    def __init__(self, base_url: str, auth: TokenAuth, timeout: int = 10):
        self.auth = auth
        self.client = HttpClient(base_url=base_url, timeout=timeout)

    def fetch_all_payments(self) -> ApiResponse:
        """
        Fetches all payments.
        """
        logger.info("Fetching all payments.")

        response = self.client.get(
            endpoint=self.PAYMENTS_ENDPOINT,
            headers={self.auth.header: f"{self.auth.token}"}
        )

        return ApiResponse(response)
