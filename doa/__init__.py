from typing import Any

from oracledb import Connection


class Dao:
    """
    Data Access Object
    get access of your database here
    """

    def __init__(self, conn: Connection):
        """
        :param conn: conn is Connection object from oracledb import Connection
        """
        self.conn: Connection = conn

    def create(self, entity: Any) -> bool:
        """
        save information on the database
        :param entity:
        :return: bool
        """
        pass

    def delete(self, id_: int) -> bool:
        """delete information on the database"""
        pass

    def update(self, entity: Any) -> bool:
        """update information on the database"""
        pass

    def get_by_id(self, id_: int) -> object:
        """
        get entity from database with here id
        :param id_:
        :return: entity object
        """
        pass

    def get_all(self) -> list[object]:
        """
        get all list of element in database
        :return: list of entity object
        """
        pass
