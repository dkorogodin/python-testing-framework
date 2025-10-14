import pytest

from src.core.api.mock.infra.wire_mock_factory import WireMockServiceFactory
from src.core.api.service.service_manager import ApiMicroServiceManager
from src.core.db.core.config import DbConfig
from src.core.db.core.db_pool import DbPool
from src.core.db.infra.db_test_container import DbTestContainer
from src.core.web.infra.selenium_grid_test_container import SeleniumGridTestContainer
from src.core.web.manager.web_app_lifecycle import WebAppLifecycle
from src.core.web.pageobject.page_navigator import PageNavigator


@pytest.fixture(scope="session")
def selenium_grid(configs_manager):
    props = configs_manager.web_configs
    container = None
    if props.driver_type.lower() == "remote":
        container = SeleniumGridTestContainer(props)
    yield container
    if container:
        container.shutdown()


@pytest.fixture(scope="session")
def wiremock_service(configs_manager):
    service = WireMockServiceFactory.get_wiremock_service(configs_manager)
    service.start()
    yield service
    service.shutdown()


@pytest.fixture(scope="session")
def payment_db_pool(configs_manager):
    payment = DbTestContainer(configs_manager.payments_db_configs, DbTestContainer.INIT_PAYMENT_DB_TEST_DATA_PATH)
    pool = DbPool(DbConfig(payment), max_pool_size=5)
    yield pool
    payment.shutdown()


@pytest.fixture(scope="session")
def product_db_pool(configs_manager):
    product = DbTestContainer(configs_manager.products_db_configs, DbTestContainer.INIT_PRODUCT_DB_TEST_DATA_PATH)
    pool = DbPool(DbConfig(product), max_pool_size=5)
    yield pool
    product.shutdown()


@pytest.fixture(scope="session")
def api_service_manager(configs_manager, wiremock_service):
    return ApiMicroServiceManager(configs_manager, wiremock_service.get_url())


@pytest.fixture
def web_app_lifecycle(configs_manager, selenium_grid):
    lifecycle = WebAppLifecycle(configs_manager.web_configs)
    yield lifecycle
    lifecycle.close_browser()


@pytest.fixture
def login_page(web_app_lifecycle, configs_manager):
    driver = web_app_lifecycle.get_driver()
    page_navigator = PageNavigator(driver, configs_manager.web_configs)
    return page_navigator.goto_login_page()


@pytest.fixture
def home_page(login_page, configs_manager):
    props = configs_manager.web_configs
    return login_page.login_then_goto_home_page(
        props.web_username,
        props.web_password
    )
