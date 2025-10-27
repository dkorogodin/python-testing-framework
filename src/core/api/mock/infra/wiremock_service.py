from abc import ABC, abstractmethod
from typing import List
from typing import cast

from src import logger
from src.core.api.mock.service.mock_auth_service import MockAuthService
from src.core.api.mock.service.mock_payment_service import MockPaymentService
from src.core.api.mock.service.mock_product_service import MockProductService
from src.core.api.service.auth.model.basic_auth import BasicAuth
from src.core.api.service.auth.model.token_auth import TokenAuth
from src.core.data.configs.configs_manager import ConfigsManager
from src.core.data.factory.auth.auth.api_auth_factory import ApiAuthFactory
from src.core.data.factory.auth.auth.basic_auth_data_builder import BasicAuthDataBuilder
from src.core.data.factory.auth.auth.token_auth_constant_data_builder import TokenAuthConstantDataBuilder
from src.core.data.factory.auth.token.api_auth_token_factory import ApiAuthTokenFactory
from src.core.data.factory.auth.token.token_constant_data_builder import TokenConstantDataBuilder


class WireMockService(ABC):
    """ Base class for WireMock services (local or containerized). Manages server lifecycle and initialization of mock endpoints. """

    def __init__(self, configs_manager: ConfigsManager):
        self.configs_manager = configs_manager
        self.mock_services: List = []
        self.server = None
        self.url = None

    @abstractmethod
    def start_wiremock(self):
        """Start the WireMock server."""
        pass

    @abstractmethod
    def stop_wiremock(self):
        """Stop the WireMock server."""
        pass

    @abstractmethod
    def get_base_url(self) -> str:
        """Return the WireMock base URL."""
        pass

    def start(self):
        logger.info("Starting WireMock service...")
        self.start_wiremock()
        self.url = self.get_base_url()
        logger.info(f"WireMock started at {self.url}")
        self._collect_all_mock_services()
        self._start_all_mock_services()

    def shutdown(self):
        logger.info("Stopping WireMock service...")
        self.stop_wiremock()
        logger.info("WireMock stopped.")

    def get_url(self) -> str:
        return self.url

    def _collect_all_mock_services(self):
        username = self.configs_manager.web_configs.web_username
        password = self.configs_manager.web_configs.web_password

        auth_service = MockAuthService(self.url, username)

        basic_auth = cast(BasicAuth, ApiAuthFactory.get_api_auth(BasicAuthDataBuilder(username, password)))
        product_service = MockProductService(self.url, basic_auth)

        token = TokenAuthConstantDataBuilder(ApiAuthTokenFactory.get_token(TokenConstantDataBuilder(username)).token)
        token_auth = cast(TokenAuth, ApiAuthFactory.get_api_auth(token))
        payment_service = MockPaymentService(self.url, token_auth)

        self.mock_services = [auth_service, payment_service, product_service]

    def _start_all_mock_services(self):
        logger.info("Initializing WireMock stubs...")
        for service in self.mock_services:
            service.stub_all_api()
            names = [s.__class__.__name__ for s in self.mock_services]
            logger.info(f"Initialized mock services: {names}")
