from dao import Dao
from entity import Produit


class ProduitDao(Dao):
    def create(self, entity: Produit) -> bool:
        try:
            sql = "insert into produit(name, description, image, id_categorie, id_admin)" \
                  " values (:name, :description, :image,:id_categorie, :id_admin) "
            cursor = self.conn.cursor()
            cursor.execute(sql, name=entity.name, description=entity.description, image=entity.image,
                           id_categorie=entity.id_categorie,
                           id_admin=entity.id_admin)
            cursor.close()
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error {e}")
            return False

    def update(self, entity: Produit) -> bool:
        try:
            sql = "update produit " \
                  "set name=:name," \
                  " description=:description," \
                  " image=:image," \
                  " id_categorie=:id_categorie" \
                  " where id=:id"
            cursor = self.conn.cursor()
            cursor.execute(sql, name=entity.name, description=entity.description, image=entity.image,
                           id_categorie=entity.id_categorie,
                           id=entity.id)
            cursor.close()
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error {e}")
            return False

    def delete(self, id_: int) -> bool:
        try:
            sql = "delete from produit where id=:id"
            cursor = self.conn.cursor()
            cursor.execute(sql, id=id_)
            cursor.close()
            self.conn.commit()
            return True
        except Exception as e:
            print(f"error {e}")
            return False

    def get_by_id(self, id_: int) -> Produit:
        sql = "select * from produit where id=:id"
        cursor = self.conn.cursor()
        cursor.execute(sql, id=id_)
        result = cursor.fetchone()
        if result is None:
            return Produit()
        cursor.close()
        return Produit(*result)

    def get_all(self) -> list[Produit]:
        sql = "select * from produit"
        cursor = self.conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        if len(result) == 0:
            return result
        cursor.close()
        return [Produit(*row) for row in result]
