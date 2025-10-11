from src.core.api.mock.infra.wire_mock_local import WireMockLocal
from src.core.api.mock.infra.wire_mock_service_type import WireMockServiceType
from src.core.api.mock.infra.wire_mock_test_container import WireMockTestContainer
from src.core.api.mock.infra.wiremock_service import WireMockService
from src.core.data.properties.properties_manager import PropertiesManager


class WireMockServiceFactory:
    @staticmethod
    def get_wiremock_service(properties_manager: PropertiesManager) -> WireMockService:
        service_type = WireMockServiceType.from_property(
            properties_manager.api_properties.mock_service
        )

        if service_type == WireMockServiceType.LOCAL:
            return WireMockLocal(properties_manager)
        else:
            return WireMockTestContainer(properties_manager)
