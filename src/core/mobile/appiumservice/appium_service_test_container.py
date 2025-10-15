from testcontainers.core.container import DockerContainer
from testcontainers.core.waiting_utils import wait_for_logs

from src import logger


class AppiumServiceTestContainer:
    _APPIUM_PORT = 4723
    _VNC_PORT = 5900
    _NOVNC_PORT = 6080

    def __init__(self, image="appium/appium:latest"):
        self.container = (DockerContainer(image)
                          .with_exposed_ports(self._APPIUM_PORT, self._VNC_PORT, self._NOVNC_PORT)
                          .with_env("APPIUM_ALLOW_INSECURE", "chromedriver_autodownload")
                          .with_env("ENABLE_VNC", "true")
                          .with_env("ENABLE_NO_VNC", "true"))
        self._start()

    def shutdown(self):
        logger.info(f"Stopping Appium test container at '{self.url}'")
        self.container.stop()
        logger.info("Appium container stopped.")

    def get_url(self):
        return self.url

    def _start(self):
        logger.info("Starting Appium container...")

        self.container.start()
        wait_for_logs(self.container, "listener started", timeout=60)

        mapped_port = self.container.get_exposed_port(self._APPIUM_PORT)
        host = self.container.get_container_host_ip()
        self.url = f"http://{host}:{mapped_port}"

        novnc_port = self.container.get_exposed_port(self._NOVNC_PORT)
        logger.info(f"Appium test container started at '{self.url}'. noVNC: http://{host}:{novnc_port}")

        return self.url
