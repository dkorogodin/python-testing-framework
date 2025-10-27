import json
from pathlib import Path

# src/core/mobile/data/dataprovider/login_data_provider.py
DATA_PATH = Path(__file__).resolve().parents[5] / "data/test_data/mobile/json"


def invalid_login_credentials() -> list[tuple[str, str]]:
    """Reads login-invalid-data.json and returns data as a list of tuples or dicts."""
    json_file = DATA_PATH / "login-invalid-data.json"
    with open(json_file, encoding="utf-8") as f:
        data = json.load(f)

    return [(item["username"], item["password"]) for item in data]
