from abc import ABC, abstractmethod
from pathlib import Path

from src import logger
from src.core.data.configs.db_configs import DbConfigs


class DbService(ABC):
    # src/core/db/infra/db_test_container.py
    PROJECT_ROOT = Path(__file__).parents[4]
    DB_TEST_DATA_PATH = PROJECT_ROOT / "data" / "test_data" / "db"

    def __init__(self, db_configs: DbConfigs):
        self.db_configs = db_configs
        self.db_name = db_configs.db_name
        self.db_username = db_configs.db_username
        self.db_password = db_configs.db_password
        self.db_host = None
        self.db_port = None

        self.setup()
        self._execute_init_script()

    @abstractmethod
    def setup(self):
        pass

    @abstractmethod
    def shutdown(self):
        pass

    def _execute_init_script(self):
        """Executes SQL script on the running container."""
        script_path = self.DB_TEST_DATA_PATH / self.db_configs.db_init_script
        if self.db_configs.db_init_script:
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
