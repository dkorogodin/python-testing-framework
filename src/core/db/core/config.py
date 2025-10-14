from src.core.db.infra.db_test_container import DbTestContainer


class DbConfig:
    db_test_container: DbTestContainer

    def __init__(self, db_test_container: DbTestContainer):
        self.db_test_container = db_test_container

    def get_url(self) -> str:
        """Return SQLAlchemy-compatible connection URL."""
        username = self.db_test_container.db_username
        password = self.db_test_container.db_password
        host = self.db_test_container.db_host
        port = self.db_test_container.db_port
        db_name = self.db_test_container.db_name
        return f"mysql+pymysql://{username}:{password}@{host}:{port}/{db_name}"
