from src import logger
from src.core.api.service.auth.model.token import Token
from src.core.data.factory.common.data_item import DataItem


class ApiAuthTokenFactory:
    """
    Factory for retrieving Token authentication objects.
    """

    @staticmethod
    def get_token(token_data: DataItem) -> Token | None:
        """
        Retrieves a Token instance from the given data builder.
        """
        token = token_data.get()
        if token is None:
            logger.warning("AuthFactory returned None Token.")
        else:
            logger.info("Fetched Token: '%s'", token)
        return token
