from server.db.Mapper import Mapper
from server.bo.ClothingItems import ClothingItem

class ClothingItemMapper(Mapper):
    """Mapper-Klasse für ClothingItem-Objekte"""

    def __init__(self):
        super().__init__()

    def find_all(self):
        """Alle Kleidungsstücke auslesen"""
        result = []
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM clothing_item")
        tuples = cursor.fetchall()

        for (id, wardrobe_id, type_id, name, description, created_at) in tuples:
            item = ClothingItem()
            item.set_id(id)
            item.set_wardrobe_id(wardrobe_id)
            item.set_type_id(type_id)
            item.set_name(name)
            item.set_description(description)
            result.append(item)

        self._connection.commit()
        cursor.close()
        return result

    def find_by_wardrobe(self, wardrobe_id):
        """Alle Kleidungsstücke eines Kleiderschranks auslesen"""
        result = []
        cursor = self._connection.cursor()
        command = "SELECT * FROM clothing_item WHERE wardrobe_id={}".format(wardrobe_id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, wardrobe_id, type_id, name, description, created_at) in tuples:
            item = ClothingItem()
            item.set_id(id)
            item.set_wardrobe_id(wardrobe_id)
            item.set_type_id(type_id)
            item.set_name(name)
            item.set_description(description)
            result.append(item)

        self._connection.commit()
        cursor.close()
        return result

    def insert(self, item):
        """Ein neues Kleidungsstück anlegen"""
        cursor = self._connection.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM clothing_item")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is not None:
                item.set_id(maxid[0] + 1)
            else:
                item.set_id(1)

        command = "INSERT INTO clothing_item (id, wardrobe_id, type_id, name, description) VALUES (%s, %s, %s, %s, %s)"
        data = (item.get_id(), item.get_wardrobe_id(), item.get_type_id(), 
                item.get_name(), item.get_description())
        cursor.execute(command, data)

        self._connection.commit()
        cursor.close()
        return item

    def update(self, item):
        """Ein Kleidungsstück aktualisieren"""
        cursor = self._connection.cursor()

        command = "UPDATE clothing_item SET wardrobe_id=%s, type_id=%s, name=%s, description=%s WHERE id=%s"
        data = (item.get_wardrobe_id(), item.get_type_id(), item.get_name(), 
                item.get_description(), item.get_id())
        cursor.execute(command, data)

        self._connection.commit()
        cursor.close()

    def delete(self, item):
        """Ein Kleidungsstück löschen"""
        cursor = self._connection.cursor()

        command = "DELETE FROM clothing_item WHERE id={}".format(item.get_id())
        cursor.execute(command)

        self._connection.commit()
        cursor.close()