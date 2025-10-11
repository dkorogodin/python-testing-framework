from src import logger
from src.core.api.service.auth.model.basic_auth import BasicAuth
from src.core.data.factory.common.data_item import DataItem


class BasicAuthDataBuilder(DataItem):
    """
    Data builder for creating BasicAuth authentication objects.
    """

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def get(self) -> BasicAuth:
        logger.info("Returning BasicAuth with username: '%s' and password: '%s'", self.username, self.password)
        return BasicAuth(username=self.username, password=self.password)
