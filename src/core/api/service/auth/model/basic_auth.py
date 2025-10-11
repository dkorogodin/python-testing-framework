from src.core.api.service.auth.model.api_auth import ApiAuth


class BasicAuth(ApiAuth):
    """Basic authentication credentials."""
    username: str
    password: str
