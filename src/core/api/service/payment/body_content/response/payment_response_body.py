from src.core.api.core.model.api_response_item import ApiResponseItem
from src.core.api.service.payment.model.payment import Payment


class PaymentResponseBody(ApiResponseItem):
    """Response body for a single payment."""

    @staticmethod
    def expected_body_for_get_request(payment: Payment) -> "PaymentResponseBody":
        return PaymentResponseBody(
            data=payment,
            message="Payment Details fetched successfully."
        )

    @staticmethod
    def expected_body_for_delete_request(payment_id: int) -> "PaymentResponseBody":
        return PaymentResponseBody(
            message=f"Payment '{payment_id}' deleted successfully."
        )
