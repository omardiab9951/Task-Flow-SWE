
import sqlite3
from pathlib import Path

# Database file path
DATABASE_PATH = "taskflow.db"


def get_db_connection():
    conn = sqlite3.connect(DATABASE_PATH)

    # Return rows as dictionary-like objects
    conn.row_factory = sqlite3.Row

    # Enable foreign key enforcement
    conn.execute("PRAGMA foreign_keys = ON")

    return conn
