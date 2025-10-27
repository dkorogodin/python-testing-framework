import json
from pathlib import Path

# src/core/web/data/dataprovider/login_data_provider.py
DATA_PATH = Path(__file__).resolve().parents[5] / "data/test_data/web/json"


def invalid_login_simple_data() -> list[tuple[str, str]]:
    """Static list of invalid login data."""
    return [
        ("tester_aqa_331@mail.com", "12345678"),
        ("tester_aqa_332@mail.com", "Tester123.")
    ]


def invalid_login_json_to_map() -> list[tuple[str, str]]:
    """Reads login-invalid-data.json and returns data as a list of tuples or dicts."""
    json_file = DATA_PATH / "login-invalid-data.json"
    with open(json_file, encoding="utf-8") as f:
        data = json.load(f)

    return [(item["username"], item["password"]) for item in data]
