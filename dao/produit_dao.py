from dao import Dao
from database_connection import database_connection
from entity import Produit


class ProduitDao(Dao):

    @staticmethod
    def create(entity: Produit) -> bool:
        try:
            connection = database_connection()
            sql = "insert into produit(name, description, image, id_categorie, id_admin)" \
                  " values (?, ?, ?, ?, ?) "
            cursor = connection.cursor()
            cursor.execute(sql, (entity.name, entity.description, entity.image,
                                 entity.id_categorie,
                                 entity.id_admin))
            cursor.close()
            connection.commit()
            connection.close()
            return True
        except Exception as e:
            print(f"Error {e}")
            return False

    @staticmethod
    def update(entity: Produit) -> bool:
        connection = database_connection()
        try:
            sql = "update produit " \
                  "set name=?," \
                  " description=?," \
                  " image=?," \
                  " id_categorie=?" \
                  " where id=?"
            cursor = connection.cursor()
            cursor.execute(sql, (entity.name,
                                 entity.description,
                                 entity.image,
                                 entity.id_categorie,
                                 entity.id)
                           )
            cursor.close()
            connection.commit()
            connection.close()
            return True
        except Exception as e:
            print(f"Error {e}")
            return False

    @staticmethod
    def delete(id_: int) -> bool:
        connection = database_connection()
        try:
            sql = "delete from produit where id=?"
            cursor = connection.cursor()
            cursor.execute(sql, (id_,))
            cursor.close()
            connection.commit()
            connection.close()
            return True
        except Exception as e:
            print(f"error {e}")
            return False

    @staticmethod
    def get_by_id(id_: int) -> Produit:
        connection = database_connection()
        sql = "select * from produit where id=?"
        cursor = connection.cursor()
        cursor.execute(sql, (id_,))
        result = cursor.fetchone()
        if result is None:
            return Produit()
        cursor.close()
        connection.close()
        return Produit(*result)

    @staticmethod
    def get_all() -> list[Produit]:
        connection = database_connection()
        sql = "select * from produit"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        if len(result) == 0:
            return result
        cursor.close()
        connection.close()
        return [Produit(*row) for row in result]
