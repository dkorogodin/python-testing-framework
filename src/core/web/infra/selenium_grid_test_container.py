import logging
import time

import requests
from testcontainers.core.container import DockerContainer

logger = logging.getLogger(__name__)


class SeleniumGridTestContainer:
    """Manages standalone Selenium containers for browser automation tests."""

    def __init__(self, browser_name: str):
        self.browser_name = browser_name.lower()
        self.container: DockerContainer | None = None

        docker_image = self._get_docker_image()
        logger.info("Starting Selenium standalone container with '%s' docker image...", docker_image)

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

        logger.info(
            "Selenium container with '%s' docker image started at '%s'", docker_image, self.hub_url
        )

    def shutdown(self):
        """Stops the Selenium container."""
        if self.container:
            logger.info("Stopping Selenium standalone container at '%s'...", self.hub_url)
            self.container.stop()
            logger.info("Selenium container stopped at '%s'.", self.hub_url)

    def _get_docker_image(self) -> str:
        """Returns the Docker image name for the specified browser."""
        if self.browser_name == "chrome":
            return "selenium/standalone-chrome:latest"
        elif self.browser_name == "firefox":
            return "selenium/standalone-firefox:latest"
        else:
            logger.warning("Unknown browser '%s', defaulting to Chrome.", self.browser_name)
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
