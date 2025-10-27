from enum import Enum
from typing import Optional


class MobilePlatform(Enum):
    ANDROID = "android"
    IOS = "ios"

    @property
    def appium_name(self) -> str:
        """Returns the correct Appium platform name."""
        return self.value.capitalize()

    @staticmethod
    def from_property(value: Optional[str]) -> "MobilePlatform":
        try:
            return MobilePlatform(value.strip().lower())
        except Exception:
            raise ValueError(f"Incorrect platform provided: {value}")
