from src.core.db.infra.db_service import DbService


class DbConfig:

    def __init__(self, db_service: DbService):
        self.db_service = db_service

    def get_url(self) -> str:
        """Return SQLAlchemy-compatible connection URL."""
        username = self.db_service.db_username
        password = self.db_service.db_password
        host = self.db_service.db_host
        port = self.db_service.db_port
        db_name = self.db_service.db_name
        return f"mysql+pymysql://{username}:{password}@{host}:{port}/{db_name}"
