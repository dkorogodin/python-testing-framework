from typing import Any, Dict

from pydantic import BaseModel


class Gesture(BaseModel):
    """Base class for all gestures."""

    model_config = {"arbitrary_types_allowed": True}

    def get_supported_arguments(self) -> Dict[str, Any]:
        """Returns a map of arguments supported by this gesture."""
        data = self.model_dump(exclude_none=True)
        return data
