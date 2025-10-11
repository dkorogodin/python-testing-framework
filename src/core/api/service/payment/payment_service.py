import allure

from src import logger
from src.core.api.core.response import ApiResponse
from src.core.api.core.response_validator import ApiResponseValidator
from src.core.api.service.auth.model.token_auth import TokenAuth
from src.core.api.service.payment.controller.payment_controller import PaymentController
from src.core.api.service.payment.controller.payments_controller import PaymentsController


class PaymentService:
    """
    Service class for interacting with PaymentService APIs.

    Provides methods to fetch individual payments, all payments, or delete
    specific payments and wraps responses for validation using ApiResponseValidator.

    Uses PaymentController and PaymentsController internally
    to perform API calls with authentication via TokenAuth.
    """

    def __init__(self, base_url: str, auth: TokenAuth, timeout: int = 10):
        self.auth = auth
        self.response: ApiResponse | None = None
        self.payment_controller = PaymentController(base_url=base_url, auth=auth, timeout=timeout)
        self.payments_controller = PaymentsController(base_url=base_url, auth=auth, timeout=timeout)

    @allure.step("Retrieve a specific payment by ID")
    def fetch_payment_by_id(self, payment_id: int) -> "PaymentService":
        """
        Retrieve a specific payment by its ID.
        """
        logger.info("Fetching payment by ID: %s", payment_id)
        self.response = self.payment_controller.fetch_payment_by_id(payment_id)
        return self

    @allure.step("Delete a specific payment by ID")
    def remove_payment_by_id(self, payment_id: int) -> "PaymentService":
        """
        Delete a specific payment by its ID.
        """
        logger.info("Deleting payment by ID: %s", payment_id)
        self.response = self.payment_controller.remove_payment_by_id(payment_id)
        return self

    @allure.step("Retrieve all payments")
    def fetch_all_payments(self) -> "PaymentService":
        """
        Retrieve all payments in the system.
        """
        logger.info("Fetching all payments.")
        self.response = self.payments_controller.fetch_all_payments()
        return self

    @allure.step("Validate API response")
    def verify_that_response(self) -> ApiResponseValidator:
        """
        Provides a validator for the last API response.
        """
        if self.response is None:
            raise ValueError("No response available. Call one of the fetch/remove methods first.")
        return ApiResponseValidator(self.response)
