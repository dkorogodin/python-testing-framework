from typing import List

from src.core.api.core.model.api_response_list import ApiResponseList
from src.core.api.service.payment.model.payment import Payment


class PaymentsResponseBody(ApiResponseList):
    """Response body for multiple payments."""

    @staticmethod
    def expected_body_for_get_request(expected_payments: List[Payment]) -> "PaymentsResponseBody":
        return PaymentsResponseBody(
            data=expected_payments or [],
            count=len(expected_payments) if expected_payments else 0,
            message="All Payments fetched successfully."
        )
