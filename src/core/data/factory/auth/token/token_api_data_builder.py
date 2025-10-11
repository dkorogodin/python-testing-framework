from src.core.api.service.auth.auth_service import AuthService
from src.core.api.service.auth.model.basic_auth import BasicAuth
from src.core.api.service.auth.model.token import Token
from src.core.data.factory.common.data_item import DataItem


class TokenApiDataBuilder(DataItem):
    """
    Data builder for creating Token objects via API authentication.
    """

    def __init__(self, base_url: str, username: str, password: str):
        self.base_url = base_url
        self.username = username
        self.password = password

    def get(self) -> Token:
        auth_service = AuthService(self.base_url)
        response = auth_service.login(BasicAuth(username=self.username, password=self.password)).response
        data = response.get_json()
        return Token(**data)
