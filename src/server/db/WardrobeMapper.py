from server.db.Mapper import Mapper
from server.bo.Wardrobe import Wardrobe
import uuid

class WardrobeMapper(Mapper):
    def __init__(self):
        super().__init__()

    def find_by_person(self, person_id):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * FROM wardrobe WHERE person_id=%s", (person_id,))
        tuples = cursor.fetchall()

        try:
            (id, person_id, owner_name, created_at) = tuples[0]
            wardrobe = Wardrobe()
            wardrobe.set_id(id)
            wardrobe.set_person_id(person_id)
            wardrobe.set_owner_name(owner_name)
            wardrobe.set_created_at(created_at)
            result = wardrobe
        except IndexError:
            result = None

        self._cnx.commit()
        cursor.close()
        return result

    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * FROM wardrobe")
        tuples = cursor.fetchall()

        for (id, person_id, owner_name, created_at) in tuples:
            wardrobe = Wardrobe()
            wardrobe.set_id(id)
            wardrobe.set_person_id(person_id)
            wardrobe.set_owner_name(owner_name)
            wardrobe.set_created_at(created_at)
            result.append(wardrobe)

        self._cnx.commit()
        cursor.close()
        return result

    def insert(self, wardrobe):
        cursor = self._cnx.cursor()

        if not wardrobe.get_id():
            wardrobe.set_id(str(uuid.uuid4()))

        command = "INSERT INTO wardrobe (id, person_id, owner_name) VALUES (%s,%s,%s)"
        data = (wardrobe.get_id(), wardrobe.get_person_id(), wardrobe.get_owner_name())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return wardrobe

    def update(self, wardrobe):
        cursor = self._cnx.cursor()
        command = "UPDATE wardrobe SET person_id=%s, owner_name=%s WHERE id=%s"
        data = (wardrobe.get_person_id(), wardrobe.get_owner_name(), wardrobe.get_id())
        cursor.execute(command, data)
        self._cnx.commit()
        cursor.close()

    def delete(self, wardrobe):
        cursor = self._cnx.cursor()
        command = "DELETE FROM wardrobe WHERE id=%s"
        cursor.execute(command, (wardrobe.get_id(),))
        self._cnx.commit()
        cursor.close()

if __name__ == "__main__":
    with WardrobeMapper() as mapper:
        result = mapper.find_all()
        for w in result:
            print(w)