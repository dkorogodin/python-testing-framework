import pytest

from src.core.util.platformshared.screenshot_util import ScreenshotUtil


# ---------- Pytest CLI integration ----------

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default=None)
    parser.addoption("--driver_type", action="store", default=None)
    parser.addoption("--app_baseurl", action="store", default=None)
    parser.addoption("--app_username", action="store", default=None)
    parser.addoption("--app_password", action="store", default=None)
    parser.addoption("--mock_service", action="store", default=None)
    parser.addoption("--selenium_grid", action="store", default=None)
    parser.addoption("--db_infra", action="store", default=None)


def pytest_collection_modifyitems(config, items):
    """
    Automatically rerun only web tests (marked with @pytest.mark.web)
    if they fail, up to 2 times with a short delay.
    """
    for item in items:
        if "web" in item.keywords:
            item.add_marker(pytest.mark.flaky(reruns=2, reruns_delay=2))


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to attach screenshots for failed tests.
    """
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

    if rep.when == "call" and rep.failed:
        driver = ScreenshotUtil.extract_driver_from_item(item)
        if driver:
            ScreenshotUtil.attach_screenshot_on_failure(item, driver)
        else:
            print(f"[WARN] No WebDriver found for failed test: {item.name}")
