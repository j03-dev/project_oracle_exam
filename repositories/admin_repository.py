from database_connection import database_connection
from entity import Admin
from repositories import Repository


class AdminRepository(Repository):
    _name = "admin"
    _migration_file = "admin.sql"

    @staticmethod
    def get_by_email(email) -> Admin:
        connection = database_connection()
        sql = "select * from admin where email=:email"
        cursor = connection.cursor()
        cursor.execute(sql, (email,))
        result = cursor.fetchone()

        if result is None:
            return Admin()

        cursor.close()
        connection.close()

        return Admin(*result)
