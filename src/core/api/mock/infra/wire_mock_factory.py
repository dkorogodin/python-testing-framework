from src.core.api.mock.infra.wire_mock_local import WireMockLocal
from src.core.api.mock.infra.wire_mock_service_type import WireMockServiceType
from src.core.api.mock.infra.wire_mock_test_container import WireMockTestContainer
from src.core.api.mock.infra.wiremock_service import WireMockService
from src.core.data.configs.configs_manager import ConfigsManager


class WireMockServiceFactory:
    @staticmethod
    def get_wiremock_service(configs_manager: ConfigsManager) -> WireMockService:
        mockservice = configs_manager.api_configs.mock_service
        service_type = WireMockServiceType.from_property(mockservice)

        if service_type == WireMockServiceType.LOCAL:
            return WireMockLocal(configs_manager)
        else:
            return WireMockTestContainer(configs_manager)
