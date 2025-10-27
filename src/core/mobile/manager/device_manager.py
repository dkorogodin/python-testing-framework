from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import WebDriverException

from src import logger
from src.core.mobile.data.enums.mobile_orientation import MobileOrientation


class DeviceManager:
    """
    Manages device-level operations such as lock/unlock, location, orientation, and device time.

    Supports Android and iOS devices using Appium.
    """

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # ----------------------------
    # Lock / Unlock
    # ----------------------------

    def lock_device(self, seconds: int = 5):
        """Locks the device for a specified duration."""
        logger.info(f"Locking device for {seconds} seconds.")
        try:
            self.driver.lock(seconds)
        except WebDriverException as e:
            logger.warning(f"Driver does not support device locking: {e}")

    def unlock_device(self):
        """Unlocks the device."""
        logger.info("Unlocking device.")
        try:
            self.driver.unlock()
        except WebDriverException as e:
            logger.warning(f"Driver does not support device unlocking: {e}")

    def is_device_locked(self) -> bool:
        """Returns True if device is locked, False otherwise."""
        logger.info("Checking if device is locked.")
        try:
            return self.driver.is_locked()
        except WebDriverException as e:
            logger.warning(f"Driver does not support lock status check: {e}")
            return False

    # ----------------------------
    # Device Time
    # ----------------------------

    def get_device_time(self) -> str:
        """Returns the device time as a string."""
        logger.info("Getting device time.")
        try:
            return self.driver.device_time
        except WebDriverException as e:
            logger.warning(f"Driver does not support getting device time: {e}")
            return ""

    # ----------------------------
    # Location
    # ----------------------------

    def get_location(self) -> dict[str, float] | None:
        """Returns the device location."""
        logger.info("Getting device location.")
        try:
            return self.driver.location
        except WebDriverException as e:
            logger.warning(f"Driver does not support getting location: {e}")
            return None

    def set_location(self, latitude: float, longitude: float, altitude: float = 0.0):
        """Sets the device location."""
        logger.info(f"Setting device location to ({latitude}, {longitude}, {altitude})")
        try:
            self.driver.set_location(latitude, longitude, altitude)
        except WebDriverException as e:
            logger.warning(f"Driver does not support setting location: {e}")

    # ----------------------------
    # Orientation
    # ----------------------------

    def get_screen_orientation(self) -> str:
        """Returns the current screen orientation."""
        logger.info("Getting screen orientation.")
        try:
            return self.driver.orientation
        except WebDriverException as e:
            logger.warning(f"Driver does not support getting screen orientation: {e}")
            return "UNKNOWN"

    def set_screen_orientation(self, orientation: MobileOrientation):
        """Sets the screen orientation (PORTRAIT or LANDSCAPE)."""
        logger.info(f"Setting screen orientation to {orientation}.")
        try:
            self.driver.orientation = orientation.value
        except WebDriverException as e:
            logger.warning(f"Driver does not support setting screen orientation: {e}")

    # ----------------------------
    # Reset State
    # ----------------------------

    def reset_device_state(self):
        """Resets device state to default orientation and location."""
        logger.info("Resetting device state to default.")
        try:
            self.set_screen_orientation(MobileOrientation.PORTRAIT)
            self.set_location(0, 0, 0)
        except Exception as e:
            logger.warning(f"Failed to reset device state: {e}")
