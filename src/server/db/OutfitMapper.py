from src.server.db.Mapper import Mapper
from src.server.bo.Outfit import Outfit


class OutfitMapper(Mapper):
    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * FROM digital_wardrobe.outfit")
        tuples = cursor.fetchall()

        for (id, outfit_name, style_id) in tuples:
            outfit = Outfit()
            outfit.set_id(id)
            outfit.set_name(outfit_name)
            outfit.set_style_id(style_id)
            result.append(outfit)

        self._cnx.commit()
        cursor.close()
        return result

    def find_by_key(self, key):
        result = None
        cursor = self._cnx.cursor()
        command = f"SELECT * FROM outfit WHERE id={key}"
        cursor.execute(command)
        tuples = cursor.fetchall()

        if tuples:
            (id, outfit_name, style_id) = tuples[0]
            result = Outfit()
            result.set_id(id)
            result.set_name(outfit_name)
            result.set_style_id(style_id)

        self._cnx.commit()
        cursor.close()
        return result

    def find_by_style(self, style_id):
        result = []
        cursor = self._cnx().cursor()
        command = "SELECT * FROM outfit WHERE style_id='{}'".format(style_id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, outfit_name, style_id, created_by, created_at) in tuples:
            outfit = Outfit()
            outfit.set_id(id)
            outfit.set_name(outfit_name)
            outfit.set_style(style_id)
            result.append(outfit)

        self._cnx().commit()
        cursor.close()
        return result

    def find_items_by_outfit(self, outfit_id):
        result = []
        cursor = self._cnx().cursor()
        command = "SELECT ci.* FROM clothing_item ci " \
                 "JOIN outfit_items oi ON ci.id = oi.clothing_item_id " \
                 "WHERE oi.outfit_id='{}'".format(outfit_id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, wardrobe_id, type_id, product_name, color, brand, season) in tuples:
            clothing_item = clothing_item()
            clothing_item.set_id(id)
            clothing_item.set_wardrobe_id(wardrobe_id)
            clothing_item.set_type_id(type_id)
            clothing_item.set_product_name(product_name)
            clothing_item.set_color(color)
            clothing_item.set_brand(brand)
            clothing_item.set_season(season)
            result.append(clothing_item)

        self._cnx().commit()
        cursor.close()
        return result

    def insert(self, outfit):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM digital_wardrobe.outfit")
        max_id = cursor.fetchone()[0]
        outfit.set_id(max_id + 1 if max_id else 1)

        command = ("INSERT INTO digital_wardrobe.outfit (id, outfit_name, style_id) "
                   "VALUES (%s, %s, %s)")
        data = (outfit.get_id(), outfit.get_name(), outfit.get_style_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return outfit

    def update(self, outfit):
        cursor = self._cnx.cursor()
        command = ("UPDATE digital_wardrobe.outfit "
                   "SET outfit_name=%s, style_id=%s "
                   "WHERE id=%s")
        data = (outfit.get_name(), outfit.get_style_id(), outfit.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def delete(self, outfit):
        cursor = self._cnx.cursor()
        command = f"DELETE FROM outfit WHERE id={outfit.get_id()}"
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

    def add_item_to_outfit(self, outfit_id, clothing_item_id):
        cursor = self._cnx().cursor()
        command = "INSERT INTO outfit_items (outfit_id, clothing_item_id) VALUES ('{}','{}')" \
            .format(outfit_id, clothing_item_id)
        cursor.execute(command)
        self._cnx().commit()
        cursor.close()

    def remove_item_from_outfit(self, outfit_id, clothing_item_id):
        cursor = self._cnx().cursor()
        command = "DELETE FROM outfit_items WHERE outfit_id='{}' AND clothing_item_id='{}'" \
            .format(outfit_id, clothing_item_id)
        cursor.execute(command)
        self._cnx().commit()
        cursor.close()

