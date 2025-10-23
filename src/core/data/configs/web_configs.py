from src.core.util.system.config_loader_util import ConfigLoader


class WebConfigs:

    def __init__(self, loader: ConfigLoader):
        self.loader = loader
        self.driver_type = self.loader.get("driver.type")
        self.browser_name = self.loader.get("browser.name")
        self.browser_version = self.loader.get("browser.version")
        self.web_base_url = self.loader.get("app.baseurl")
        self.web_username = self.loader.get("app.username")
        self.web_password = self.loader.get("app.password")
        self.cloud_os_name = self.loader.get("cloud.os.name")
        self.cloud_os_version = self.loader.get("cloud.os.version")
        self.cloud_username = self.loader.get("cloud.username")
        self.cloud_access_key = self.loader.get("cloud.accessKey")
        self.cloud_remote_address = self.loader.get("cloud.remoteAddress")
        self.cloud_session_name = self.loader.get("cloud.session.name")
        self.cloud_build_name = self.loader.get("cloud.build.name")
        self.remote_address = None

    def set_remote_address(self, new_remote_address: str):
        """Update the remote_address value."""
        self.remote_address = new_remote_address
