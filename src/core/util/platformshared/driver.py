from abc import ABC, abstractmethod

from selenium.webdriver import Remote


class Driver(ABC):
    """Abstract base class for drivers."""

    @abstractmethod
    def initiate_driver(self) -> Remote:
        pass
