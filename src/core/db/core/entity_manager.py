from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session

Base = declarative_base()


class EntityManager:
    def __init__(self, db_url: str, echo: bool = False):
        self.engine = create_engine(db_url, echo=echo, future=True)
        self.SessionLocal = sessionmaker(bind=self.engine, expire_on_commit=False, class_=Session)

    def create_tables(self):
        """Create all database tables based on entity metadata."""
        Base.metadata.create_all(self.engine)

    def drop_tables(self):
        """Drop all tables (useful for tests)."""
        Base.metadata.drop_all(self.engine)

    def get_session(self) -> Session:
        """Return a new SQLAlchemy Session (like EntityManager)."""
        return self.SessionLocal()
