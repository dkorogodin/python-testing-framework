import allure
from selenium.webdriver import Remote

from src.core.data.configs.web_configs import WebConfigs
from src.core.web.driver.driver_cloud import DriverCloud
from src.core.web.driver.driver_local import DriverLocal
from src.core.web.driver.driver_remote import DriverRemote
from src.core.web.driver.driver_type import DriverType


class DriverFactory:
    """Factory to create WebDriver instances."""

    def __init__(self, configs: WebConfigs):
        self.configs = configs

    @allure.step("Initiate Driver. Open browser.")
    def initiate_driver(self) -> Remote:
        driver_type = DriverType.from_property(
            self.configs.driver_type
        )

        if driver_type == DriverType.LOCAL:
            return DriverLocal(self.configs).initiate_driver()
        elif driver_type == DriverType.REMOTE:
            return DriverRemote(self.configs).initiate_driver()
        elif driver_type == DriverType.CLOUD:
            return DriverCloud(self.configs).initiate_driver()
        else:
            raise ValueError(f"Unknown driver type: {self.configs.driver_type}")
