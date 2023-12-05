import sqlite3


def database_connection():
    try:
        conn = sqlite3.connect("/mnt/d/Project/project_oracle/blog.db")
        return conn
    except Exception as e:
        raise Exception(f"failed to connect to the database raison {e}")
