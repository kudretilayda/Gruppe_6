from server.db.Mapper import Mapper
from server.bo.ClothingType import ClothingType
import uuid

class ClothingTypeMapper(Mapper):
    def __init__(self):
        super().__init__()

    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * FROM clothing_type")
        tuples = cursor.fetchall()

        for (id, type_name, type_description, category) in tuples:
            clothing_type = ClothingType()
            clothing_type.set_id(id)
            clothing_type.set_type_name(type_name)
            clothing_type.set_type_description(type_description)
            clothing_type.set_category(category)
            result.append(clothing_type)

        self._cnx.commit()
        cursor.close()
        return result

    def find_by_id(self, type_id):
        cursor = self._cnx.cursor()
        command = "SELECT * FROM clothing_type WHERE id=%s"
        cursor.execute(command, (type_id,))
        tuples = cursor.fetchall()

        try:
            (id, type_name, type_description, category) = tuples[0]
            clothing_type = ClothingType()
            clothing_type.set_id(id)
            clothing_type.set_type_name(type_name)
            clothing_type.set_type_description(type_description)
            clothing_type.set_category(category)
            return clothing_type
        except IndexError:
            return None
        finally:
            self._cnx.commit()
            cursor.close()

    def insert(self, clothing_type):
        cursor = self._cnx.cursor()

        if not clothing_type.get_id():
            clothing_type.set_id(str(uuid.uuid4()))

        command = """INSERT INTO clothing_type 
                    (id, type_name, type_description, category) 
                    VALUES (%s,%s,%s,%s)"""
        data = (clothing_type.get_id(), clothing_type.get_type_name(),
                clothing_type.get_type_description(), clothing_type.get_category())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return clothing_type

    def update(self, clothing_type):
        cursor = self._cnx.cursor()
        command = """UPDATE clothing_type 
                    SET type_name=%s, type_description=%s, category=%s 
                    WHERE id=%s"""
        data = (clothing_type.get_type_name(), clothing_type.get_type_description(),
                clothing_type.get_category(), clothing_type.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def delete(self, clothing_type):
        cursor = self._cnx.cursor()
        command = "DELETE FROM clothing_type WHERE id=%s"
        cursor.execute(command, (clothing_type.get_id(),))
        self._cnx.commit()
        cursor.close()
