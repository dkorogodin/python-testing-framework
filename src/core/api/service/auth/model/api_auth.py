from pydantic import BaseModel


class ApiAuth(BaseModel):
    """Abstract base class for authentication strategies."""
    pass
