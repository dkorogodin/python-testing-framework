from enum import Enum
from typing import Optional


class SeleniumGridType(Enum):
    LOCAL = "local"
    CONTAINER = "container"

    @staticmethod
    def from_property(value: Optional[str]) -> "SeleniumGridType":
        try:
            return SeleniumGridType(value.strip().lower())
        except Exception:
            return SeleniumGridType.LOCAL
