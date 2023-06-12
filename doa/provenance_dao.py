from doa import Dao
from entity import Provenance
from setting import database_connection


class ProvenanceDao(Dao):
    def create(self, entity: Provenance) -> bool:
        sql = "insert into provenance(name, id_admin) values (:name, :id_admin)"
        self.conn.cursor().execute(sql, name=entity.name, id_admin=entity.id_admin)
        self.conn.commit()
        return True

    def update(self, entity: Provenance) -> bool:
        try:
            sql = "update provenance set name=:name where id=:id"
            self.conn.cursor().execute(sql, name=entity.name, id=entity.id)
            self.conn.commit()
            return True
        except Exception as e:
            print(f"error {e}")
            return False

    def delete(self, _id: int) -> bool:
        try:
            sql = "delete from provenance where id=:id"
            self.conn.cursor().execute(sql, id=_id)
            self.conn.commit()
            return True
        except Exception as e:
            print(f"error {e}")
            return False

    def get_by_id(self, _id: int) -> Provenance:
        sql = "select * from provenance where id=:id"
        cursor = self.conn.cursor()
        cursor.execute(sql, id=_id)
        result = cursor.fetchone()
        if result is None:
            return Provenance()
        id_, name, id_admin = result
        cursor.close()
        return Provenance(id_, name, id_admin)

    def get_all(self) -> list[Provenance]:
        sql = "select * from provenance"
        cursor = self.conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        if len(result) == 0:
            return result
        cursor.close()
        return [Provenance(id_, name, id_admin) for id_, name, id_admin in result]


if __name__ == "__main__":
    conn = database_connection()
    provenance_dao = ProvenanceDao(conn)
    # provenance = Provenance(name="NosyBe", id_admin=1)
    # print(provenance_dao.create(provenance))

    provenances = provenance_dao.get_all()
    for pro in provenances:
        print(pro)
