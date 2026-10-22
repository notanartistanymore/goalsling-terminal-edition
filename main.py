from dotenv import load_dotenv

import os

from src.storage import read_db
from src.cli import run_cli

load_dotenv()
database_url = os.getenv("DATABASE_URL")


def main():
    print(database_url)
    cache = read_db(db_url=database_url)
    run_cli(db_url=database_url, cache=cache)


if __name__ == "__main__":
    main()
