from enum import Enum


class AppiumServiceType(str, Enum):
    LOCAL = "LOCAL"
    CONTAINER = "CONTAINER"

    @staticmethod
    def from_property(value: str) -> "AppiumServiceType":
        try:
            return AppiumServiceType(value.strip().upper())
        except (ValueError, AttributeError):
            return AppiumServiceType.LOCAL
