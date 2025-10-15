from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver

from src import logger
from src.core.mobile.data.enums.mobile_platform import MobilePlatform


class KeyboardActions:
    """
    Provides methods to interact with mobile keyboards on Android and iOS devices.

    Includes pressing keys, hiding the keyboard, and checking its visibility.
    """

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def press_key(self, key: str):
        """Presses a key using its accessibility id."""
        logger.info(f"Pressing '{key}' key.")
        try:
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, key).click()
        except Exception as e:
            logger.warning(f"Could not press key '{key}': {e}")

    def press_android_key(self, key: int):
        """
        Presses a hardware Android key.
        Raises NotImplementedError if driver is not Android.
        """
        if self.driver.capabilities.get("platformName", "").lower() != MobilePlatform.ANDROID.value.lower():
            raise NotImplementedError("press_android_key is only supported on Android.")
        try:
            logger.info(f"Pressing '{key}' Android key.")
            self.driver.press_keycode(key)
        except Exception as e:
            logger.warning(f"Could not press Android key '{key}': {e}")

    def is_keyboard_shown(self) -> bool:
        """Checks if the keyboard is currently shown."""
        logger.info("Checking if a keyboard is shown.")
        try:
            return self.driver.is_keyboard_shown()
        except Exception as e:
            logger.warning(f"is_keyboard_shown() not available: {e}")
            return False

    def hide_keyboard(self):
        """Hides the keyboard if it is displayed."""
        try:
            logger.info("Hiding the keyboard.")
            self.driver.hide_keyboard()
        except Exception as e:
            logger.warning(f"Could not hide keyboard: {e}")
