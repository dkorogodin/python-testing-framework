from src.core.util.system.config_loader_util import ConfigLoader


class DbConfigs:

    def __init__(self, loader: ConfigLoader):
        self.loader = loader
        self.db_name = self.loader.get("db.name")
        self.db_username = self.loader.get("db.username")
        self.db_password = self.loader.get("db.password")
