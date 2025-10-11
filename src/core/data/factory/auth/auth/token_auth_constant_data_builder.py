from src import logger
from src.core.api.service.auth.model.token_auth import TokenAuth
from src.core.data.factory.common.data_item import DataItem


class TokenAuthConstantDataBuilder(DataItem):
    """
    Data builder for creating TokenAuth objects from constant tokens.
    """

    def __init__(self, token: str):
        self.token = token

    def get(self) -> TokenAuth:
        bearer_token = f"Bearer {self.token}"
        logger.info("Returning TokenAuth from constants with token '%s'.", bearer_token)
        return TokenAuth(token=bearer_token, header="Authorization")
