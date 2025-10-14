from pathlib import Path
from typing import Optional, Callable, Any

from src.core.util.system.config_loader_util import ConfigLoader


class DbConfigs:
    def __init__(self, file_path: Path, override_fn: Optional[Callable[[str], Any]] = None):
        self.loader = ConfigLoader(file_path, override_fn)
        self.db_name = self.loader.get("db.name")
        self.db_username = self.loader.get("db.username")
        self.db_password = self.loader.get("db.password")
