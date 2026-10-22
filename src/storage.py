import json
from pathlib import Path


def save_db(db_url: str, cache: list[dict]):
    db_path = Path(db_url)
    db_path.parent.mkdir(parents=True, exist_ok=True)

    with db_path.open("w", encoding="utf-8") as db:
        json.dump(cache, db, ensure_ascii=False, indent=4)


def read_db(db_url: str) -> list:
    try:
        with open(db_url, "r", encoding="utf-8") as db:
            return json.load(db)
    except FileNotFoundError:
        return []
