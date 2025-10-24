import os

from src import logger
from src.core.data.configs.db_configs import DbConfigs
from src.core.db.infra.db_service import DbService


class DbLocal(DbService):

    def __init__(self, db_configs: DbConfigs):
        super().__init__(db_configs)

    def setup(self):
        logger.info(f"MySQL docker container with '{self.db_name}' database started separately.")
        docker_host = os.environ.get("DOCKER_HOST_INTERNAL", "").lower() in ("1", "true", "yes")
        self.db_host = "host.docker.internal" if docker_host else "localhost"
        self.db_port = int(self.db_configs.db_port)
        logger.info(f"'{self.db_name}' database started at '{self.db_host}:{self.db_port}'.")

    def shutdown(self):
        logger.info(f"MySQL docker container with '{self.db_name}' database not stopped. It will be stopped separately.")
