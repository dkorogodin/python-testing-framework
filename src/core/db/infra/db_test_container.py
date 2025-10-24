from testcontainers.mysql import MySqlContainer

from src import logger
from src.core.data.configs.db_configs import DbConfigs
from src.core.db.infra.db_service import DbService


class DbTestContainer(DbService):
    DEFAULT_TEST_CONTAINER_PORT = 3306
    MYSQL_DOCKER_IMAGE = "mysql:8.0.36"

    def __init__(self, db_configs: DbConfigs):
        self.container = None
        super().__init__(db_configs)

    def setup(self):
        self.container = MySqlContainer(
            image=self.MYSQL_DOCKER_IMAGE,
            username=self.db_username,
            password=self.db_password,
            dbname=self.db_name,
        )

        logger.info(f"Starting MySQL test container with '{self.db_name}' database.")
        self.container.start()
        self.db_host = self.container.get_container_host_ip()
        self.db_port = self.container.get_exposed_port(self.DEFAULT_TEST_CONTAINER_PORT)
        logger.info(f"MySQL test container with '{self.db_name}' database started at '{self.db_host}:{self.db_port}'.")

    def shutdown(self):
        logger.info(f"Stopping MySQL test container with '{self.db_name}' database at '{self.db_host}:{self.db_port}'.")
        self.container.stop()
        logger.info(f"MySQL test container with '{self.db_name}' database stopped.")
