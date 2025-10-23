from src.core.util.system.config_loader_util import ConfigLoader


class ApiConfigs:

    def __init__(self, loader: ConfigLoader):
        self.loader = loader
        self.mock_service = self.loader.get("mock.service")
