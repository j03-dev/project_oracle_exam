from database_connection import database_connection
from entity import Article
from repositories import Repository


class ArticleRepository(Repository):
    _name = "article"
    _migration_file = "article.sql"
    _object = Article

    def get_by_category(self, category_name: str):
        connection = database_connection()
        sql = f"select * from {self._name} where caterory.name=?"
        cursor = connection.cursor()
        cursor.execute(sql, (category_name,))
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return [] if result is None else [Article(*row) for row in result]
