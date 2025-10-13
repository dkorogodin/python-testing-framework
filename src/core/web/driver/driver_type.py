from enum import Enum
from typing import Optional


class DriverType(Enum):
    LOCAL = "local"
    REMOTE = "remote"
    CLOUD = "cloud"

    @staticmethod
    def from_property(value: Optional[str]) -> "DriverType":
        try:
            return DriverType(value.strip().lower())
        except Exception:
            return DriverType.LOCAL
