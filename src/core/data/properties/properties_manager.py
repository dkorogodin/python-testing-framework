import os
from pathlib import Path
from typing import Optional, Callable, Any

from src.core.data.properties.api_properties import ApiProperties
from src.core.data.properties.web_properties import WebProperties


class PropertiesManager:
    """
    Central manager for loading API and Web properties with three-layer resolution.
    """

    def __init__(self, env: str = "dev", override_fn: Optional[Callable[[str], Any]] = None):
        self.env = env
        self.override_fn = override_fn

        # src/core/data/properties/properties_manager.py
        self.project_root = Path(__file__).parent.parent.parent.parent.parent
        self._api_properties: Optional[ApiProperties] = None
        self._web_properties: Optional[WebProperties] = None

    @property
    def api_properties(self) -> ApiProperties:
        if self._api_properties is None:
            path = self.project_root / "config" / self.env / "api_config.yaml"
            self._api_properties = ApiProperties(path, self.override_fn)
        return self._api_properties

    @property
    def web_properties(self) -> WebProperties:
        if self._web_properties is None:
            path = self.project_root / "config" / self.env / "web_config.yaml"
            self._web_properties = WebProperties(path, self.override_fn)
        return self._web_properties
