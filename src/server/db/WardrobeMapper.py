from src.server.db.Mapper import Mapper
from src.server.bo.Wardrobe import Wardrobe


class WardrobeMapper(Mapper):
    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * FROM digital_wardrobe.wardrobe")
        tuples = cursor.fetchall()

        for (id, wardrobe_owner) in tuples:
            wardrobe = Wardrobe()
            wardrobe.set_id(id)
            wardrobe.set_owner(wardrobe_owner)
            result.append(wardrobe)

        self._cnx.commit()
        cursor.close()
        return result

    def find_by_key(self, key):
        result = None
        cursor = self._cnx.cursor()
        command = f"SELECT * FROM wardrobe WHERE id={key}"
        cursor.execute(command)
        tuples = cursor.fetchall()

        if tuples:
            (id, wardrobe_owner) = tuples[0]
            result = Wardrobe()
            result.set_id(id)
            result.set_owner(wardrobe_owner)

        self._cnx.commit()
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

        self._cnx().commit()
        cursor.close()
        return result

    def insert(self, wardrobe):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM digital_wardrobe.wardrobe")
        max_id = cursor.fetchone()[0]
        wardrobe.set_id(max_id + 1 if max_id else 1)

        command = ("INSERT INTO digital_wardrobe.wardrobe (id, wardrobe_owner) "
                   "VALUES (%s, %s)")
        data = (wardrobe.get_id(), wardrobe.get_owner())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return wardrobe

    def update(self, wardrobe):
        cursor = self._cnx.cursor()
        command = ("UPDATE digital_wardrobe.wardrobe "
                   "SET wardrobe_owner=%s WHERE id=%s")
        data = (wardrobe.get_owner(), wardrobe.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def delete(self, wardrobe):
        cursor = self._cnx.cursor()
        command = f"DELETE FROM wardrobe WHERE id={wardrobe.get_id()}"
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
