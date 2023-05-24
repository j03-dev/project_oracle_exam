from doa import Dao
from entity import Categorie
from setting import database_connection


class CategorieDao(Dao):
    def create(self, entity: Categorie) -> bool:
        try:
            sql = "insert into categorie(name, id_admin) values (:name, :id_admin)"
            self.conn.cursor().execute(sql, name=entity.name, id_admin=entity.id_admin)
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error {e}")
            return False

    def update(self, entity: Categorie) -> bool:
        try:
            sql = "update categorie set name=:name where id=:id"
            self.conn.cursor().execute(sql, name=entity.name, id=entity.id)
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error {e}")
            return False

    def delete(self, _id: int) -> bool:
        try:
            sql = "delete from categorie where id=:id"
            self.conn.cursor().execute(sql, id=_id)
            self.conn.commit()
            return True
        except Exception as e:
            print("error {}", e)
            return False

    def get_by_id(self, _id: int) -> Categorie:
        sql = "select * from categorie where id=:id"
        cursor = self.conn.cursor()
        cursor.execute(sql, id=_id)
        result = cursor.fetchone()
        if result is None:
            return Categorie()
        id_, name, id_admin = result
        cursor.close()
        return Categorie(id_, name, id_admin)

    def get_all(self) -> list[Categorie]:
        sql = "select * from categorie"
        cursor = self.conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        if len(result) == 0:
            return result
        cursor.close()
        return [Categorie(id_, name, id_admin) for id_, name, id_admin in result]


if __name__ == "__main__":
    conn = database_connection()
    categorie_dao = CategorieDao(conn)
    # categorie = Categorie(name="Élevage", id_admin=1)
    # print(categorie_dao.create(categorie))

    categorie = categorie_dao.get_all()
    print(categorie[0].name)

    print(categorie_dao.get_by_id(2))
