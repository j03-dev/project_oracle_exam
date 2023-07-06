from typing import Any


class Dao:
    """
    Data Access Object
    get access of your database here
    """

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
