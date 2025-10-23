import os

import pytest

from src.core.data.configs.configs_manager import ConfigsManager
from src.core.mobile.appiumservice.appium_service_factory import AppiumServiceFactory
from src.core.mobile.data.enums.mobile_platform import MobilePlatform
from src.core.mobile.manager.mobile_manager import MobileManager


@pytest.fixture(scope="session")
def android_configs_manager(request):
    os.environ["COMMON_PLATFORM"] = MobilePlatform.ANDROID.name
    return ConfigsManager(pytest_config=request.config)


@pytest.fixture()
def appium_service(android_configs_manager):
    """Start local Appium service only for non-cloud runs."""
    mobile_configs = android_configs_manager.mobile_configs

    if mobile_configs.is_cloud:
        yield None
        return

    service = AppiumServiceFactory.get_appium_service(mobile_configs)
    yield service
    service.shutdown()


@pytest.fixture()
def mobile_manager(android_configs_manager, appium_service):
    """Create the Appium driver (local or cloud)."""
    mobile_configs = android_configs_manager.mobile_configs
    mobile_configs.set_mobile_platform(MobilePlatform.ANDROID)
    app_package_or_bundle_id = mobile_configs.app_package_or_bundle_id

    manager = MobileManager(mobile_configs)
    manager.get_app().install_app_then_launch(app_package_or_bundle_id, mobile_configs.app_name)
    yield manager
    manager.full_mobile_cleanup(app_package_or_bundle_id)
