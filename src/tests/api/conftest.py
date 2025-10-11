import pytest

from src.core.api.mock.infra.wire_mock_factory import WireMockServiceFactory
from src.core.api.service.service_manager import ApiMicroServiceManager
from src.core.data.properties.properties_manager import PropertiesManager


@pytest.fixture(scope="session")
def properties_manager():
    return PropertiesManager()


@pytest.fixture(scope="session")
def wiremock_service(properties_manager):
    service = WireMockServiceFactory.get_wiremock_service(properties_manager)
    service.start()
    yield service
    service.shutdown()


@pytest.fixture(scope="session")
def api_service_manager(properties_manager, wiremock_service):
    return ApiMicroServiceManager(properties_manager, wiremock_service.get_url())
