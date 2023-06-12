from oracledb import Connection
from oracledb.exceptions import OperationalError


def database_connection():
    username = "joe"
    password = "joejoe"
    hostname = "192.168.63.28:1521"
    db_name = "projet_oracle_db"

    try:
        dns = f"{username}/{password}@{hostname}/{db_name}"
        conn = Connection(dns)
        return conn
    except OperationalError:
        raise Exception("failed to connect to the database")


if __name__ == "__main__":
    database_connection()
