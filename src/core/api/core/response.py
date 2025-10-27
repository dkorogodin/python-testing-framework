import json
from typing import Any, Optional

import requests

from src import logger


class ApiResponse:
    """
    Wrapper for HTTP responses with utility methods
    for accessing status, JSON body, and nested fields.
    All operations are logged via the central logger.
    """

    def __init__(self, response: requests.Response):
        self.response = response
        logger.debug("ApiResponse initialized with status code: %s", self.response.status_code)

    def get_status_code(self) -> int:
        code = self.response.status_code
        logger.debug("Response status code: %s", code)
        return code

    def get_text(self) -> str:
        text = self.response.text
        logger.debug("Response text length: %d characters", len(text))
        return text

    def get_json(self) -> Any:
        try:
            data = self.response.json()
            logger.debug("Parsed JSON response successfully")
            return data
        except json.JSONDecodeError:
            logger.error("Response body is not valid JSON: %s", self.response.text)
            raise ValueError("Response body is not valid JSON")

    def get_field(self, path: str) -> Optional[Any]:
        """
        Retrieve a nested field from JSON body using dot notation.
        Example: path="data.user.id"
        """
        logger.debug("Retrieving field '%s' from response JSON", path)
        data = self.get_json()
        for key in path.split('.'):
            if isinstance(data, dict) and key in data:
                data = data[key]
            else:
                logger.error("Field '%s' not found in response body", path)
                raise KeyError(f"Field '{path}' not found in response body")
        logger.debug("Field '%s' value: %s", path, data)
        return data

    def get_fields(self, path: str) -> list[Any]:
        logger.debug("Retrieving list field '%s'", path)
        field = self.get_field(path)
        if not isinstance(field, list):
            logger.error("Expected list at '%s', but got %s", path, type(field).__name__)
            raise TypeError(f"Expected list at '{path}', but got {type(field).__name__}")
        logger.debug("Retrieved list at '%s': %s", path, field)
        return field

    def pretty_print(self):
        """
        Pretty print JSON response for debugging.
        """
        try:
            pretty = json.dumps(self.get_json(), indent=2)
            print(pretty)
            logger.debug("Pretty printed response successfully")
        except Exception:
            text = self.get_text()
            print(text)
            logger.warning("Failed to pretty print response; falling back to raw text. Length: %d chars", len(text))
