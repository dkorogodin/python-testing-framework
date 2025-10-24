import time

import requests
from testcontainers.core.container import DockerContainer

from src import logger
from src.core.data.configs.web_configs import WebConfigs
from src.core.web.infra.selenium_grid_service import SeleniumGridService


class SeleniumGridTestContainer(SeleniumGridService):

    def __init__(self, web_configs: WebConfigs):
        self.container = None
        self.hub_url = None
        super().__init__(web_configs)

    def setup(self):
        docker_image = self._get_docker_image(self.web_configs.browser_name.lower())
        logger.info("Starting Selenium Grid test container with '%s' docker image...", docker_image)

        self.container = (
            DockerContainer(docker_image)
            .with_env("SE_NODE_MAX_SESSIONS", "2")
            .with_env("VNC_NO_PASSWORD", "1")
            .with_exposed_ports(4444)
        )

        # Start container
        self.container.start()
        host = self.container.get_container_host_ip()
        port = self.container.get_exposed_port(4444)
        self.hub_url = f"http://{host}:{port}/wd/hub"
        self._wait_for_grid(self.hub_url)

        self.web_configs.remote_address = self.hub_url
        logger.info("Selenium Grid started at '%s'", self.hub_url)

    def shutdown(self):
        if self.container:
            logger.info("Stopping Selenium Grid test container at '%s'...", self.hub_url)
            self.container.stop()
            logger.info("Selenium Grid test container at '%s' stopped.", self.hub_url)

    def _get_docker_image(self, browser_name: str) -> str:
        if browser_name == "chrome":
            return "selenium/standalone-chrome:latest"
        elif browser_name == "firefox":
            return "selenium/standalone-firefox:latest"
        else:
            logger.warning("Unknown browser '%s', defaulting to Chrome.", browser_name)
            return "selenium/standalone-chrome:latest"

    def _wait_for_grid(self, url, timeout=30):
        start = time.time()
        while time.time() - start < timeout:
            try:
                response = requests.get(f"{url}/status", timeout=2)
                if response.status_code == 200 and '"ready": true' in response.text:
                    return True
            except Exception:
                time.sleep(1)
        raise RuntimeError(f"Selenium Grid not ready at {url}")
