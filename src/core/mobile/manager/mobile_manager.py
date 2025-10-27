from typing import Optional

from appium.webdriver.webdriver import WebDriver

from src import logger
from src.core.data.configs.mobile_configs import MobileConfigs
from src.core.mobile.driver.driver_factory import DriverFactory
from src.core.mobile.manager.device_manager import DeviceManager
from src.core.mobile.manager.mobile_app_lifecycle import MobileAppLifecycle


class MobileManager:
    """
    High-level manager that coordinates driver, device, and application lifecycles.

    Provides access to:
      - Appium WebDriver
      - MobileAppLifecycle
      - DeviceManager
    """

    def __init__(self, configs: MobileConfigs):
        self.configs = configs
        self._driver = None
        self._app: Optional[MobileAppLifecycle] = None
        self._device: Optional[DeviceManager] = None

    def get_driver(self) -> WebDriver:
        """Returns the Appium WebDriver, initializing it if necessary."""
        if self._driver is None:
            self._driver = DriverFactory(self.configs).initiate_driver()
        return self._driver

    def get_app(self) -> MobileAppLifecycle:
        """Returns the MobileAppLifecycle manager, initializing it if necessary."""
        if self._app is None:
            logger.info("Initializing MobileAppLifecycle manager...")
            driver = self.get_driver()
            self._app = MobileAppLifecycle(driver, self.configs.is_cloud)
        return self._app

    def get_device(self) -> DeviceManager:
        """Returns the DeviceManager, initializing it if necessary."""
        if self._device is None:
            logger.info("Initializing DeviceManager...")
            driver = self.get_driver()
            self._device = DeviceManager(driver)
        return self._device

    def full_mobile_cleanup(self, app_id: str):
        """Performs full cleanup of app and device, and quits the Appium WebDriver."""
        logger.info(f"Performing full cleanup for app '{app_id}'...")
        try:
            if self._app:
                self._app.uninstall_app(app_id)
            if self._device:
                self._device.reset_device_state()
        finally:
            self.quit()

    def quit(self):
        """Quits the Appium WebDriver and clears all references."""
        if self._driver:
            logger.info("Quitting Appium WebDriver...")
            try:
                self._driver.quit()
            except Exception as e:
                logger.warning(f"Error during Appium WebDriver quit: {e}")
            finally:
                self._driver = None
                self._app = None
                self._device = None
                logger.info("Appium WebDriver and managers cleaned up.")
