from src.server.bo.Kleidungstyp import Kleidungstyp
from src.server.db.Mapper import Mapper


class ClothingTypeMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):
        """Auslesen aller Kleidungstypen.
        : return eine Sammlung mit ClothingType-Objekten.
        """
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT id, name, category FROM clothing_types")
        tuples = cursor.fetchall()

        for (id, name, category) in tuples:
            clothing_type = Kleidungstyp()
            clothing_type.set_id(id)
            clothing_type.set_name(name)
            clothing_type.set_category(category)
            result.append(clothing_type)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_category(self, category):
        """Auslesen aller Kleidungstypen einer bestimmten Kategorie.

        :param category Die gesuchte Kategorie
        :return Eine Sammlung von ClothingType-Objekten
        """
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, name, category FROM clothing_types WHERE category='{}'".format(category)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, name, category) in tuples:
            clothing_type = Kleidungstyp()
            clothing_type.set_id(id)
            clothing_type.set_name(name)
            clothing_type.set_category(category)
            result.append(clothing_type)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, key):
        """Suchen eines Kleidungstyps mit vorgegebener ID.

        :param key Primärschlüsselattribut
        :return ClothingType-Objekt, das dem übergebenen Schlüssel entspricht
        """
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, name, category FROM clothing_types WHERE id={}".format(key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if tuples[0] is not None:
            (id, name, category) = tuples[0]
            clothing_type = Kleidungstyp()
            clothing_type.set_id(id)
            clothing_type.set_name(name)
            clothing_type.set_category(category)
            result = clothing_type

        self._cnx.commit()
        cursor.close()

        return result

    def insert(self, clothing_type):
        """Einfügen eines ClothingType-Objekts in die Datenbank.

        : param clothing_type das zu speichernde Objekt

        : return das bereits übergebene Objekt, jedoch mit ggf. korrigierter ID.
        """
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM clothing_types")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            clothing_type.set_id(maxid[0] + 1)

        command = "INSERT INTO clothing_types (id, name, category) VALUES (%s, %s, %s)"
        data = (clothing_type.get_id(), clothing_type.get_name(), clothing_type.get_category())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return clothing_type

    def update(self, clothing_type):
        """Wiederholtes Schreiben eines Objekts in die Datenbank.

        :param clothing_type das Objekt, das in die DB geschrieben werden soll
        """
        cursor = self._cnx.cursor()

        command = "UPDATE clothing_types SET name=%s, category=%s WHERE id=%s"
        data = (clothing_type.get_name(), clothing_type.get_category(), clothing_type.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def delete(self, clothing_type):
        """Löschen der Daten eines ClothingType-Objekts aus der Datenbank.

        :param clothing_type das aus der DB zu löschende "Objekt"
        """
        cursor = self._cnx.cursor()

        command = "DELETE FROM clothing_types WHERE id={}".format(clothing_type.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

if (__name__ == "__main__"):
    with ClothingTypeMapper() as mapper:
        result = mapper.find_all()
        for ct in result:
            print(ct)
