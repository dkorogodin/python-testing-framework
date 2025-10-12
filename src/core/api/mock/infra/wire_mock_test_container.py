from wiremock.testing.testcontainer import WireMockContainer

from src import logger
from src.core.api.mock.infra.wiremock_service import WireMockService
from src.core.data.properties.properties_manager import PropertiesManager


class WireMockTestContainer(WireMockService):
    def __init__(self, properties_manager: PropertiesManager):
        super().__init__(properties_manager)
        self.container = WireMockContainer(secure=False)
        self.host = None
        self.port = None

    def start_wiremock(self):
        self.container.start()
        self.host = self.container.get_container_host_ip()
        self.port = self.container.get_exposed_port(8080)
        logger.info("WireMock started in test container.")

    def stop_wiremock(self):
        self.container.stop()

    def get_base_url(self) -> str:
        if self.host is None or self.port is None:
            raise RuntimeError("WireMock container not started yet")
        return f"http://{self.host}:{self.port}"
