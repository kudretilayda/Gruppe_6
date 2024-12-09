from src.server.db.Mapper import Mapper
from src.server.bo.ClothingItem import ClothingItem


class ClothingItemMapper(Mapper):
    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * FROM digital_wardrobe.clothing_item")
        tuples = cursor.fetchall()

        for (id, wardrobe_id, clothing_type_id, clothing_item_name) in tuples:
            clothing_item = ClothingItem()
            clothing_item.set_id(id)
            clothing_item.set_wardrobe_id(wardrobe_id)
            clothing_item.set_clothing_type(clothing_type_id)
            clothing_item.set_item_name(clothing_item_name)
            result.append(clothing_item)

        self._cnx.commit()
        cursor.close()
        return result

    def find_by_key(self, key):
        result = None
        cursor = self._cnx.cursor()
        command = f"SELECT * FROM clothing_item WHERE id={key}"
        cursor.execute(command)
        tuples = cursor.fetchall()

        if tuples:
            (id, wardrobe_id, clothing_type_id, clothing_item_name) = tuples[0]
            result = ClothingItem()
            result.set_id(id)
            result.set_wardrobe_id(wardrobe_id)
            result.set_clothing_type(clothing_type_id)
            result.set_item_name(clothing_item_name)

        self._cnx.commit()
        cursor.close()
        return result

    def find_by_type(self, type_id):
        result = []
        cursor = self._cnx.cursor()
        command = ("SELECT id, name, type_id, style_id "
                   "FROM clothing_items WHERE type_id={}").format(
            type_id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, name, type_id, style_id) in tuples:
            clothing_item = ClothingItem()
            clothing_item.set_id(id)
            clothing_item.set_item_name(name)
            clothing_item.set_clothing_type(type_id)
            result.append(clothing_item)

        self._cnx.commit()
        cursor.close()
        return result

    def insert(self, clothing_item):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM digital_wardrobe.clothing_item")
        max_id = cursor.fetchone()[0]
        clothing_item.set_id(max_id + 1 if max_id else 1)

        command = ("INSERT INTO digital_wardrobe.clothing_item "
                   "(id, wardrobe_id, clothing_type_id, clothing_item_name) "
                   "VALUES (%s, %s, %s, %s)")
        data = (clothing_item.get_id(), clothing_item.get_wardrobe_id(),
                clothing_item.get_clothing_type_id(), clothing_item.get_name())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return clothing_item

    def update(self, clothing_item):
        cursor = self._cnx.cursor()
        command = ("UPDATE digital_wardrobe.clothing_item "
                   "SET wardrobe_id=%s, clothing_type_id=%s, clothing_item_name=%s "
                   "WHERE id=%s")
        data = (clothing_item.get_wardrobe_id(), clothing_item.get_clothing_type_id(),
                clothing_item.get_name(), clothing_item.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def delete(self, clothing_item):
        cursor = self._cnx.cursor()
        command = f"DELETE FROM clothing_item WHERE id={clothing_item.get_id()}"
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
