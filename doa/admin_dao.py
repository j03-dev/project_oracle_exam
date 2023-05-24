from doa import Dao
from entity import Admin
from setting import database_connection


class AdminDao(Dao):
    def get_by_email(self, email) -> Admin:
        sql = "select * from admin where email=:email"
        cursor = self.conn.cursor()
        cursor.execute(sql, email=email)
        result = cursor.fetchone()

        if result is None:
            return Admin()

        id_, email, password = result
        cursor.close()

        return Admin(id_, email, password)


if __name__ == "__main__":
    conn = database_connection()
    admin_dao = AdminDao(conn)
    admin = admin_dao.get_by_email("24nomeniavo@gmail.com")
    print(admin)
