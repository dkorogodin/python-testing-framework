from src.core.util.system.config_loader_util import ConfigLoader


class DbConfigs:

    def __init__(self, loader: ConfigLoader):
        self.loader = loader
        self.db_name = self.loader.get("db.name")
        self.db_port = self.loader.get("db.port")
        self.db_username = self.loader.get("db.username")
        self.db_password = self.loader.get("db.password")
        self.db_infra = self.loader.get("db.infra")
        self.db_init_script = self.loader.get("db.initscript")
