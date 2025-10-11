from src.core.api.core.model.api_error import ApiError

# HTTP status code
HTTP_UNAUTHORIZED = 401


class AuthErrors:
    """Contains predefined authentication error responses for testing."""

    def __new__(cls, *args, **kwargs):
        raise TypeError("AuthErrors is a static class and cannot be instantiated.")

    UNAUTHORIZED_USER_ERR = ApiError(
        code=HTTP_UNAUTHORIZED,
        message="User unauthorized."
    )
