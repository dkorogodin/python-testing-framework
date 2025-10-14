from pathlib import Path
from typing import Optional, Callable, Any

from src.core.util.system.config_loader_util import ConfigLoader


class ApiConfigs:
    def __init__(self, file_path: Path, override_fn: Optional[Callable[[str], Any]] = None):
        self.loader = ConfigLoader(file_path, override_fn)
        self.mock_service = self.loader.get("mock.service")
