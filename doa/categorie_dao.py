from doa import Dao


class CategorieDao(Dao):
    def create(self, T) -> bool:
        sql = "insert into categorie(name) values (?)"
        self.conn.cursor().execute(sql)

    def update(self, _id: int) -> bool:
        sql = "update categorie set name=? where id=?"
        pass

    def delete(self, _id: int) -> bool:
        sql = "delete from categorie where id=?"
        pass

    def get_by_id(self, _id: int) -> object:
        sql = "select * from categorie where id=?"

    def get_all(self) -> object:
        sql = "select * from categorie"
        pass
