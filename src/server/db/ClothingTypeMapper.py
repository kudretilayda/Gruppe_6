from server.db.Mapper import Mapper
from server.bo.ClothingType import ClothingType, Category

class ClothingTypeMapper(Mapper):
    def __init__(self):
        super().__init__()

    def find_all(self):
        cursor = self._get_connection().cursor()
        cursor.execute("SELECT * FROM clothing_type")
        tuples = cursor.fetchall()
        result = []

        for (id, type_name, type_description, category) in tuples:
            clothing_type = ClothingType()
            clothing_type.set_id(id)
            clothing_type.set_type_name(type_name)
            clothing_type.set_type_description(type_description)
            clothing_type.set_category(Category(category))
            result.append(clothing_type)

        self._get_connection().commit()
        cursor.close()
        return result

    def find_by_id(self, type_id):
        cursor = self._get_connection().cursor()
        command = "SELECT * FROM clothing_type WHERE id=%s"
        cursor.execute(command, (type_id,))
        tuples = cursor.fetchall()

        try:
            (id, type_name, type_description, category) = tuples[0]
            clothing_type = ClothingType()
            clothing_type.set_id(id)
            clothing_type.set_type_name(type_name)
            clothing_type.set_type_description(type_description)
            clothing_type.set_category(Category(category))
            return clothing_type
        except IndexError:
            return None
        finally:
            self._get_connection().commit()
            cursor.close()

    def find_by_category(self, category: Category):
        cursor = self._get_connection().cursor()
        command = "SELECT * FROM clothing_type WHERE category=%s"
        cursor.execute(command, (category.value,))
        tuples = cursor.fetchall()
        result = []

        for (id, type_name, type_description, category) in tuples:
            clothing_type = ClothingType()
            clothing_type.set_id(id)
            clothing_type.set_type_name(type_name)
            clothing_type.set_type_description(type_description)
            clothing_type.set_category(Category(category))
            result.append(clothing_type)

        self._get_connection().commit()
        cursor.close()
        return result

    def insert(self, clothing_type):
        cursor = self._get_connection().cursor()
        
        command = """INSERT INTO clothing_type (id, type_name, type_description, category) 
                    VALUES (%s, %s, %s, %s)"""
        data = (clothing_type.get_id(), clothing_type.get_type_name(),
                clothing_type.get_type_description(), clothing_type.get_category().value)
        cursor.execute(command, data)

        self._get_connection().commit()
        cursor.close()
        return clothing_type

    def update(self, clothing_type):
        cursor = self._get_connection().cursor()
        command = """UPDATE clothing_type 
                    SET type_name=%s, type_description=%s, category=%s 
                    WHERE id=%s"""
        data = (clothing_type.get_type_name(), clothing_type.get_type_description(),
                clothing_type.get_category().value, clothing_type.get_id())
        cursor.execute(command, data)

        self._get_connection().commit()
        cursor.close()

    def delete(self, clothing_type):
        cursor = self._get_connection().cursor()
        cursor.execute("DELETE FROM clothing_type WHERE id=%s", (clothing_type.get_id(),))
        self._get_connection().commit()
        cursor.close()
