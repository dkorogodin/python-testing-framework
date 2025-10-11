from src.core.api.mock.service.base_mock_service import BaseMockService
from src.core.api.service.auth.body_content.response.auth_errors import AuthErrors
from src.core.api.service.auth.model.token_auth import TokenAuth
from src.core.api.service.payment.body_content.response.payment_errors import PaymentErrors
from src.core.api.service.payment.body_content.response.payment_response_body import PaymentResponseBody
from src.core.api.service.payment.body_content.response.payments_response_body import PaymentsResponseBody
from src.core.api.service.payment.controller.payment_controller import PaymentController
from src.core.api.service.payment.controller.payments_controller import PaymentsController
from src.core.data.factory.payment.payments_constant_data_builder import PaymentsConstantDataBuilder
from src.core.data.factory.payment.payments_factory import PaymentsFactory


class MockPaymentService(BaseMockService):
    DELETED_PAYMENT_ID = 10

    def __init__(self, base_url: str, token: TokenAuth):
        super().__init__(base_url)
        self.token = token
        self.all_payments = PaymentsFactory.get_all(PaymentsConstantDataBuilder())

    def stub_all_api(self):
        self._stub_get_all_payments()
        self._stub_get_all_payments_unauthorized()
        self._stub_get_payment()
        self._stub_get_payment_unauthorized()
        self._stub_delete_payment()
        self._stub_non_existing_payment()

    def _stub_get_all_payments(self):
        self._stub_request(
            "GET",
            PaymentsController.PAYMENTS_ENDPOINT,
            PaymentsResponseBody.expected_body_for_get_request(self.all_payments),
            auth_header=self.token.header,
            auth_value=self.token.token
        )

    def _stub_get_all_payments_unauthorized(self):
        self._stub_request(
            "GET",
            PaymentsController.PAYMENTS_ENDPOINT,
            AuthErrors.UNAUTHORIZED_USER_ERR,
            auth_header=self.token.header,
            auth_value=self.token.token,
            match_type="doesNotMatch",
            status=401
        )

    def _stub_get_payment(self):
        for payment in self.all_payments:
            self._stub_request(
                "GET",
                f"{PaymentController.PAYMENT_ENDPOINT}/{payment.id}",
                PaymentResponseBody.expected_body_for_get_request(payment),
                auth_header=self.token.header,
                auth_value=self.token.token,
                match_type="matches"
            )

    def _stub_get_payment_unauthorized(self):
        for payment in self.all_payments:
            self._stub_request(
                "GET",
                f"{PaymentController.PAYMENT_ENDPOINT}/{payment.id}",
                AuthErrors.UNAUTHORIZED_USER_ERR,
                auth_header=self.token.header,
                auth_value=self.token.token,
                match_type="doesNotMatch",
                status=401
            )

    def _stub_non_existing_payment(self):
        self._stub_request(
            "GET",
            f"{PaymentController.PAYMENT_ENDPOINT}/{self.DELETED_PAYMENT_ID}",
            PaymentErrors.non_existing_payment_err(self.DELETED_PAYMENT_ID),
            auth_header=self.token.header,
            auth_value=self.token.token
        )

    def _stub_delete_payment(self):
        self._stub_request(
            "DELETE",
            f"{PaymentController.PAYMENT_ENDPOINT}/{self.DELETED_PAYMENT_ID}",
            PaymentResponseBody.expected_body_for_delete_request(self.DELETED_PAYMENT_ID),
            auth_header=self.token.header,
            auth_value=self.token.token
        )
