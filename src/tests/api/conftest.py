import pytest

from src.core.api.mock.infra.wire_mock_factory import WireMockServiceFactory
from src.core.api.service.service_manager import ApiMicroServiceManager


@pytest.fixture(scope="session")
def wiremock_service(configs_manager):
    service = WireMockServiceFactory.get_wiremock_service(configs_manager)
    service.start()
    yield service
    service.shutdown()


@pytest.fixture
def api_service_manager(configs_manager, wiremock_service):
    return ApiMicroServiceManager(configs_manager, wiremock_service.get_url())
