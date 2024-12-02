# src/server/db/mapper/clothing_type_mapper.py

from server.db.Mapper import Mapper
from server.bo.ClothingType import ClothingType

class ClothingTypeMapper(Mapper):
    """Mapper-Klasse für ClothingType-Objekte."""

    def __init__(self):
        super().__init__()

    def find_all(self):
        """Auslesen aller ClothingType-Objekte."""
        result = []
        cursor = self._get_connection().cursor()
        cursor.execute("SELECT * FROM clothing_type")
        tuples = cursor.fetchall()

        for (id, type_name, type_description, category) in tuples:
            clothing_type = ClothingType()
            clothing_type.set_id(id)
            clothing_type.set_name(type_name)
            clothing_type.set_description(type_description)
            clothing_type.set_category(category)
            result.append(clothing_type)

        self._get_connection().commit()
        cursor.close()
        return result

    def find_by_id(self, key):
        """Suchen eines ClothingType-Objekts nach ID."""
        result = None
        cursor = self._get_connection().cursor()
        command = "SELECT * FROM clothing_type WHERE id='{}'".format(key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if tuples is not None and len(tuples) > 0:
            (id, type_name, type_description, category) = tuples[0]
            result = ClothingType()
            result.set_id(id)
            result.set_name(type_name)
            result.set_description(type_description)
            result.set_category(category)

        self._get_connection().commit()
        cursor.close()
        return result

    def find_by_category(self, category):
        """Suchen von ClothingType-Objekten nach Kategorie."""
        result = []
        cursor = self._get_connection().cursor()
        command = "SELECT * FROM clothing_type WHERE category='{}'".format(category)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, type_name, type_description, category) in tuples:
            clothing_type = ClothingType()
            clothing_type.set_id(id)
            clothing_type.set_name(type_name)
            clothing_type.set_description(type_description)
            clothing_type.set_category(category)
            result.append(clothing_type)

        self._get_connection().commit()
        cursor.close()
        return result

    def insert(self, clothing_type):
        """Einfügen eines ClothingType-Objekts in die Datenbank."""
        cursor = self._get_connection().cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM clothing_type")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is None:
                clothing_type.set_id(1)
            else:
                clothing_type.set_id(maxid[0] + 1)

        command = "INSERT INTO clothing_type (id, type_name, type_description, category) VALUES ('{}','{}','{}','{}')" \
            .format(clothing_type.get_id(), clothing_type.get_name(), 
                    clothing_type.get_description(), clothing_type.get_category())
        cursor.execute(command)

        self._get_connection().commit()
        cursor.close()
        return clothing_type

    def update(self, clothing_type):
        """Aktualisieren eines ClothingType-Objekts in der Datenbank."""
        cursor = self._get_connection().cursor()
        command = "UPDATE clothing_type SET type_name='{}', type_description='{}', category='{}' WHERE id='{}'"\
            .format(clothing_type.get_name(), clothing_type.get_description(), 
                    clothing_type.get_category(), clothing_type.get_id())
        cursor.execute(command)

        self._get_connection().commit()
        cursor.close()

    def delete(self, clothing_type):
        """Löschen eines ClothingType-Objekts aus der Datenbank."""
        cursor = self._get_connection().cursor()
        command = "DELETE FROM clothing_type WHERE id='{}'".format(clothing_type.get_id())
        cursor.execute(command)

        self._get_connection().commit()
        cursor.close()