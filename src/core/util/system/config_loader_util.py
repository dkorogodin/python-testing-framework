import os
from pathlib import Path
from typing import Any, Callable, Optional

import yaml


class ConfigLoader:
    """
    Loads configuration values from:
      1. Environment variables
      2. Pytest CLI options
      3. YAML file defaults
    """

    def __init__(self, yaml_path: Path, override_fn: Optional[Callable[[str], Any]] = None):
        self.yaml_path = yaml_path
        self.override_fn = override_fn
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
        env_key = key.replace(".", "_").upper()  # e.g., browser.name -> BROWSER_NAME
        if env_key in os.environ:
            return os.environ[env_key]

        if self.override_fn:
            cli_value = self.override_fn(key)
            if cli_value is not None:
                return cli_value

        parts = key.split(".")
        value = self._config
        try:
            for part in parts:
                value = value[part]
            return value
        except (KeyError, TypeError):
            return default


# ---------- Pytest CLI integration ----------

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default=None)
    parser.addoption("--driver_type", action="store", default=None)
    parser.addoption("--app_baseurl", action="store", default=None)
    parser.addoption("--app_username", action="store", default=None)
    parser.addoption("--app_password", action="store", default=None)
    parser.addoption("--mock_service", action="store", default=None)


def get_cli_option(key: str):
    """
    Maps config keys to pytest CLI options
    """
    from _pytest.config import get_config
    config = get_config()
    cli_key = key.replace(".", "_")
    return config.getoption(f"--{cli_key}")
