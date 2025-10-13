from http import HTTPStatus

import pytest

from src.core.api.mock.service.mock_payment_service import MockPaymentService
from src.core.api.service.payment.body_content.response.payment_errors import PaymentErrors
from src.core.api.service.payment.body_content.response.payment_response_body import PaymentResponseBody
from src.core.api.service.payment.body_content.response.payments_response_body import PaymentsResponseBody
from src.core.api.service.payment.payment_service import PaymentService
from src.core.data.factory.payment.payments_constant_data_builder import PaymentsConstantDataBuilder
from src.core.data.factory.payment.payments_factory import PaymentsFactory


@pytest.mark.api
@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.payment
class TestApiPayment:
    @pytest.fixture
    def payment_service(self, api_service_manager) -> PaymentService:
        return api_service_manager.get_payment_service()

    def test_get_payment(self, payment_service):
        random_payment = PaymentsFactory.get_random(PaymentsConstantDataBuilder())
        expected_payment = PaymentResponseBody.expected_body_for_get_request(random_payment)

        (payment_service
         .fetch_payment_by_id(random_payment.id)
         .verify_that_response()
         .status_code_is_equal_to(HTTPStatus.OK)
         .body_is_equal_to(expected_payment))

    def test_delete_payment(self, payment_service):
        payment_id = MockPaymentService.DELETED_PAYMENT_ID

        expected_payment = PaymentResponseBody.expected_body_for_delete_request(payment_id)
        (payment_service
         .remove_payment_by_id(payment_id)
         .verify_that_response()
         .status_code_is_equal_to(HTTPStatus.OK)
         .body_is_equal_to(expected_payment))

        expected_error = PaymentErrors.non_existing_payment_err(payment_id)
        (payment_service
         .fetch_payment_by_id(payment_id)
         .verify_that_response()
         .status_code_is_equal_to(HTTPStatus.OK)
         .body_is_equal_to(expected_error))

    def test_get_all_payments(self, payment_service):
        expected_payments = PaymentsResponseBody.expected_body_for_get_request(
            PaymentsFactory.get_all(PaymentsConstantDataBuilder())
        )

        (payment_service
         .fetch_all_payments()
         .verify_that_response()
         .status_code_is_equal_to(HTTPStatus.OK)
         .body_is_equal_to(expected_payments))
