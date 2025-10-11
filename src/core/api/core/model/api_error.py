from pydantic import BaseModel


class ApiError(BaseModel):
    code: int
    message: str
