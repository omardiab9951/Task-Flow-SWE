
import sqlite3
from werkzeug.security import generate_password_hash
from db import get_db_connection


def create_user(name, email, password):

    # Hash the password
    password_hash = generate_password_hash(password)

    # Open database connection
    conn = get_db_connection()

    try:
        cursor = conn.execute(
            """
            INSERT INTO users (name, email, password_hash)
            VALUES (?, ?, ?)
            """,
            (name, email, password_hash)
        )

        conn.commit()

        return cursor.lastrowid

    finally:
        conn.close()

def find_user_by_email(email):

    conn = get_db_connection()

    try:
        user = conn.execute(
            """
            SELECT * FROM users
            WHERE email = ?
            """,
            (email,)
        ).fetchone()

        return user

    finally:
        conn.close()