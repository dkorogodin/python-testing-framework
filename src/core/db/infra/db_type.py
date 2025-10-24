from enum import Enum
from typing import Optional


class DbType(Enum):
    LOCAL = "local"
    CONTAINER = "container"

    @staticmethod
    def from_property(value: Optional[str]) -> "DbType":
        try:
            return DbType(value.strip().lower())
        except Exception:
            return DbType.LOCAL
