from server.db.Mapper import Mapper
from server.bo.Wardrobe import Wardrobe

class WardrobeMapper(Mapper):
    """Mapper-Klasse für Wardrobe-Objekte"""

    def __init__(self):
        super().__init__()

    def find_all(self):
        """Alle Wardrobe-Objekte auslesen"""
        result = []
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM wardrobe")
        tuples = cursor.fetchall()

        for (id, owner_id, created_at) in tuples:
            wardrobe = Wardrobe()
            wardrobe.set_id(id)
            wardrobe.set_owner_id(owner_id)
            result.append(wardrobe)

        self._connection.commit()
        cursor.close()

        return result

    def find_by_id(self, id):
        """Einen Wardrobe anhand seiner ID auslesen"""
        result = None
        cursor = self._connection.cursor()
        command = "SELECT * FROM wardrobe WHERE id={}".format(id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, owner_id, created_at) = tuples[0]
            wardrobe = Wardrobe()
            wardrobe.set_id(id)
            wardrobe.set_owner_id(owner_id)
            result = wardrobe
        except IndexError:
            result = None

        self._connection.commit()
        cursor.close()
        return result

    def find_by_owner_id(self, owner_id):
        """Einen Wardrobe anhand der Owner ID auslesen"""
        result = None
        cursor = self._connection.cursor()
        command = "SELECT * FROM wardrobe WHERE owner_id={}".format(owner_id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, owner_id, created_at) = tuples[0]
            wardrobe = Wardrobe()
            wardrobe.set_id(id)
            wardrobe.set_owner_id(owner_id)
            result = wardrobe
        except IndexError:
            result = None

        self._connection.commit()
        cursor.close()
        return result

    def insert(self, wardrobe):
        """Einen neuen Wardrobe anlegen"""
        cursor = self._connection.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM wardrobe")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is not None:
                wardrobe.set_id(maxid[0] + 1)
            else:
                wardrobe.set_id(1)

        command = "INSERT INTO wardrobe (id, owner_id) VALUES (%s, %s)"
        data = (wardrobe.get_id(), wardrobe.get_owner_id())
        cursor.execute(command, data)

        self._connection.commit()
        cursor.close()
        return wardrobe

    def update(self, wardrobe):
        """Einen Wardrobe aktualisieren"""
        cursor = self._connection.cursor()

        command = "UPDATE wardrobe SET owner_id=%s WHERE id=%s"
        data = (wardrobe.get_owner_id(), wardrobe.get_id())
        cursor.execute(command, data)

        self._connection.commit()
        cursor.close()

    def delete(self, wardrobe):
        """Einen Wardrobe löschen"""
        cursor = self._connection.cursor()

        command = "DELETE FROM wardrobe WHERE id={}".format(wardrobe.get_id())
        cursor.execute(command)

        self._connection.commit()
        cursor.close()