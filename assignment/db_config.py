from sqlalchemy import create_engine
import pandas as pd
import hashlib
import logging
from datetime import datetime

DB_CONFIG = {
    "host": "localhost",
    "database": "sales",
    "user": "postgres",
    "password": "StrongPass123",
    "port": 5432
}

LOG_FILE = "daily_etl.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_engine():
    connection_url = (
        f"postgresql+psycopg2://{DB_CONFIG['user']}:"
        f"{DB_CONFIG['password']}@"
        f"{DB_CONFIG['host']}:"
        f"{DB_CONFIG['port']}/"
        f"{DB_CONFIG['database']}"
    )
    return create_engine(connection_url)
