from entity import User
from repositories import Repository


class UserRepository(Repository):
    _name = "user"
    _migration_file = "user.sql"
    _object = User
