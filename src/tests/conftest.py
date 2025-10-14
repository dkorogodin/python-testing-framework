import os
from pathlib import Path

import pytest

from src.core.data.configs.configs_manager import ConfigsManager


def pytest_configure(config):
    # src/tests/conftest.py
    project_root = Path(__file__).parents[2]
    allure_dir = project_root / "target" / "reports" / "allure-results"
    os.makedirs(allure_dir, exist_ok=True)
    config.option.allure_report_dir = allure_dir


@pytest.fixture(scope="session")
def configs_manager():
    return ConfigsManager()
