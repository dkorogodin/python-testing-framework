from enum import Enum
from typing import Optional


class WireMockServiceType(Enum):
    LOCAL = "local"
    TEST_CONTAINER = "testcontainer"

    @staticmethod
    def from_property(value: Optional[str]) -> "WireMockServiceType":
        try:
            return WireMockServiceType(value.strip().lower())
        except Exception:
            return WireMockServiceType.LOCAL
