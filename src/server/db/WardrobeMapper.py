from server.db.Mapper import Mapper
from server.bo.Wardrobe import Wardrobe
import uuid

class WardrobeMapper(Mapper):
    def __init__(self):
        super().__init__()

    def find_all(self):
        result = []
        cursor = self._get_connection().cursor()
        cursor.execute("SELECT * FROM wardrobe")
        tuples = cursor.fetchall()

        for (id, person_id, owner_name, created_at) in tuples:
            wardrobe = Wardrobe()
            wardrobe.set_id(id)
            wardrobe.set_person_id(person_id)
            wardrobe.set_owner_name(owner_name)
            wardrobe.set_created_at(created_at)
            result.append(wardrobe)

        self._get_connection().commit()
        cursor.close()
        return result

    def find_by_id(self, wardrobe_id):
        cursor = self._get_connection().cursor()
        command = "SELECT * FROM wardrobe WHERE id=%s"
        cursor.execute(command, (wardrobe_id,))
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

        self._get_connection().commit()
        cursor.close()
        return result

    def find_by_person_id(self, person_id):
        result = None
        cursor = self._get_connection().cursor()
        command = "SELECT * FROM wardrobe WHERE person_id=%s"
        cursor.execute(command, (person_id,))
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

        self._get_connection().commit()
        cursor.close()
        return result

    def get_clothes_by_wardrobe_id(self, wardrobe_id):
        """Alle Kleidungsstücke eines Kleiderschranks ausgeben"""
        from server.db.ClothingItemsMapper import ClothingItemMapper
        mapper = ClothingItemMapper()
        return mapper.find_by_wardrobe(wardrobe_id)

    def insert(self, wardrobe):
        cursor = self._get_connection().cursor()

        if not wardrobe.get_id():
            wardrobe.set_id(str(uuid.uuid4()))

        command = "INSERT INTO wardrobe (id, person_id, owner_name) VALUES (%s,%s,%s)"
        data = (wardrobe.get_id(), wardrobe.get_person_id(), wardrobe.get_owner_name())

        cursor.execute(command, data)
        self._get_connection().commit()
        cursor.close()
        return wardrobe

    def update(self, wardrobe):
        cursor = self._get_connection().cursor()

        command = "UPDATE wardrobe SET person_id=%s, owner_name=%s WHERE id=%s"
        data = (wardrobe.get_person_id(), wardrobe.get_owner_name(), wardrobe.get_id())

        cursor.execute(command, data)
        self._get_connection().commit()
        cursor.close()

    def delete(self, wardrobe):
        cursor = self._get_connection().cursor()
        command = "DELETE FROM wardrobe WHERE id=%s"
        cursor.execute(command, (wardrobe.get_id(),))
        self._get_connection().commit()
        cursor.close()

if __name__ == "__main__":
    with WardrobeMapper() as mapper:
        result = mapper.find_all()
        for w in result:
            print(w)
