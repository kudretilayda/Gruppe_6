# src/server/db/mapper/WardrobeMapper.py

from server.db.Mapper import Mapper
from server.bo.Wardrobe import Wardrobe

class WardrobeMapper(Mapper):
    """Mapper-Klasse, die Wardrobe-Objekte auf eine relationale
    Datenbank abbildet."""
    
    def __init__(self):
        super().__init__()

    def find_by_person_id(self, person_id):
        """Suchen eines Kleiderschranks einer bestimmten Person."""
        with self._cursor() as cursor:
            command = "SELECT * FROM wardrobe WHERE person_id=%s"
            cursor.execute(command, (person_id,))
            tuples = cursor.fetchall()
            try:
                (id, person_id, create_time) = tuples[0]
                wardrobe = Wardrobe()
                wardrobe.set_id(id)
                wardrobe.set_person_id(person_id)
                wardrobe.set_create_time(create_time)
                return wardrobe
            except IndexError:
                return None

    def insert(self, wardrobe):
        """Einfügen eines Kleiderschranks in die Datenbank."""
        with self._cursor() as cursor:
            command = "INSERT INTO wardrobe (id, person_id) VALUES (%s, %s)"
            data = (wardrobe.get_id(), wardrobe.get_person_id())
            cursor.execute(command, data)
            self._cnx.commit()
            return wardrobe

    def update(self, wardrobe):
        """Aktualisieren eines Kleiderschranks in der Datenbank."""
        with self._cursor() as cursor:
            command = "UPDATE wardrobe SET person_id=%s WHERE id=%s"
            data = (wardrobe.get_person_id(), wardrobe.get_id())
            cursor.execute(command, data)
            self._cnx.commit()
            return wardrobe

    def delete(self, wardrobe):
        """Löschen eines Kleiderschranks aus der Datenbank."""
        with self._cursor() as cursor:
            command = "DELETE FROM wardrobe WHERE id=%s"
            cursor.execute(command, (wardrobe.get_id(),))
            self._cnx.commit()