from pathlib import Path
from typing import Optional

from src.core.data.configs.api_configs import ApiConfigs
from src.core.data.configs.db_configs import DbConfigs
from src.core.data.configs.mobile_configs import MobileConfigs
from src.core.data.configs.web_configs import WebConfigs
from src.core.util.system.config_loader_util import ConfigLoader


class ConfigsManager:
    """
    Central manager for loading API and Web configs.
    """

    def __init__(self, env: str = "dev", pytest_config=None):
        self.env = env
        self.pytest_config = pytest_config

        # src/core/data/configs/configs_manager.py
        self.project_root = Path(__file__).parents[4]
        self.config_path = self.project_root / "data" / "config" / self.env

        self._api_configs: Optional[ApiConfigs] = None
        self._web_configs: Optional[WebConfigs] = None
        self._mobile_configs: Optional[MobileConfigs] = None
        self._payments_db_configs: Optional[DbConfigs] = None
        self._products_db_configs: Optional[DbConfigs] = None

    @property
    def api_configs(self) -> ApiConfigs:
        if self._api_configs is None:
            path = self.config_path / "api_config.yaml"
            self._api_configs = ApiConfigs(ConfigLoader(path, self.pytest_config))
        return self._api_configs

    @property
    def web_configs(self) -> WebConfigs:
        if self._web_configs is None:
            path = self.config_path / "web_config.yaml"
            self._web_configs = WebConfigs(ConfigLoader(path, self.pytest_config))
        return self._web_configs

    @property
    def mobile_configs(self) -> MobileConfigs:
        if self._mobile_configs is None:
            path = self.config_path / "mobile_config.yaml"
            self._mobile_configs = MobileConfigs(ConfigLoader(path, self.pytest_config))
        return self._mobile_configs

    @property
    def payments_db_configs(self) -> DbConfigs:
        if self._payments_db_configs is None:
            path = self.config_path / "db" / "payments_db_config.yaml"
            self._payments_db_configs = DbConfigs(ConfigLoader(path, self.pytest_config))
        return self._payments_db_configs

    @property
    def products_db_configs(self) -> DbConfigs:
        if self._products_db_configs is None:
            path = self.config_path / "db" / "products_db_config.yaml"
            self._products_db_configs = DbConfigs(ConfigLoader(path, self.pytest_config))
        return self._products_db_configs
