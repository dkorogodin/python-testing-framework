import os
from pathlib import Path

import pytest

from src.core.api.mock.infra.wire_mock_factory import WireMockServiceFactory
from src.core.api.service.service_manager import ApiMicroServiceManager
from src.core.data.properties.properties_manager import PropertiesManager


def pytest_configure(config):
    # src/tests/api/conftest.py
    project_root = Path(__file__).parents[3]
    allure_dir = project_root / "reports" / "allure-results"
    os.makedirs(allure_dir, exist_ok=True)
    config.option.allure_report_dir = allure_dir


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
