from enum import Enum
from typing import Optional


class DbType(Enum):
    DOCKER_COMPOSE = "dockercompose"
    TEST_CONTAINER = "testcontainer"

    @staticmethod
    def from_property(value: Optional[str]) -> "DbType":
        try:
            return DbType(value.strip().lower())
        except Exception:
            return DbType.DOCKER_COMPOSE
