from typing import Optional

from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import WebDriverException

from src import logger
from src.core.mobile.data.enums.mobile_platform import MobilePlatform


class MobileAppLifecycle:
    """
    Manages the lifecycle of a mobile application including install, uninstall, activate, and query state.

    Supports both local and cloud environments for Android and iOS.
    """

    def __init__(self, driver: WebDriver, is_cloud: bool = False):
        if not hasattr(driver, "install_app"):
            raise ValueError("Driver must support app management commands (install_app, remove_app, etc.)")

        self.driver = driver
        self.is_cloud = is_cloud
        self.is_ios = driver.capabilities.get("platformName", "").lower() == MobilePlatform.IOS.value.lower()

    # ------------------------------------------------
    # Install
    # ------------------------------------------------
    def install_app(self, app_path: str):
        """Install app only if running locally. Cloud apps are pre-installed."""
        if self.is_cloud:
            logger.info("Cloud session — skipping install_app (pre-installed by provider).")
            return

        logger.info(f"Installing app from path: {app_path}")
        try:
            self.driver.install_app(app_path, replace=True)
            logger.info(f"App installed successfully from: {app_path}")
        except WebDriverException as e:
            logger.warning(f"Failed to install app: {e}")

    def install_app_then_launch(self, app_id: str, app_path: Optional[str] = None):
        """
        Installs and/or launches the app.
        For iOS cloud, skip install/activate — Appium session launches automatically.
        """
        if self.is_cloud and self.is_ios:
            logger.info("Cloud iOS — skipping install/activate (session will auto-launch).")
            return

        if not self.is_app_installed(app_id):
            if app_path:
                self.install_app(app_path)
            else:
                logger.warning(f"App '{app_id}' not installed, but no path provided.")
        else:
            logger.info(f"App '{app_id}' is already installed, skipping installation.")

        if self.get_app_state(app_id) != "running_in_foreground":
            self.activate_app(app_id)

    # ------------------------------------------------
    # Uninstall
    # ------------------------------------------------
    def uninstall_app(self, app_id: str):
        """Uninstall app only locally."""
        if self.is_cloud:
            logger.info("Cloud session — skipping uninstall_app (managed by provider).")
            return
        if self.is_app_installed(app_id):
            self.remove_app(app_id)

    def remove_app(self, app_id: str):
        """Remove the app locally."""
        if self.is_cloud:
            logger.info("Cloud session — skipping remove_app (managed by provider).")
            return False
        try:
            self.driver.remove_app(app_id)
            logger.info(f"App '{app_id}' removed.")
        except WebDriverException as e:
            logger.warning(f"Failed to remove app '{app_id}': {e}")
            return False

    # ------------------------------------------------
    # Activation / Termination
    # ------------------------------------------------
    def activate_app(self, app_id: str):
        """Activates the app. Skips for cloud iOS."""
        if self.is_cloud and self.is_ios:
            logger.info("Cloud iOS — skipping activate_app (session already launched).")
            return
        logger.info(f"Activating app '{app_id}'.")
        try:
            self.driver.activate_app(app_id)
            logger.info(f"App '{app_id}' activated successfully.")
        except WebDriverException as e:
            logger.warning(f"Failed to activate app '{app_id}': {e}")

    def terminate_app(self, app_id: str) -> bool:
        """Terminates the app."""
        logger.info(f"Terminating app '{app_id}'.")
        try:
            terminated = self.driver.terminate_app(app_id)
            logger.info(f"App '{app_id}' terminated: {terminated}")
            return terminated
        except WebDriverException as e:
            logger.warning(f"Failed to terminate app '{app_id}': {e}")
            return False

    # ------------------------------------------------
    # App State
    # ------------------------------------------------
    def is_app_installed(self, app_id: str) -> bool:
        """Checks if app is installed. For cloud iOS, always True."""
        if self.is_cloud and self.is_ios:
            logger.info(f"Cloud iOS — assuming app '{app_id}' is installed.")
            return True

        try:
            installed = self.driver.is_app_installed(app_id)
            logger.info(f"Checking if app '{app_id}' is installed: {installed}")
            return installed
        except WebDriverException as e:
            logger.warning(f"Error checking app install state for '{app_id}': {e}")
            return False

    def get_app_state(self, app_id: str) -> str:
        """Returns the current application state (mapped to readable string)."""
        try:
            state = self.driver.query_app_state(app_id)
            state_map = {
                0: "not_installed",
                1: "not_running",
                2: "running_in_background_suspended",
                3: "running_in_background",
                4: "running_in_foreground"
            }
            readable_state = state_map.get(state, f"unknown({state})")
            logger.info(f"App '{app_id}' state: {readable_state}")
            return readable_state
        except WebDriverException as e:
            logger.warning(f"Failed to get app state for '{app_id}': {e}")
            return "unknown"

    # ------------------------------------------------
    # Background
    # ------------------------------------------------
    def run_app_in_background(self, seconds: int):
        """Runs the app in background for a specified duration."""
        logger.info(f"Running app in background for {seconds} seconds.")
        try:
            self.driver.background_app(seconds)
            logger.info("App ran in background and returned to foreground.")
        except WebDriverException as e:
            logger.warning(f"Failed to run app in background: {e}")
