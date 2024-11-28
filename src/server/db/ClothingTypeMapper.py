# src/server/db/mapper/ClothingTypeMapper.py

from server.db.Mapper import Mapper
from server.bo.ClothingType import ClothingType

class ClothingTypeMapper(Mapper):
    """Mapper-Klasse, die ClothingType-Objekte auf eine relationale
    Datenbank abbildet."""
    
    def __init__(self):
        super().__init__()

    def find_all(self):
        """Auslesen aller Kleidungstypen."""
        result = []
        with self._cursor() as cursor:
            cursor.execute("SELECT * FROM clothing_type")
            tuples = cursor.fetchall()
            for (id, name, usage, create_time) in tuples:
                clothing_type = ClothingType()
                clothing_type.set_id(id)
                clothing_type.set_name(name)
                clothing_type.set_usage(usage)
                clothing_type.set_create_time(create_time)
                result.append(clothing_type)
        return result

    def find_by_key(self, key):
        """Suchen eines Kleidungstyps mit vorgegebener ID."""
        with self._cursor() as cursor:
            command = "SELECT * FROM clothing_type WHERE id=%s"
            cursor.execute(command, (key,))
            tuples = cursor.fetchall()
            try:
                (id, name, usage, create_time) = tuples[0]
                clothing_type = ClothingType()
                clothing_type.set_id(id)
                clothing_type.set_name(name)
                clothing_type.set_usage(usage)
                clothing_type.set_create_time(create_time)
                return clothing_type
            except IndexError:
                return None

    def insert(self, clothing_type):
        """Einfügen eines Kleidungstyps in die Datenbank."""
        with self._cursor() as cursor:
            command = "INSERT INTO clothing_type (id, name, usage) VALUES (%s, %s, %s)"
            data = (clothing_type.get_id(), clothing_type.get_name(), 
                   clothing_type.get_usage())
            cursor.execute(command, data)
            self._cnx.commit()
            return clothing_type

    def update(self, clothing_type):
        """Aktualisieren eines Kleidungstyps in der Datenbank."""
        with self._cursor() as cursor:
            command = "UPDATE clothing_type SET name=%s, usage=%s WHERE id=%s"
            data = (clothing_type.get_name(), clothing_type.get_usage(),
                   clothing_type.get_id())
            cursor.execute(command, data)
            self._cnx.commit()
            return clothing_type

    def delete(self, clothing_type):
        """Löschen eines Kleidungstyps aus der Datenbank."""
        with self._cursor() as cursor:
            command = "DELETE FROM clothing_type WHERE id=%s"
            cursor.execute(command, (clothing_type.get_id(),))
            self._cnx.commit()