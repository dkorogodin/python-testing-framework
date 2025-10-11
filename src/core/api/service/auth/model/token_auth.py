from src.core.api.service.auth.model.api_auth import ApiAuth


class TokenAuth(ApiAuth):
    """Token-based authentication credentials."""
    token: str
    header: str = "Authorization"

    def set_token(self, new_token: str):
        """Update the token value at runtime."""
        self.token = new_token
