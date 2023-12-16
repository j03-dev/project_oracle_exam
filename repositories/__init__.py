from abc import ABC
from os import path
from typing import Any, Optional, List

from database_connection import database_connection


class Repository(ABC):
    _name = ""
    _migration_file = ""
    _object = None

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

    def create(self, entity: Any) -> bool:
        """
        Save information to the database.

        Args:
            entity (Any): The object containing information to be saved.

        Returns:
            bool: True if the save operation is successful, False otherwise.
        """
        try:
            fields = []
            values = []

            for k, v in entity.__dict__.items():
                if v is not None:
                    fields.append(k)
                    values.append(v)

            placeholders = ",".join("?" * len(values))
            insert_fields = ",".join(fields)

            # Build and execute the SQL query
            sql = f"INSERT INTO {self._name}({insert_fields}) VALUES ({placeholders})"
            connection = database_connection()
            cursor = connection.cursor()
            cursor.execute(sql, values)
            connection.commit()
            connection.close()

            return True
        except Exception as e:
            print(f"Error during save: {e}")
            return False

    def update(self, entity: Any) -> bool:
        """
        Update information in the database.

        Args:
           entity (Any): The object containing updated information.

        Returns:
           bool: True if the update is successful, False otherwise.
        """
        try:
            fields = []
            values = []
            entity_dict = entity.__dict__

            # Extract primary key and remove it from entity
            primary_key = entity_dict.pop("id")

            for k, v in entity_dict.items():
                if v is not None:
                    fields.append(f"{k}=?")
                    values.append(v)

            set_fields = ",".join(fields)

            # Add primary key to values for WHERE clause
            values.append(primary_key)

            # Build and execute the SQL query
            sql = f"UPDATE {self._name} SET {set_fields} WHERE id=?"
            connection = database_connection()
            cursor = connection.cursor()
            cursor.execute(sql, values)
            connection.commit()
            connection.close()

            return True
        except Exception as e:
            print(f"Error during update: {e}")
            return False

    def delete(self, id_: int) -> bool:
        """delete information on the database"""
        connection = database_connection()
        try:
            sql = f"delete from {self._name} where id=?"
            cursor = connection.cursor()
            cursor.execute(sql, (id_,))
            cursor.close()
            connection.commit()
            connection.close()
            return True
        except Exception as e:
            print(f"error {e}")
            return False

    def get_by_id(self, id_: int) -> Optional[object]:
        """
        Retrieve an entity from the database based on its ID.

        Args:
            id_ (int): The ID of the entity to retrieve.

        Returns:
            Optional[object]: The retrieved entity object, or None if not found.
        """
        connection = database_connection()
        sql = f"SELECT * FROM {self._name} WHERE id=?"
        cursor = connection.cursor()
        cursor.execute(sql, (id_,))
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        return None if result is None else self._object(*result)

    def get_all(self) -> List[object]:
        """
        Retrieve a list of all elements from the database.

        Returns:
            List[object]: A list containing entity objects.
        """
        connection = database_connection()
        sql = f"SELECT * FROM {self._name}"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return [] if not result else [self._object(*row) for row in result]
