from typing import Any

from oracledb import Connection


class Dao:
    def __init__(self, conn: Connection):
        self.conn = conn

    def create(self, entity: Any) -> bool:
        pass

    def delete(self, _id: int) -> object:
        pass

    def update(self, entity: Any) -> bool:
        pass

    def get_by_id(self, _id: int) -> object:
        pass

    def get_all(self) -> list[object]:
        pass
