from doa import Dao
from entity import Produit
from setting import database_connection


class ProduitDao(Dao):
    def create(self, entity: Produit) -> bool:
        try:
            sql = """insert into produit(name, description, image, id_provenance, id_categorie, id_admin) values 
            (:name, :description, :image, :id_provenance, :id_categorie, :id_admin)
            """
            self.conn.cursor().execute(sql, name=entity.name, description=entity.description, image=entity.image,
                                       id_provenance=entity.id_provenance, id_categorie=entity.id_categorie,
                                       id_admin=entity.id_admin)
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error {e}")
            return False

    def update(self, entity: Produit) -> bool:
        try:
            sql = "update produit set name=:name, description=:description, image=:image where id=:id"
            self.conn.cursor().execute(sql, name=entity.name, description=entity.description, image=entity.image,
                                       id=entity.id)
            self.conn.commit()
        except Exception as e:
            print(f"Error {e}")
            return False

    def delete(self, _id: int) -> bool:
        try:
            sql = "delete from produit where id=:id"
            self.conn.cursor().execute(sql, id=_id)
            self.conn.commit()
            return True
        except Exception as e:
            print(f"error {e}")
            return False

    def get_by_id(self, _id: int) -> Produit:
        sql = "select * from produit where id=:id"
        cursor = self.conn.cursor()
        cursor.execute(sql, id=_id)
        result = cursor.fetchone()
        if result is None:
            return Produit()
        id_, name, description, image, id_provenance, id_categorie, id_admin = result
        cursor.close()
        return Produit(id_, name, description, image, id_provenance, id_categorie, id_admin)

    def get_all(self) -> list[Produit]:
        sql = "select * from produit"
        cursor = self.conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        if len(result) == 0:
            return result
        cursor.close()
        return [Produit(id_, name, description, image, id_provenance, id_categorie, id_admin) for
                id_, name, description, image, id_provenance, id_categorie, id_admin in result]


if __name__ == "__main__":
    conn = database_connection()
    produit_dao = ProduitDao(conn)

    produits = produit_dao.get_all()

    for prod in produits:
        print(prod.name)
