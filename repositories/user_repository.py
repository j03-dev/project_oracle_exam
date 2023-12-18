from database_connection import database_connection
from entity import User
from repositories import Repository


class UserRepository(Repository):
    _name = "user"
    _migration_file = "user.sql"
    _object = User

    def get_by_email(self, email: str) -> User:
        connection = database_connection()
        sql = f"select * from {self._name} where email=?"
        cursor = connection.cursor()
        cursor.execute(sql, (email,))
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        return None if result is None else self._object(*result)
