import datetime
import json
from dataclasses import is_dataclass, asdict
from typing import Any, List

import allure
from deepdiff import DeepDiff
from pydantic import BaseModel

from src import logger


class ApiResponseValidator:
    """
    Provides fluent validation for ApiResponse.
    Integrates with Allure steps and uses native pytest assertions.
    Logs all validations via the central logger.
    """

    def __init__(self, response):
        self.response = response
        logger.debug(
            "ApiResponseValidator initialized for response with status %s",
            getattr(self.response, 'get_status_code', lambda: 'unknown')()
        )

    @allure.step("Verify that status code is equal to {expected_status}")
    def status_code_is_equal_to(self, expected_status: int) -> "ApiResponseValidator":
        actual_status = self.response.get_status_code()
        logger.info("Validating status code: expected=%s, actual=%s", expected_status, actual_status)
        assert actual_status == expected_status, f"Expected status code {expected_status}, but got {actual_status}"
        return self

    def and_(self) -> "ApiResponseValidator":
        return self

    @allure.step("Verify that response body is equal to expected object")
    def body_is_equal_to(self, expected_body: Any) -> "ApiResponseValidator":
        actual_body = self.response.response.json()
        diff = DeepDiff(self.make_serializable(expected_body.dict()), actual_body, ignore_order=True)
        if diff:
            logger.error("Response body mismatch:\n%s", diff.pretty())
        else:
            logger.debug("Response body matches expected object")
        assert not diff, f"Body mismatch:\n{diff.pretty()}"
        return self

    @allure.step("Verify that field {path} is equal to expected value")
    def body_field_is_equal_to(self, expected_value: Any, path: str) -> "ApiResponseValidator":
        actual_value = self.response.get_field(path)
        logger.info("Validating field '%s': expected=%s, actual=%s", path, expected_value, actual_value)
        assert actual_value == expected_value, f"Expected {path} = {expected_value}, but got {actual_value}"
        return self

    @allure.step("Verify that field {path} is not empty")
    def body_field_is_not_empty(self, path: str) -> "ApiResponseValidator":
        actual_value = self.response.get_field(path)
        logger.info("Validating non-empty field '%s': value=%s", path, actual_value)
        assert (actual_value is not None and str(actual_value).strip()), \
            f"Expected field '{path}' to be non-empty, but got '{actual_value}'"
        return self

    @allure.step("Verify that list at {path} equals expected items")
    def body_list_is_equal_to(self, expected_items: List[Any], path: str) -> "ApiResponseValidator":
        actual_items = self.response.get_fields(path)
        diff = DeepDiff(self.make_serializable(expected_items.dict()), actual_items, ignore_order=True)
        if diff:
            logger.error("List mismatch at '%s':\n%s", path, diff.pretty())
        else:
            logger.debug("List at '%s' matches expected items", path)
        assert not diff, f"List mismatch at {path}:\n{diff.pretty()}"
        return self

    @allure.step("Verify that list at {path} contains expected items")
    def body_list_contains(self, expected_items: List[Any], path: str) -> "ApiResponseValidator":
        actual_items = self.response.get_fields(path)
        missing_items = [item for item in expected_items if item not in actual_items]
        if missing_items:
            logger.error("Missing expected items in '%s': %s", path, missing_items)
        else:
            logger.debug("All expected items found in list at '%s'", path)
        assert not missing_items, f"Missing expected items in {path}: {missing_items}"
        return self

    def make_serializable(self, obj):
        if isinstance(obj, dict):
            return {k: self.make_serializable(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [self.make_serializable(v) for v in obj]
        elif isinstance(obj, datetime.date):
            return obj.isoformat()
        else:
            return obj
