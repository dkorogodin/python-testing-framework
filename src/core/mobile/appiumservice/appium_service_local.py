import subprocess
import time
from pathlib import Path
from typing import Optional

import requests

from src import logger
from src.core.util.system.port_util import find_free_port


class AppiumServiceLocal:
    def __init__(self, node_path: str = "/opt/homebrew/bin/node",
                 appium_js_path: str = "/opt/homebrew/lib/node_modules/appium/build/lib/main.js"):
        self.node_path = node_path
        self.appium_js_path = appium_js_path
        self.port = find_free_port(4723, 4800)
        self.url = f"http://127.0.0.1:{self.port}"
        self.startup_timeout = 30
        self.process: Optional[subprocess.Popen] = None

        if not Path(self.node_path).exists():
            raise RuntimeError(f"Node executable not found at: {self.node_path}")
        if not Path(self.appium_js_path).exists():
            raise RuntimeError(f"Appium JS not found at: {self.appium_js_path}")

        self._start()

    def shutdown(self):
        logger.info("Stopping local Appium service...")
        if self.process:
            self.process.terminate()
            try:
                self.process.wait(timeout=10)
                logger.info("Appium service stopped gracefully.")
            except subprocess.TimeoutExpired:
                self.process.kill()
                logger.warning("Appium process killed after timeout.")
            self.process = None
        else:
            logger.warning("No Appium process to stop.")

    def get_url(self) -> str:
        return self.url

    def _start(self):
        logger.info(f"Starting local Appium server at {self.url}")
        command = [
            self.node_path, self.appium_js_path,
            "--address", "127.0.0.1",
            "--port", str(self.port),
            "--session-override",
            "--allow-insecure", "chromedriver_autodownload"
        ]

        # Launch Appium process
        self.process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        self._wait_until_server_ready()

    def _wait_until_server_ready(self):
        # Wait for Appium server to be ready
        start_time = time.time()
        while True:
            try:
                session = requests.Session()
                resp = session.get(f"{self.url}/status", timeout=2)
                if resp.status_code == 200:
                    logger.info(f"Appium server is ready at {self.url}")
                    break
            except requests.exceptions.RequestException:
                pass

            if time.time() - start_time > self.startup_timeout:
                self.shutdown()
                raise RuntimeError(f"Appium server failed to start within {self.startup_timeout} seconds")
            time.sleep(1)
