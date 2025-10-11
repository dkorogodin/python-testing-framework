from typing import Optional, Any

from pydantic import BaseModel


class ApiResponseItem(BaseModel):
    data: Optional[Any] = None
    message: Optional[str] = None
