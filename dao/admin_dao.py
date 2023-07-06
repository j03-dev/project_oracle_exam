from dao import Dao
from database_connection import database_connection
from entity import Admin


class AdminDao(Dao):
    @staticmethod
    def get_by_email(email) -> Admin:
        connection = database_connection()
        sql = "select * from admin where email=:email"
        cursor = connection.cursor()
        cursor.execute(sql, (email,))
        result = cursor.fetchone()

        if result is None:
            return Admin()

        id_, email, password = result
        cursor.close()
        connection.close()

        return Admin(id_, email, password)
