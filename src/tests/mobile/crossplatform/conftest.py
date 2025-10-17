import pytest

from src.core.mobile.appiumservice.appium_service_factory import AppiumServiceFactory
from src.core.mobile.manager.mobile_manager import MobileManager
from src.core.mobile.pageobject.crossplatform.catalog_page import CatalogPage
from src.core.mobile.util.video_util import VideoUtil


@pytest.fixture(autouse=True)
def video_recorder(configs_manager, mobile_manager, request):
    """
    Start/stop Appium video recording automatically for mobile tests.
    Only active if 'recordVideo' is enabled in mobile configs.
    """
    driver = mobile_manager.get_driver()

    if configs_manager.mobile_configs.recordVideo:
        VideoUtil.start_recording(driver)

    yield  # Run test

    rep_call = getattr(request.node, "rep_call", None)
    if configs_manager.mobile_configs.recordVideo:
        base64_data = VideoUtil.stop_recording(driver)
        if rep_call and rep_call.failed:
            VideoUtil.save_video_if_failed(driver, request.node.name, base64_data)


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
