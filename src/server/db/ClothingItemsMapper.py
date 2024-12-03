from server.db.Mapper import Mapper
from server.bo.ClothingItems import ClothingItem


class ClothingItemMapper(Mapper):
    """Mapper-Klasse für ClothingItem-Objekte."""

    def __init__(self):
        super().__init__()

    def find_all(self):
        """Auslesen aller ClothingItem-Objekte."""
        result = []
        cursor = self._get_connection().cursor()
        cursor.execute("SELECT * FROM clothing_item")
        tuples = cursor.fetchall()

        for (id, wardrobe_id, type_id, product_name, color, brand, season) in tuples:
            clothing_item = ClothingItem()
            clothing_item.set_id(id)
            clothing_item.set_wardrobe_id(wardrobe_id)
            clothing_item.set_type_id(type_id)
            clothing_item.set_product_name(product_name)
            clothing_item.set_color(color)
            clothing_item.set_brand(brand)
            clothing_item.set_season(season)
            result.append(clothing_item)

        self._get_connection().commit()
        cursor.close()
        return result

    def find_by_id(self, key):
        """Suchen eines ClothingItem-Objekts nach ID."""
        result = None
        cursor = self._get_connection().cursor()
        command = "SELECT * FROM clothing_item WHERE id='{}'".format(key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if tuples is not None and len(tuples) > 0:
            (id, wardrobe_id, type_id, product_name, color, brand, season) = tuples[0]
            result = ClothingItem()
            result.set_id(id)
            result.set_wardrobe_id(wardrobe_id)
            result.set_type_id(type_id)
            result.set_product_name(product_name)
            result.set_color(color)
            result.set_brand(brand)
            result.set_season(season)

        self._get_connection().commit()
        cursor.close()
        return result

    def find_by_wardrobe(self, wardrobe_id):
        """Suchen von ClothingItem-Objekten nach Wardrobe ID."""
        result = []
        cursor = self._get_connection().cursor()
        command = "SELECT * FROM clothing_item WHERE wardrobe_id='{}'".format(wardrobe_id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, wardrobe_id, type_id, product_name, color, brand, season) in tuples:
            clothing_item = ClothingItem()
            clothing_item.set_id(id)
            clothing_item.set_wardrobe_id(wardrobe_id)
            clothing_item.set_type_id(type_id)
            clothing_item.set_product_name(product_name)
            clothing_item.set_color(color)
            clothing_item.set_brand(brand)
            clothing_item.set_season(season)
            result.append(clothing_item)

        self._get_connection().commit()
        cursor.close()
        return result

    def insert(self, clothing_item):
        """Einfügen eines ClothingItem-Objekts in die Datenbank."""
        cursor = self._get_connection().cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM clothing_item")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is None:
                clothing_item.set_id(1)
            else:
                clothing_item.set_id(maxid[0] + 1)

        command = "INSERT INTO clothing_item (id, wardrobe_id, type_id, product_name, color, brand, season) VALUES ('{}','{}','{}','{}','{}','{}','{}')" \
            .format(clothing_item.get_id(), clothing_item.get_wardrobe_id(), clothing_item.get_type_id(),
                    clothing_item.get_product_name(), clothing_item.get_color(), 
                    clothing_item.get_brand(), clothing_item.get_season())
        cursor.execute(command)

        self._get_connection().commit()
        cursor.close()
        return clothing_item

    def update(self, clothing_item):
        """Aktualisieren eines ClothingItem-Objekts in der Datenbank."""
        cursor = self._get_connection().cursor()
        command = "UPDATE clothing_item SET product_name='{}', color='{}', brand='{}', season='{}' WHERE id='{}'"\
            .format(clothing_item.get_product_name(), clothing_item.get_color(), 
                    clothing_item.get_brand(), clothing_item.get_season(), clothing_item.get_id())
        cursor.execute(command)

        self._get_connection().commit()
        cursor.close()

    def delete(self, clothing_item):
        """Löschen eines ClothingItem-Objekts aus der Datenbank."""
        cursor = self._get_connection().cursor()
        command = "DELETE FROM clothing_item WHERE id='{}'".format(clothing_item.get_id())
        cursor.execute(command)

        self._get_connection().commit()
        cursor.close()

"""Zu Testzwecken können wir diese Datei bei Bedarf auch ausführen, 
um die grundsätzliche Funktion zu überprüfen.

Anmerkung: Nicht professionell aber hilfreich..."""
if (__name__ == "__main__"):
    with ClothingItemMapper() as mapper:
        result = mapper.find_all()
        for p in result:
            print(p)