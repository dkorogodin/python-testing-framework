import base64
import json
from abc import ABC, abstractmethod
from dataclasses import asdict, is_dataclass

from pydantic import BaseModel
from wiremock.constants import Config
from wiremock.resources.mappings import Mapping
from wiremock.resources.mappings.resource import Mappings

from src import logger


class BaseMockService(ABC):
    """Abstract base class for all WireMock mock services."""

    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")

    @abstractmethod
    def stub_all_api(self):
        """Stub all endpoints for the service."""
        pass

    def _stub_request(
            self,
            method: str,
            url: str,
            body_obj: object,
            auth_header: str = None,
            auth_value: str = None,
            status: int = 200,
            match_type: str = "matches",  # supports "matches" and "doesNotMatch"
    ):
        """Generic helper for creating a WireMock mapping, supports token or basic auth."""
        headers = {}
        if auth_header and auth_value:
            headers[auth_header] = {match_type: auth_value}

        mapping = Mapping(
            request={
                "method": method,
                "url": url,
                "headers": headers
            },
            response={
                "status": status,
                "jsonBody": self.make_serializable(body_obj),
                "headers": {"Content-Type": "application/json"},
            }
        )
        self._create_mapping_for_server(mapping, self.base_url)
        logger.info(f"Stubbed {method} {url} {headers} (status={status})")

    def _create_mapping_for_server(self, mapping: Mapping, base_url: str):
        """Helper to create mapping for a specific base_url without affecting global Config."""
        old_base_url = Config.base_url
        try:
            Config.base_url = f"{base_url}/__admin"
            Mappings.create_mapping(mapping)
        finally:
            Config.base_url = old_base_url

    def _get_basic_auth_header(self, username: str, password: str) -> str:
        """Generate Basic Auth header value from credentials."""
        token = base64.b64encode(f"{username}:{password}".encode()).decode()
        return f"Basic {token}"

    def make_serializable(self, obj):
        if isinstance(obj, BaseModel):
            return json.loads(obj.model_dump_json())
        elif is_dataclass(obj):
            return json.loads(json.dumps(asdict(obj), default=str))
        else:
            return obj
