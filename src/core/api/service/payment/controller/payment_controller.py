from src import logger
from src.core.api.core.http_client import HttpClient
from src.core.api.core.response import ApiResponse
from src.core.api.service.auth.model.token_auth import TokenAuth


class PaymentController:
    """
    Controller for individual payment operations.

    Provides methods to fetch or delete a single payment by ID.
    Handles authorization using token-based authentication.
    """

    PAYMENT_ENDPOINT = "/api/v2/payments/payment"

    def __init__(self, base_url: str, auth: TokenAuth, timeout: int = 10):
        self.auth = auth
        self.client = HttpClient(base_url=base_url, timeout=timeout)

    def fetch_payment_by_id(self, payment_id: int) -> ApiResponse:
        """
        Fetches a payment by its ID.
        """
        logger.info("Fetching payment with paymentId=%s", payment_id)

        response = self.client.get(
            endpoint=f"{self.PAYMENT_ENDPOINT}/{payment_id}",
            headers={self.auth.header: f"{self.auth.token}"}
        )

        return ApiResponse(response)

    def remove_payment_by_id(self, payment_id: int) -> ApiResponse:
        """
        Deletes a payment by its ID.
        """
        logger.info("Deleting payment with paymentId=%s", payment_id)

        response = self.client.delete(
            endpoint=f"{self.PAYMENT_ENDPOINT}/{payment_id}",
            headers={self.auth.header: f"{self.auth.token}"}
        )

        return ApiResponse(response)
