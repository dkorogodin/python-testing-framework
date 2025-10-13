import allure
from selenium.webdriver import Remote

from src.core.data.properties.web_properties import WebProperties
from src.core.web.driver.driver_cloud import DriverCloud
from src.core.web.driver.driver_local import DriverLocal
from src.core.web.driver.driver_remote import DriverRemote
from src.core.web.driver.driver_type import DriverType


class DriverFactory:
    """Factory to create WebDriver instances."""

    def __init__(self, properties: WebProperties):
        self.properties = properties

    @allure.step("Initiate Driver. Open browser.")
    def initiate_driver(self) -> Remote:
        driver_type = DriverType.from_property(
            self.properties.driver_type
        )

        if driver_type == DriverType.LOCAL:
            return DriverLocal(self.properties).initiate_driver()
        elif driver_type == DriverType.REMOTE:
            return DriverRemote(self.properties).initiate_driver()
        elif driver_type == DriverType.CLOUD:
            return DriverCloud(self.properties).initiate_driver()
        else:
            raise ValueError(f"Unknown driver type: {self.properties.driver_type}")
