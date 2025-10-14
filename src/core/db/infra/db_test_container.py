from pathlib import Path

from testcontainers.mysql import MySqlContainer

from src import logger
from src.core.data.configs.db_configs import DbConfigs


class DbTestContainer:
    DEFAULT_TEST_CONTAINER_PORT = 3306
    MYSQL_DOCKER_IMAGE = "mysql:8.0.36"

    # src/core/db/infra/db_test_container.py
    PROJECT_ROOT = Path(__file__).parents[4]
    DB_TEST_DATA_PATH = PROJECT_ROOT / "data" / "test_data" / "db"
    INIT_PAYMENT_DB_TEST_DATA_PATH = DB_TEST_DATA_PATH / "initial-paymentdb-test-data.sql"
    INIT_PRODUCT_DB_TEST_DATA_PATH = DB_TEST_DATA_PATH / "initial-productdb-test-data.sql"

    def __init__(self, db_configs: DbConfigs, init_script_path: str):
        self.container = MySqlContainer(
            image=self.MYSQL_DOCKER_IMAGE,
            username=db_configs.db_username,
            password=db_configs.db_password,
            dbname=db_configs.db_name,
        )

        logger.info(f"Starting MySQL test container with '{db_configs.db_name}' database.")
        self.container.start()
        self.db_name = db_configs.db_name
        self.db_host = self.container.get_container_host_ip()
        self.db_port = self.container.get_exposed_port(self.DEFAULT_TEST_CONTAINER_PORT)
        self.db_username = db_configs.db_username
        self.db_password = db_configs.db_password

        logger.info(f"MySQL test container with '{self.db_name}' database started at '{self.db_host}:{self.db_port}'.")

        if init_script_path:
            self._execute_init_script(init_script_path)

    def shutdown(self):
        logger.info(f"Stopping MySQL test container with '{self.db_name}' database at '{self.db_host}:{self.db_port}'.")
        self.container.stop()
        logger.info(f"MySQL test container with '{self.db_name}' database stopped.")

    def _execute_init_script(self, script_path: str):
        """Executes SQL script on the running container."""
        import mysql.connector
        import time

        # Wait for container to be ready
        time.sleep(5)  # crude wait; could implement retry logic

        conn = mysql.connector.connect(
            host=self.db_host,
            port=self.db_port,
            user=self.db_username,
            password=self.db_password,
            database=self.db_name,
        )
        cursor = conn.cursor()
        logger.info(f"Initializing database with '{script_path}' script.")
        with open(script_path, 'r') as f:
            sql_commands = f.read().split(';')
            for cmd in sql_commands:
                cmd = cmd.strip()
                if cmd:
                    cursor.execute(cmd)
        conn.commit()
        cursor.close()
        conn.close()
        logger.info(f"Database '{self.db_name}' initialized.")
