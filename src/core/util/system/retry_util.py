import time
from typing import TypeVar

from src import logger

T = TypeVar("T")


class RetryUtil:
    @staticmethod
    def retry(func, retries=3, delay=1):
        """Simple retry utility to retry a callable."""
        for attempt in range(1, retries + 1):
            try:
                return func()
            except Exception as e:
                logger.warning(f"Attempt {attempt} failed: {e}")
                if attempt < retries:
                    time.sleep(delay)
                else:
                    logger.error(f"All {retries} retry attempts failed.")
                    raise
        return None
