from pydantic import BaseModel


class Token(BaseModel):
    """Represents an authentication token for a user."""
    user_info: str
    token: str
    message: str = "User successfully logged in. Token Generated"
