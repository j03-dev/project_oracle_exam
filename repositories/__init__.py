from abc import ABC
from os import path
from typing import Any

from database_connection import database_connection


class Repository(ABC):
    _name = ""
    _migration_file = ""

    def set_migration_path(self):
        absolute_path = path.abspath(".")
        return path.join(absolute_path, self._migration_file)

    def migration(self):
        try:
            conn = database_connection()
            with open(self.set_migration_path(), "r") as migration_file:
                conn.execute(migration_file.read())
            print(self._name, "migrate success")
            conn.close()
        except Exception as e:
            raise Exception(f"Migration failed cause {e}")

    def drop(self):
        try:
            conn = database_connection()
            conn.execute(f"drop table {self._name}")
            conn.close()
        except Exception as e:
            raise Exception(f"Drop table failed cause {e}")

    @staticmethod
    def create(entity: Any) -> bool:
        """
        save information on the database
        :param entity:
        :return: bool
        """
        pass

    @staticmethod
    def delete(id_: int) -> bool:
        """delete information on the database"""
        pass

    @staticmethod
    def update(entity: Any) -> bool:
        """update information on the database"""
        pass

    @staticmethod
    def get_by_id(id_: int) -> object:
        """
        get entity from database with here id
        :param id_:
        :return: entity object
        """
        pass

    @staticmethod
    def get_all() -> list[object]:
        """
        get all list of element in database
        :return: list of entity object
        """
        pass
