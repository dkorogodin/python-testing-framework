from typing import List, Optional, Any

from pydantic import BaseModel, Field


class ApiResponseList(BaseModel):
    data: List[Any] = Field(default_factory=list)
    count: int = 0
    message: Optional[str] = None
