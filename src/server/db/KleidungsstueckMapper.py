from src.server.bo.Kleidungsstueck import Kleidungsstueck
from src.server.db.Mapper import Mapper


class ClothingItemMapper(Mapper):
    """Mapper-Klasse, die ClothingItem-Objekte auf eine relationale
    Datenbank abbildet. Hierzu wird eine Reihe von Methoden zur Verfügung
    gestellt, mit deren Hilfe z.B. Objekte gesucht, erzeugt, modifiziert und
    gelöscht werden können.
    """

    def __init__(self):
        super().__init__()

    def find_all(self):
        """Auslesen aller Kleidungsstücke.

        :return Eine Sammlung mit ClothingItem-Objekten.
        """
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT id, name, type_id, style_id, size, color, brand FROM clothing_items")
        tuples = cursor.fetchall()

        for (id, name, type_id, style_id, size, color, brand) in tuples:
            clothing_item = Kleidungsstueck()
            clothing_item.set_id(id)
            clothing_item.set_name(name)
            clothing_item.set_type_id(type_id)
            clothing_item.set_style_id(style_id)
            clothing_item.set_size(size)
            clothing_item.set_color(color)
            clothing_item.set_brand(brand)
            result.append(clothing_item)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_style(self, style_id):
        """Auslesen aller Kleidungsstücke eines bestimmten Styles.

        :param style_id ID des gesuchten Styles
        :return Eine Sammlung von ClothingItem-Objekten
        """
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, name, type_id, style_id, size, color, brand FROM clothing_items WHERE style_id={}".format(style_id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, name, type_id, style_id, size, color, brand) in tuples:
            clothing_item = Kleidungsstueck()
            clothing_item.set_id(id)
            clothing_item.set_name(name)
            clothing_item.set_type_id(type_id)
            clothing_item.set_style_id(style_id)
            clothing_item.set_size(size)
            clothing_item.set_color(color)
            clothing_item.set_brand(brand)
            result.append(clothing_item)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_type(self, type_id):
        """Auslesen aller Kleidungsstücke eines bestimmten Typs.

        :param type_id ID des gesuchten Kleidungstyps
        :return Eine Sammlung von ClothingItem-Objekten
        """
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, name, type_id, style_id, size, color, brand FROM clothing_items WHERE type_id={}".format(type_id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, name, type_id, style_id, size, color, brand) in tuples:
            clothing_item = Kleidungsstueck()
            clothing_item.set_id(id)
            clothing_item.set_name(name)
            clothing_item.set_type_id(type_id)
            clothing_item.set_style_id(style_id)
            clothing_item.set_size(size)
            clothing_item.set_color(color)
            clothing_item.set_brand(brand)
            result.append(clothing_item)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, key):
        """Suchen eines Kleidungsstücks mit vorgegebener ID.

        :param key Primärschlüssel Attribut
        :return ClothingItem-Objekt, das dem übergebenen Schlüssel entspricht
        """
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, name, type_id, style_id, size, color, brand FROM clothing_items WHERE id={}".format(key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if tuples[0] is not None:
            (id, name, type_id, style_id, size, color, brand) = tuples[0]
            clothing_item = Kleidungsstueck()
            clothing_item.set_id(id)
            clothing_item.set_name(name)
            clothing_item.set_type_id(type_id)
            clothing_item.set_style_id(style_id)
            clothing_item.set_size(size)
            clothing_item.set_color(color)
            clothing_item.set_brand(brand)
            result = clothing_item

        self._cnx.commit()
        cursor.close()

        return result