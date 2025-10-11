from testcontainers.core.container import DockerContainer

from src.core.api.mock.infra.wiremock_service import WireMockService
from src.core.data.properties.properties_manager import PropertiesManager


class WireMockTestContainer(WireMockService):
    WIREMOCK_DOCKER_IMAGE = "wiremock/wiremock:3.6.0"

    def __init__(self, properties_manager: PropertiesManager):
        super().__init__(properties_manager)
        self.container = DockerContainer(self.WIREMOCK_DOCKER_IMAGE).with_exposed_ports(8080)
        self.host = None
        self.port = None

    def start_wiremock(self):
        self.container.start()
        self.host = self.container.get_container_host_ip()
        self.port = self.container.get_exposed_port(8080)

    def stop_wiremock(self):
        self.container.stop()

    def get_base_url(self) -> str:
        if self.host is None or self.port is None:
            raise RuntimeError("WireMock container not started yet")
        return f"http://{self.host}:{self.port}"
