import os
import time
from pathlib import Path

import requests
from wiremock.server import WireMockServer

from src import logger
from src.core.api.mock.infra.wiremock_service import WireMockService
from src.core.data.configs.configs_manager import ConfigsManager
from src.core.util.system.port_util import find_free_port


class WireMockLocal(WireMockService):
    def __init__(self, configs_manager: ConfigsManager, host: str = "localhost"):
        super().__init__(configs_manager)
        docker_host = os.environ.get("DOCKER_HOST_INTERNAL", "").lower() in ("1", "true", "yes")
        self.host = "host.docker.internal" if docker_host else host
        self.port = find_free_port()

        # src/core/api/mock/infra/wire_mock_local.py
        self.project_root = Path(__file__).parents[5]

        self.wiremock_standalone_jar = self.project_root / "data" / "wiremock" / "wiremock-standalone-3.13.1.jar"
        self.server = WireMockServer(port=self.port, jar_path=self.wiremock_standalone_jar, max_attempts=100)

    def start_wiremock(self):
        self.server.start()
        self._wait_for_admin()
        logger.info("WireMock started locally.")

    def stop_wiremock(self):
        self.server.stop()

    def get_base_url(self) -> str:
        return f"http://{self.host}:{self.port}"

    def _wait_for_admin(self, timeout: float = 15.0, interval: float = 0.25):
        logger.info("WireMock process started, waiting for /__admin...")
        url = f"http://{self.host}:{self.port}/__admin"
        start = time.time()
        while time.time() - start < timeout:
            try:
                r = requests.get(url)
                if r.status_code == 200:
                    logger.info("WireMock /__admin is ready")
                    return
            except requests.exceptions.ConnectionError:
                pass
            time.sleep(interval)
        raise RuntimeError(f"WireMock /__admin did not respond after {timeout} seconds")
