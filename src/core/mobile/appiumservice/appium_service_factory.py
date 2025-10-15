from src.core.data.configs.mobile_configs import MobileConfigs
from src.core.mobile.appiumservice.appium_service_local import AppiumServiceLocal
from src.core.mobile.appiumservice.appium_service_test_container import AppiumServiceTestContainer
from src.core.mobile.appiumservice.appium_service_type import AppiumServiceType


class AppiumServiceFactory:
    @staticmethod
    def get_appium_service(mobile_configs: MobileConfigs):
        service_type = AppiumServiceType.from_property(mobile_configs.appium_service_type)

        if service_type == AppiumServiceType.LOCAL:
            service = AppiumServiceLocal()
        else:
            service = AppiumServiceTestContainer()
        mobile_configs.set_appium_service_url(service.get_url())
        return service
