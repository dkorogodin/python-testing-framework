import os
from pathlib import Path
from typing import Any, Optional

import yaml


class ConfigLoader:
    """
    Loads configuration values from:
      1. Environment variables
      2. Pytest CLI options
      3. YAML file defaults
    """

    def __init__(self, yaml_path: Path, pytest_config=None):
        self.yaml_path = yaml_path
        self.pytest_config = pytest_config
        self._config = self._load_yaml()

    def _load_yaml(self) -> dict:
        if not self.yaml_path.exists():
            raise FileNotFoundError(f"Config file not found: {self.yaml_path}")
        with open(self.yaml_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}

    def get(self, key: str, default: Any = None):
        """
        Resolve config key with priority:
        ENV VAR -> CLI override -> YAML -> default
        key format: browser.name, driver.type, etc.
        """

        env_value = self._get_from_env_variables(key)
        if env_value is not None:
            return env_value

        cli_value = self._get_from_pytest_cli(key)
        if cli_value is not None:
            return cli_value

        return self._get_from_yaml(key, default)

    def _get_from_env_variables(self, key: str):
        env_key = key.replace(".", "_").upper()
        return os.environ.get(env_key)

    def _get_from_pytest_cli(self, key: str) -> Optional[str]:
        if self.pytest_config is None:
            return None
        cli_key = key.replace(".", "_")
        if hasattr(self.pytest_config.option, cli_key):
            return getattr(self.pytest_config.option, cli_key)
        return None

    def _get_from_yaml(self, key: str, default: Any = None):
        value = self._config
        for part in key.split("."):
            if isinstance(value, dict) and part in value:
                value = value[part]
            else:
                return default
        return value
