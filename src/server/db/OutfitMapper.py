from src.server.db.Mapper import Mapper
from src.server.bo.Outfit import Outfit


class OutfitMapper(Mapper):
    def find_all(self):
        result = []
        cursor = self._cnx().cursor()
        cursor.execute("SELECT * FROM digital_wardrobe.outfit")
        tuples = cursor.fetchall()

        for (outfit_id, outfit_name, style_id, created_by, created_at) in tuples:
            outfit = Outfit()
            outfit.set_id(outfit_id)
            outfit.set_name(outfit_name)
            outfit.set_style(style_id)
            outfit.set_created_by(created_by)
            outfit.set_creation_date(created_at)
            result.append(outfit)

        self._get_connection().commit()
        cursor.close()
        return result

    def find_by_id(self, key):
        result = None
        cursor = self._cnx().cursor()
        command = "SELECT * FROM outfit WHERE id='{}'".format(key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if tuples is not None and len(tuples) > 0:
            (outfit_id, outfit_name, style_id, created_by, created_at) = tuples[0]
            result = Outfit()
            result.set_id(outfit_id)
            result.set_name(outfit_name)
            result.set_style(style_id)
            result.set_created_by(created_by)
            result.set_creation_date(created_at)

        self._cnx().commit()
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
            outfit.set_created_by(created_by)
            outfit.set_creation_date(created_at)
            result.append(outfit)

        self._cnx().commit()
        cursor.close()
        return result

    def find_items_by_outfit(self, outfit_id):
        """Auslesen aller Kleidungsstücke eines Outfits."""
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
        cursor = self._cnx().cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM digital_wardrobe.outfit")
        tuples = cursor.fetchall()

        for (max_id) in tuples:
            if max_id[0] is None:
                outfit.set_id(1)
            else:
                outfit.set_id(max_id[0] + 1)

        command = "INSERT INTO outfit (id, outfit_name, style_id, created_by) VALUES ('{}','{}','{}','{}')" \
            .format(outfit.get_id(), outfit.get_name(), outfit.get_style_id(), outfit.get_created_by())
        cursor.execute(command)

        self._cnx().commit()
        cursor.close()
        return outfit

    def update(self, outfit):
        """Aktualisieren eines Outfit-Objekts in der Datenbank."""
        cursor = self._cnx().cursor()
        command = "UPDATE outfit SET outfit_name='{}', style_id='{}' WHERE id='{}'"\
            .format(outfit.get_name(), outfit.get_style_id(), outfit.get_id())
        cursor.execute(command)

        self._cnx().commit()
        cursor.close()

    def delete(self, outfit):
        """Löschen eines Outfit-Objekts aus der Datenbank."""
        cursor = self._cnx().cursor()
        # Zuerst die Verknüpfungen in der outfit_items Tabelle löschen
        command = "DELETE FROM outfit_items WHERE outfit_id='{}'".format(outfit.get_id())
        cursor.execute(command)
        # Dann das Outfit selbst löschen
        command = "DELETE FROM outfit WHERE id='{}'".format(outfit.get_id())
        cursor.execute(command)

        self._cnx().commit()
        cursor.close()

    def add_item_to_outfit(self, outfit_id, clothing_item_id):
        """Fügt ein Kleidungsstück zu einem Outfit hinzu."""
        cursor = self._cnx().cursor()
        command = "INSERT INTO outfit_items (outfit_id, clothing_item_id) VALUES ('{}','{}')" \
            .format(outfit_id, clothing_item_id)
        cursor.execute(command)
        self._cnx().commit()
        cursor.close()

    def remove_item_from_outfit(self, outfit_id, clothing_item_id):
        """Entfernt ein Kleidungsstück aus einem Outfit."""
        cursor = self._cnx().cursor()
        command = "DELETE FROM outfit_items WHERE outfit_id='{}' AND clothing_item_id='{}'" \
            .format(outfit_id, clothing_item_id)
        cursor.execute(command)
        self._cnx().commit()
        cursor.close()
