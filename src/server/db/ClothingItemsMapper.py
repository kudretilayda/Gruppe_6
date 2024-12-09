from server.db.Mapper import Mapper
from server.bo.ClothingItems import ClothingItems
import uuid

class ClothingItemsMapper(Mapper):
    def __init__(self):
        super().__init__()

    def find_by_wardrobe(self, wardrobe_id):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * FROM clothing_item WHERE wardrobe_id=%s", (wardrobe_id,))
        tuples = cursor.fetchall()

        for (id, wardrobe_id, clothing_type_id, product_name, color, brand, season) in tuples:
            item = ClothingItems()
            item.set_id(id)
            item.set_wardrobe_id(wardrobe_id)
            item.set_clothing_type_id(clothing_type_id)
            item.set_product_name(product_name)
            item.set_color(color)
            item.set_brand(brand)
            item.set_season(season)
            result.append(item)

        self._cnx.commit()
        cursor.close()
        return result

    def find_by_id(self, item_id):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * FROM clothing_item WHERE id=%s", (item_id,))
        tuples = cursor.fetchall()

        try:
            (id, wardrobe_id, clothing_type_id, product_name, color, brand, season) = tuples[0]
            item = ClothingItems()
            item.set_id(id)
            item.set_wardrobe_id(wardrobe_id)
            item.set_clothing_type_id(clothing_type_id)
            item.set_product_name(product_name)
            item.set_color(color)
            item.set_brand(brand)
            item.set_season(season)
            return item
        except IndexError:
            return None
        finally:
            self._cnx.commit()
            cursor.close()

    def insert(self, item):
        cursor = self._cnx.cursor()

        if not item.get_id():
            item.set_id(str(uuid.uuid4()))

        command = """INSERT INTO clothing_item 
                    (id, wardrobe_id, clothing_type_id, product_name, color, brand, season)
                    VALUES (%s,%s,%s,%s,%s,%s,%s)"""
        data = (item.get_id(), item.get_wardrobe_id(), item.get_clothing_type_id(),
                item.get_product_name(), item.get_color(), item.get_brand(),
                item.get_season())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return item

    def update(self, item):
        cursor = self._cnx.cursor()
        command = """UPDATE clothing_item 
                    SET wardrobe_id=%s, clothing_type_id=%s, product_name=%s,
                        color=%s, brand=%s, season=%s
                    WHERE id=%s"""
        data = (item.get_wardrobe_id(), item.get_clothing_type_id(),
                item.get_product_name(), item.get_color(), item.get_brand(),
                item.get_season(), item.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def delete(self, item):
        cursor = self._cnx.cursor()
        command = "DELETE FROM clothing_item WHERE id=%s"
        cursor.execute(command, (item.get_id(),))
        self._cnx.commit()
        cursor.close()
