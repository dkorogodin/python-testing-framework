from abc import ABC, abstractmethod


class AppiumService(ABC):

    def __init__(self):
        self.url = None

    @abstractmethod
    def setup(self):
        pass

    @abstractmethod
    def shutdown(self):
        pass

    def get_url(self) -> str:
        return self.url
