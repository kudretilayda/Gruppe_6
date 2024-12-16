from src.server.db.Mapper import Mapper
from src.server.bo.clothingtype import ClothingType


class ClothingTypeMapper(Mapper):
    def find_all(self):
        results = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * FROM digital_wardrobe.clothing_type")
        tuples = cursor.fetchall()

        for (id, type_name, type_usage) in tuples:
            clothing_type = ClothingType()
            clothing_type.set_id(id)
            clothing_type.set_name(type_name)
            clothing_type.set_usage(type_usage)
            results.append(clothing_type)

        self._cnx.commit()
        cursor.close()
        return results

    def find_by_key(self, key):
        results = None
        cursor = self._cnx.cursor()
        command = f"SELECT * FROM clothing_type WHERE id={key}"
        cursor.execute(command)
        tuples = cursor.fetchall()

        if tuples:
            (id, type_name, type_usage) = tuples[0]
            results = ClothingType()
            results.set_id(id)
            results.set_name(type_name)
            results.set_usage(type_usage)

        self._cnx.commit()
        cursor.close()
        return results

    def insert(self, clothing_type):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM digital_wardrobe.clothing_type")
        max_id = cursor.fetchone()[0]
        clothing_type.set_id(max_id + 1 if max_id else 1)

        command = ("INSERT INTO digital_wardrobe.clothing_type (id, type_name, type_usage) "
                   "VALUES (%s, %s, %s)")
        data = (clothing_type.get_id(), clothing_type.get_name(), clothing_type.get_usage())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return clothing_type

    def update(self, clothing_type):
        cursor = self._cnx.cursor()
        command = ("UPDATE digital_wardrobe.clothing_type "
                   "SET type_name=%s, type_usage=%s WHERE id=%s")
        data = (clothing_type.get_name(), clothing_type.get_usage(), clothing_type.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def delete(self, clothing_type):
        cursor = self._cnx.cursor()
        command = f"DELETE FROM clothing_type WHERE id={clothing_type.get_id()}"
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()


if __name__ == "__main__":
    with ClothingTypeMapper() as mapper:
        result = mapper.find_all()
        for ct in result:
            print(ct)

