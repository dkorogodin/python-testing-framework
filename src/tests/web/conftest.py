import pytest

from src.core.data.properties.properties_manager import PropertiesManager
from src.core.web.driver.driver_type import DriverType
from src.core.web.infra.selenium_grid_test_container import SeleniumGridTestContainer
from src.core.web.manager.web_app_lifecycle import WebAppLifecycle
from src.core.web.pageobject.page_navigator import PageNavigator


@pytest.fixture(scope="session")
def properties_manager():
    return PropertiesManager()


@pytest.fixture(scope="session")
def selenium_grid(properties_manager):
    props = properties_manager.web_properties
    container = None
    if props.driver_type.lower() == "remote":
        container = SeleniumGridTestContainer(props.browser_name)
    yield container
    if container:
        container.shutdown()


@pytest.fixture(scope="session")
def web_app_lifecycle(properties_manager, selenium_grid):
    _set_remote_address(properties_manager, selenium_grid)
    lifecycle = WebAppLifecycle(properties_manager.web_properties)
    yield lifecycle
    lifecycle.close_browser()


@pytest.fixture
def login_page(web_app_lifecycle, properties_manager):
    driver = web_app_lifecycle.get_driver()
    page_navigator = PageNavigator(driver, properties_manager.web_properties)
    yield page_navigator.goto_login_page()
    web_app_lifecycle.restart_browser()


@pytest.fixture
def home_page(login_page, properties_manager):
    props = properties_manager.web_properties
    return login_page.login_then_goto_home_page(
        props.web_username,
        props.web_password
    )


def _set_remote_address(properties_manager, selenium_grid):
    """
    Sets the remote address for the web driver based on the configured driver type.
    """
    web_props = properties_manager.web_properties
    driver_type = DriverType.from_property(web_props.driver_type)

    if driver_type == DriverType.REMOTE:
        web_props.remote_address = selenium_grid.hub_url
    elif driver_type == DriverType.CLOUD:
        cloud_url = f"https://{web_props.cloud_username}:{web_props.cloud_access_key}@{web_props.cloud_remote_url}"
        web_props.remote_address = cloud_url
    else:
        pass
