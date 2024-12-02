from src.server.db.Mapper import Mapper
from src.server.bo.Wardrobe import Wardrobe


class WardrobeMapper(Mapper):
    """Mapper-Klasse für Wardrobe-Objekte."""

    def _init_(self):
        super()._init_()

    def find_all(self):
        """Auslesen aller Wardrobe-Objekte."""
        result = []
        cursor = self._cnx().cursor()
        cursor.execute("SELECT * FROM wardrobe")
        tuples = cursor.fetchall()

        for (id, person_id, owner_name, created_at) in tuples:
            wardrobe = Wardrobe()
            wardrobe.set_id(id)
            wardrobe.set_person_id(person_id)
            wardrobe.set_owner_name(owner_name)
            wardrobe.set_creation_date(created_at)
            result.append(wardrobe)

        self._cnx().commit()
        cursor.close()
        return result

    def find_by_key(self, key):
        """Suchen eines Wardrobe-Objekts nach ID."""
        result = None
        cursor = self._cnx().cursor()
        command = "SELECT * FROM wardrobe WHERE id='{}'".format(key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if tuples is not None and len(tuples) > 0:
            (id, person_id, owner_name, created_at) = tuples[0]
            result = Wardrobe()
            result.set_id(id)
            result.set_person_id(person_id)
            result.set_owner_name(owner_name)
            result.set_creation_date(created_at)

        self._cnx().commit()
        cursor.close()
        return result

    def find_by_person_id(self, person_id):
        """Suchen eines Wardrobe-Objekts nach Person ID."""
        result = None
        cursor = self._cnx().cursor()
        command = "SELECT * FROM wardrobe WHERE person_id='{}'".format(person_id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if tuples is not None and len(tuples) > 0:
            (id, person_id, owner_name, created_at) = tuples[0]
            result = Wardrobe()
            result.set_id(id)
            result.set_person_id(person_id)
            result.set_owner_name(owner_name)
            result.set_creation_date(created_at)

        self._cnx().commit()
        cursor.close()
        return result

    def insert(self, wardrobe):
        """Einfügen eines Wardrobe-Objekts in die Datenbank."""
        cursor = self._cnx().cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM wardrobe")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is None:
                wardrobe.set_id(1)
            else:
                wardrobe.set_id(maxid[0] + 1)

        command = "INSERT INTO wardrobe (id, person_id, owner_name) VALUES ('{}','{}','{}')" \
            .format(wardrobe.get_id(), wardrobe.get_person_id(), wardrobe.get_owner_name())
        cursor.execute(command)

        self._cnx().commit()
        cursor.close()
        return wardrobe

    def update(self, wardrobe):
        """Aktualisieren eines Wardrobe-Objekts in der Datenbank."""
        cursor = self._cnx().cursor()
        command = "UPDATE wardrobe SET owner_name='{}' WHERE id='{}'"\
            .format(wardrobe.get_owner_name(), wardrobe.get_id())
        cursor.execute(command)

        self._cnx().commit()
        cursor.close()

    def delete(self, wardrobe):
        """Löschen eines Wardrobe-Objekts aus der Datenbank."""
        cursor = self._cnx().cursor()
        command = "DELETE FROM wardrobe WHERE id='{}'".format(wardrobe.get_id())
        cursor.execute(command)

        self._cnx().commit()
        cursor.close()
