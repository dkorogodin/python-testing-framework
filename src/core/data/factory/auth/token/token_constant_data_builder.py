from src.core.api.service.auth.model.token import Token
from src.core.data.factory.common.data_item import DataItem


class TokenConstantDataBuilder(DataItem):
    """
    Data builder for creating Token objects from constant values.
    """

    def __init__(self, username: str):
        self.username = username

    def get(self) -> Token:
        return Token(
            user_info=self.username,
            token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NzJiY2RiMmFlMmFmZDRjMGJiNTY3ZGIiLCJ1c2VyRW1haWwiOiJ0ZXN0ZXJfYXFhXzMzMUBtYWlsLmNvbSIsInVzZXJNb2JpbGUiOjEyMzQ1Njc4OTAsInVzZXJSb2xlIjoiY3VzdG9tZXIiLCJpYXQiOjE3MzE3MDQ4NTgsImV4cCI6MTc2MzI2MjQ1OH0._NuTReFymXhoYGyyRufc48XeC4vzi1HMNDdc-eMz_FA"
        )
