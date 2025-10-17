import os
from datetime import datetime
import allure

class ScreenshotUtil:
    """
    Handles taking and attaching screenshots for failed tests.
    Works with Selenium WebDriver (web) and Appium (mobile) drivers.
    """

    @staticmethod
    def attach_screenshot_on_failure(item, driver):
        """
        Save a screenshot for a failed test and attach it to Allure.
        """
        test_name = item.name
        screenshot_path = ScreenshotUtil._save_screenshot(driver, test_name)
        if screenshot_path:
            allure.attach.file(
                screenshot_path,
                name=f"Screenshot - {test_name}",
                attachment_type=allure.attachment_type.PNG
            )
            print(f"[INFO] Screenshot attached to Allure: {screenshot_path}")

    @staticmethod
    def _save_screenshot(driver, test_name: str) -> str | None:
        """
        Save screenshot to target/reports/screenshots and return path.
        """
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_dir = os.path.join("target", "reports", "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_path = os.path.join(screenshot_dir, f"{test_name}_{timestamp}.png")

            driver.save_screenshot(screenshot_path)
            print(f"[INFO] Screenshot saved: {screenshot_path}")
            return screenshot_path
        except Exception as e:
            print(f"[WARN] Failed to save screenshot for {test_name}: {e}")
            return None

    @staticmethod
    def extract_driver_from_item(item):
        """
        Recursively search for a Selenium/WebDriver instance in test fixtures.
        Works for nested objects like login_page.driver.
        """
        visited = set()

        def search(obj):
            if obj is None or id(obj) in visited:
                return None
            visited.add(id(obj))

            if hasattr(obj, "save_screenshot") and callable(obj.save_screenshot):
                return obj

            if hasattr(obj, "__dict__"):
                for val in obj.__dict__.values():
                    found = search(val)
                    if found:
                        return found
            return None

        for fixture_value in item.funcargs.values():
            driver = search(fixture_value)
            if driver:
                return driver

        return None
