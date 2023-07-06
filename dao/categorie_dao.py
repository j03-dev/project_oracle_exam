from dao import Dao
from database_connection import database_connection
from entity import Categorie


class CategorieDao(Dao):
    @staticmethod
    def create(entity: Categorie) -> bool:
        try:
            connection = database_connection()
            sql = "insert into categorie(name, id_admin) values (?, ?)"
            connection.cursor().execute(sql, (entity.name, entity.id_admin))
            connection.commit()
            connection.close()
            return True
        except Exception as e:
            print(f"Error {e}")
            return False

    @staticmethod
    def update(entity: Categorie) -> bool:
        try:
            connection = database_connection()
            sql = "update categorie set name=? where id=?"
            connection.cursor().execute(sql, (entity.name, entity.id))
            connection.commit()
            connection.close()
            return True
        except Exception as e:
            print(f"Error {e}")
            return False

    @staticmethod
    def delete(id_: int) -> bool:
        try:
            connection = database_connection()
            sql = "delete from categorie where id=?"
            connection.cursor().execute(sql, (id_,))
            connection.commit()
            connection.close()
            return True
        except Exception as e:
            print("error {}", e)
            return False

    @staticmethod
    def get_by_id(id_: int) -> Categorie:
        connection = database_connection()
        sql = "select * from categorie where id=?"
        cursor = connection.cursor()
        cursor.execute(sql, (id_,))
        result = cursor.fetchone()
        if result is None:
            return Categorie()
        cursor.close()
        connection.close()
        return Categorie(*result)

    @staticmethod
    def get_all() -> list[Categorie]:
        connection = database_connection()
        sql = "select * from categorie"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        if len(result) == 0:
            return result
        cursor.close()
        connection.close()
        return [Categorie(*row) for row in result]
