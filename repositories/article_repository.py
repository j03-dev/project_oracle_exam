from entity import Article
from repositories import Repository


class ArticleRepository(Repository):
    _name = "article"
    _migration_file = "article.sql"
    _object = Article
