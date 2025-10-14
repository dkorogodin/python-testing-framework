import threading
from collections import deque
from typing import Set, Deque

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from src import logger
from src.core.db.core.config import DbConfig


class DbPool:
    """
    Manages a pool of SQLAlchemy sessions for efficient reuse.
    Lazy-creates sessions up to `max_pool_size`.
    """

    def __init__(self, config: DbConfig, max_pool_size: int = 5):
        self.config = config
        self.max_pool_size = max_pool_size
        self.engine = create_engine(self.config.get_url(), future=True)
        self.sessionmaker = sessionmaker(bind=self.engine, autoflush=False, autocommit=False)

        self.available_pool: Deque[Session] = deque()
        self.used_pool: Set[Session] = set()
        self._lock = threading.Lock()

    def get_available_session(self) -> Session:
        """
        Returns an available session from the pool.
        Creates a new session if pool is not full.
        Raises RuntimeError if maximum pool size is reached.
        """
        with self._lock:
            logger.info(
                f"get_available_session called. Used: {len(self.used_pool)}, Available: {len(self.available_pool)}")
            if self.available_pool:
                session = self.available_pool.popleft()
                self.used_pool.add(session)
                logger.info(
                    f"Reusing existing Session. Available: {len(self.available_pool)}, Used: {len(self.used_pool)}")
                return session

            if len(self.used_pool) < self.max_pool_size:
                session = self.sessionmaker()
                self.used_pool.add(session)
                logger.info(f"Creating new Session. Available: {len(self.available_pool)}, Used: {len(self.used_pool)}")
                return session

            raise RuntimeError("Maximum pool size reached, no available sessions!")

    def release_session(self, session: Session) -> bool:
        """
        Releases a session back to the pool.
        Returns True if successfully released, False otherwise.
        """
        with self._lock:
            logger.info(f"Releasing Session. Used before: {len(self.used_pool)}")
            if session in self.used_pool:
                self.used_pool.remove(session)
                self.available_pool.append(session)
                logger.info(f"Session released. Available: {len(self.available_pool)}, Used: {len(self.used_pool)}")
                return True
            return False

    def shutdown(self):
        """
        Closes all sessions and disposes the engine.
        """
        with self._lock:
            logger.info(
                f"Shutting down Sessions pool. Total used: {len(self.used_pool)}, available: {len(self.available_pool)}")
            for session in list(self.used_pool) + list(self.available_pool):
                try:
                    session.close()
                except Exception:
                    pass

            self.used_pool.clear()
            self.available_pool.clear()
            self.engine.dispose()
            logger.info("Sessions pool shutdown complete.")
