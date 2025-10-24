import os

from src import logger
from src.core.data.configs.web_configs import WebConfigs
from src.core.web.infra.selenium_grid_service import SeleniumGridService


class SeleniumGridDockerCompose(SeleniumGridService):

    def __init__(self, web_configs: WebConfigs):
        self.hub_url = None
        super().__init__(web_configs)

    def setup(self):
        logger.info(f"Selenium Grid docker container started separately via docker compose.")
        docker_host = os.environ.get("DOCKER_HOST_INTERNAL", "").lower() in ("1", "true", "yes")
        host = "host.docker.internal" if docker_host else "localhost"
        self.hub_url = f"http://{host}:4444/wd/hub"
        self.web_configs.remote_address = self.hub_url
        logger.info("Selenium Grid started at '%s'", self.hub_url)

    def shutdown(self):
        logger.info("Selenium Grid docker container at '%s' not stopped. "
                    "It will be stopped separately via docker compose.", self.hub_url)
