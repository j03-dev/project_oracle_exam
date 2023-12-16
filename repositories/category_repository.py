from entity import Categorie
from repositories import Repository


class CategoryRepository(Repository):
    _name = "category"
    _migration_file = "category.sql"
    _object = Categorie
