# src/server/db/mapper/ClothingItemMapper.py

from server.db.Mapper import Mapper
from server.bo.ClothingItem import ClothingItem

class ClothingItemMapper(Mapper):
    """Mapper-Klasse, die ClothingItem-Objekte auf eine relationale
    Datenbank abbildet."""
    
    def __init__(self):
        super().__init__()

    def find_by_wardrobe_id(self, wardrobe_id):
        """Suchen aller Kleidungsstücke eines Kleiderschranks."""
        result = []
        with self._cursor() as cursor:
            command = "SELECT * FROM clothing_item WHERE wardrobe_id=%s"
            cursor.execute(command, (wardrobe_id,))
            tuples = cursor.fetchall()
            for (id, wardrobe_id, type_id, name, create_time) in tuples:
                clothing_item = ClothingItem()
                clothing_item.set_id(id)
                clothing_item.set_wardrobe_id(wardrobe_id)
                clothing_item.set_type_id(type_id)
                clothing_item.set_name(name)
                clothing_item.set_create_time(create_time)
                result.append(clothing_item)
        return result

    def find_by_key(self, key):
        """Suchen eines Kleidungsstücks mit vorgegebener ID."""
        with self._cursor() as cursor:
            command = "SELECT * FROM clothing_item WHERE id=%s"
            cursor.execute(command, (key,))
            tuples = cursor.fetchall()
            try:
                (id, wardrobe_id, type_id, name, create_time) = tuples[0]
                clothing_item = ClothingItem()
                clothing_item.set_id(id)
                clothing_item.set_wardrobe_id(wardrobe_id)
                clothing_item.set_type_id(type_id)
                clothing_item.set_name(name)
                clothing_item.set_create_time(create_time)
                return clothing_item
            except IndexError:
                return None

    def insert(self, clothing_item):
        """Einfügen eines Kleidungsstücks in die Datenbank."""
        with self._cursor() as cursor:
            command = "INSERT INTO clothing_item (id, wardrobe_id, type_id, name) VALUES (%s, %s, %s, %s)"
            data = (clothing_item.get_id(), clothing_item.get_wardrobe_id(),
                   clothing_item.get_type_id(), clothing_item.get_name())
            cursor.execute(command, data)
            self._cnx.commit()
            return clothing_item

    def update(self, clothing_item):
        """Aktualisieren eines Kleidungsstücks in der Datenbank."""
        with self._cursor() as cursor:
            command = "UPDATE clothing_item SET wardrobe_id=%s, type_id=%s, name=%s WHERE id=%s"
            data = (clothing_item.get_wardrobe_id(), clothing_item.get_type_id(),
                   clothing_item.get_name(), clothing_item.get_id())
            cursor.execute(command, data)
            self._cnx.commit()
            return clothing_item

    def delete(self, clothing_item):
        """Löschen eines Kleidungsstücks aus der Datenbank."""
        with self._cursor() as cursor:
            command = "DELETE FROM clothing_item WHERE id=%s"
            cursor.execute(command, (clothing_item.get_id(),))
            self._cnx.commit()