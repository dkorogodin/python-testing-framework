from enum import Enum
from typing import Optional


class SeleniumGridType(Enum):
    DOCKER_COMPOSE = "dockercompose"
    TEST_CONTAINER = "testcontainer"

    @staticmethod
    def from_property(value: Optional[str]) -> "SeleniumGridType":
        try:
            return SeleniumGridType(value.strip().lower())
        except Exception:
            return SeleniumGridType.DOCKER_COMPOSE
