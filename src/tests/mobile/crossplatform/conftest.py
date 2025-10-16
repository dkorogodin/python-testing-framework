import pytest

from src.core.mobile.appiumservice.appium_service_factory import AppiumServiceFactory
from src.core.mobile.manager.mobile_manager import MobileManager
from src.core.mobile.pageobject.crossplatform.catalog_page import CatalogPage


@pytest.fixture()
def appium_service(configs_manager):
    """Start local Appium service only for non-cloud runs."""
    mobile_configs = configs_manager.mobile_configs

    if mobile_configs.is_cloud:
        yield None
        return

    service = AppiumServiceFactory.get_appium_service(mobile_configs)
    yield service
    service.shutdown()


@pytest.fixture()
def mobile_manager(configs_manager, appium_service):
    """Create the Appium driver (local or cloud)."""
    mobile_configs = configs_manager.mobile_configs
    app_package_or_bundle_id = mobile_configs.app_package_or_bundle_id

    manager = MobileManager(mobile_configs)
    manager.get_app().install_app_then_launch(app_package_or_bundle_id, mobile_configs.app_name)
    yield manager
    manager.full_mobile_cleanup(app_package_or_bundle_id)


@pytest.fixture
def catalog_page(mobile_manager):
    return CatalogPage(mobile_manager.get_driver())


@pytest.fixture
def login_page(catalog_page):
    return catalog_page.expand_navigation_menu().goto_login_page()
