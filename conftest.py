import os
from datetime import datetime

import allure
import pytest


def pytest_collection_modifyitems(config, items):
    """
    Automatically rerun only web tests (marked with @pytest.mark.web)
    if they fail, up to 2 times with a short delay.
    """
    for item in items:
        if "web" in item.keywords:
            # Add rerun marker dynamically for web tests only
            item.add_marker(pytest.mark.flaky(reruns=2, reruns_delay=2))

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Attach a screenshot to Allure report when a test fails.
    """
    outcome = yield
    result = outcome.get_result()

    if result.when == "call" and result.failed:
        driver = _extract_driver(item)
        if driver:
            _attach_screenshot(driver, item.name)
        else:
            print(f"[WARN] No WebDriver found for failed test: {item.name}")


def _extract_driver(item):
    """
    Recursively search for a Selenium WebDriver inside test fixtures.
    Works for nested objects like login_page.driver.
    """
    visited = set()

    def search(obj):
        if obj is None or id(obj) in visited:
            return None
        visited.add(id(obj))

        # Found the WebDriver itself
        if hasattr(obj, "save_screenshot") and callable(obj.save_screenshot):
            return obj

        # Look inside attributes (page objects, helpers, etc.)
        if hasattr(obj, "__dict__"):
            for val in obj.__dict__.values():
                found = search(val)
                if found:
                    return found

        return None

    # Search through all test fixtures
    for fixture_value in item.funcargs.values():
        driver = search(fixture_value)
        if driver:
            return driver

    return None


def _attach_screenshot(driver, test_name: str):
    """
    Save screenshot and attach it to Allure.
    """
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_dir = os.path.join("target", "reports", "screenshots")
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = os.path.join(screenshot_dir, f"{test_name}_{timestamp}.png")

        driver.save_screenshot(screenshot_path)
        allure.attach.file(
            screenshot_path,
            name=f"Screenshot - {test_name}",
            attachment_type=allure.attachment_type.PNG
        )
        print(f"[INFO] Screenshot saved: {screenshot_path}")
    except Exception as e:
        print(f"[WARN] Failed to take screenshot for {test_name}: {e}")
