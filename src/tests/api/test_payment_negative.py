# test_payment_negative.py
from http import HTTPStatus

import pytest

from src.core.api.service.auth.body_content.response.auth_errors import AuthErrors
from src.core.api.service.payment.payment_service import PaymentService
from src.core.data.factory.payment.payments_constant_data_builder import PaymentsConstantDataBuilder
from src.core.data.factory.payment.payments_factory import PaymentsFactory

NON_EXISTING_TOKEN = "non existing token"


@pytest.fixture
def payment_service(api_service_manager) -> PaymentService:
    return api_service_manager.get_payment_service()


def test_get_all_payments_non_existing_token(payment_service):
    payment_service.auth.set_token(NON_EXISTING_TOKEN)

    (payment_service
     .fetch_all_payments()
     .verify_that_response()
     .status_code_is_equal_to(HTTPStatus.UNAUTHORIZED)
     .body_is_equal_to(AuthErrors.UNAUTHORIZED_USER_ERR))


def test_get_payment_non_existing_token(payment_service):
    random_payment = PaymentsFactory.get_random(PaymentsConstantDataBuilder())
    payment_service.auth.set_token(NON_EXISTING_TOKEN)

    (payment_service
     .fetch_payment_by_id(random_payment.id)
     .verify_that_response()
     .status_code_is_equal_to(HTTPStatus.UNAUTHORIZED)
     .body_is_equal_to(AuthErrors.UNAUTHORIZED_USER_ERR))
