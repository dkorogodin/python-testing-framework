from abc import ABC, abstractmethod

from src.core.data.configs.web_configs import WebConfigs


class SeleniumGridService(ABC):

    def __init__(self, web_configs: WebConfigs):
        self.web_configs = web_configs
        self.setup()

    @abstractmethod
    def setup(self):
        pass

    @abstractmethod
    def shutdown(self):
        pass
