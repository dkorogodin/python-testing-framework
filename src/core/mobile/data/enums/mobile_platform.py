from enum import Enum
from typing import Optional


class MobilePlatform(Enum):
    ANDROID = "android"
    IOS = "ios"

    @staticmethod
    def from_property(value: Optional[str]) -> "MobilePlatform":
        try:
            return MobilePlatform(value.strip().lower())
        except Exception:
            raise ValueError(f"Incorrect platform provided: {value}")
