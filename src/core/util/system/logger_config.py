import logging
import os
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path

# Logs directory at project root src/core/util/system/logger_config.py
PROJECT_ROOT = Path(__file__).parents[4]

LOG_DIR = PROJECT_ROOT / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

# Formatter similar to Logback
formatter = logging.Formatter(
    "%(asctime)s.%(msecs)03d [%(threadName)s] %(levelname)-5s %(name)s - %(message)s",
    datefmt="%H:%M:%S"
)

# Current log file
current_log_file = LOG_DIR / "currentLogFile.log"


# Daily rotating + size rotation
class DailySizeRotatingHandler(TimedRotatingFileHandler):
    def __init__(self, base_dir: Path, filename="logFile.log"):
        self.base_dir = base_dir
        log_file = base_dir / filename
        super().__init__(log_file, when="midnight", interval=1, backupCount=0, encoding="utf-8")

    def doRollover(self):
        date_str = datetime.now().strftime("%Y-%m-%d")
        date_dir = self.base_dir / date_str
        date_dir.mkdir(parents=True, exist_ok=True)
        i = 0
        while (date_dir / f"logFile-{date_str}-{i}.log").exists():
            i += 1
        self.stream.close()
        os.rename(self.baseFilename, date_dir / f"logFile-{date_str}-{i}.log")
        self.stream = self._open()


# Central function to configure logger
def configure_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.propagate = False

    if not logger.handlers:
        # Console (WARN+)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.WARN)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        # Current log file
        file_handler = logging.FileHandler(current_log_file, encoding="utf-8")
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # Archived daily+size logs
        archive_handler = DailySizeRotatingHandler(LOG_DIR)
        archive_handler.setLevel(logging.INFO)
        archive_handler.setFormatter(formatter)
        logger.addHandler(archive_handler)

    return logger
