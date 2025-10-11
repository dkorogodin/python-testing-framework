from src.core.api.core.model.api_error import ApiError


class PaymentErrors:
    """Predefined payment-related error responses."""

    @staticmethod
    def non_existing_payment_err(payment_id: int) -> ApiError:
        return ApiError(
            code=400,  # BAD_REQUEST
            message=f"Payment with id='{payment_id}' does not exist."
        )
