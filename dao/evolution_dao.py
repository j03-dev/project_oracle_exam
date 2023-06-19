from dao import Dao
from entity import Evolution


class EvolutionDao(Dao):
    def create(self, entity: Evolution) -> bool:
        try:
            sql = "insert into evolution(date, prix, id_produit)" \
                  "values (:date, :prix, :id_produit)"
            cursor = self.conn.cursor()
            cursor.execute(sql, data=entity.date, prix=entity.prix, id_produit=entity.id_produit)
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error {e}")
            return False

    def update(self, entity: Evolution) -> bool:
        try:
            sql = "update evolution set date=:date prix=:prix where id=:id"
            cursor = self.conn.cursor()
            cursor.execute(sql, date=entity.date, prix=entity.prix, id=entity.id)
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error {e}")
            return False

    def delete(self, id_: int) -> bool:
        try:
            sql = "delete from evolution where id=:id"
            self.conn.cursor().execute(sql, id=id_)
            self.conn.commit()
            return True
        except Exception as e:
            print(f"error {e}")
            return False

    def get_by_id(self, id_: int) -> Evolution:
        sql = "select * from evolution where id=:id"
        cursor = self.conn.cursor()
        cursor.execute(sql, id=id_)
        result = cursor.fetchone()
        if result is None:
            return Evolution()
        cursor.close()
        return Evolution(*result)

    def get_all(self) -> list[Evolution]:
        sql = "select * from evolution"
        cursor = self.conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        if len(result) == 0:
            return result
        cursor.close()
        return [Evolution(*row) for row in result]
