from typing import cast

from src.core.api.service.auth.auth_service import AuthService
from src.core.api.service.auth.model.basic_auth import BasicAuth
from src.core.api.service.auth.model.token_auth import TokenAuth
from src.core.api.service.payment.payment_service import PaymentService
from src.core.api.service.product.product_service import ProductService
from src.core.data.configs.configs_manager import ConfigsManager
from src.core.data.factory.auth.auth.api_auth_factory import ApiAuthFactory
from src.core.data.factory.auth.auth.basic_auth_data_builder import BasicAuthDataBuilder
from src.core.data.factory.auth.auth.token_auth_api_data_builder import TokenAuthApiDataBuilder
from src.core.data.factory.auth.token.api_auth_token_factory import ApiAuthTokenFactory
from src.core.data.factory.auth.token.token_api_data_builder import TokenApiDataBuilder


class ApiMicroServiceManager:
    """
    Central manager for accessing API service instances.

    Provides convenient methods to obtain pre-configured service objects
    for authentication, payments, and products.
    """

    def __init__(self, configs_manager: ConfigsManager, base_url: str, timeout: int = 10):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

        web_configs = configs_manager.web_configs
        self.user_name = web_configs.web_username
        self.password = web_configs.web_password

    def get_payment_service(self) -> PaymentService:
        """
        Provides a pre-configured PaymentService instance with authentication token.
        """
        # Get token using the token factory
        token = TokenApiDataBuilder(base_url=self.base_url, username=self.user_name, password=self.password)
        token_auth = ApiAuthTokenFactory.get_token(token).token

        auth = cast(TokenAuth, ApiAuthFactory.get_api_auth(TokenAuthApiDataBuilder(token_auth)))
        return PaymentService(base_url=self.base_url, auth=auth, timeout=self.timeout)

    def get_product_service(self) -> ProductService:
        """
        Provides a pre-configured ProductService instance with basic authentication.
        """
        auth = cast(BasicAuth, ApiAuthFactory.get_api_auth(BasicAuthDataBuilder(self.user_name, self.password)))
        return ProductService(base_url=self.base_url, auth=auth, timeout=self.timeout)

    def get_auth_service(self) -> AuthService:
        """
        Provides a pre-configured AuthService instance.
        """
        return AuthService(base_url=self.base_url, timeout=self.timeout)
