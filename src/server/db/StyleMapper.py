from src.server.bo.Style import Style
from src.server.db.Mapper import Mapper


class StyleMapper(Mapper):
    """Mapper-Klasse, die Style-Objekte auf eine relationale
    Datenbank abbildet. Hierzu wird eine Reihe von Methoden zur Verfügung
    gestellt, mit deren Hilfe z.B. Objekte gesucht, erzeugt, modifiziert und
    gelöscht werden können.
    """

    def __init__(self):
        super().__init__()

    def find_all(self):
        """Auslesen aller Styles.

        : return eine Sammlung mit Style-Objekten.
        """
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT id, name, description FROM styles")
        tuples = cursor.fetchall()

        for (id, name, description) in tuples:
            style = Style()
            style.set_id(id)
            style.set_name(name)
            style.set_description(description)
            result.append(style)

        self._cnx.commit()
        cursor.close()
        return result

    def find_by_name(self, name):
        """Auslesen eines Styles mit gegebenem Namen.

        :param name Name des gesuchten Styles
        :return Style-Objekt, das dem übergebenen Namen entspricht
        """
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT id, name, description FROM styles WHERE name LIKE '{}' ORDER BY id".format(name)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if tuples[0] is not None:
            (id, name, description) = tuples[0]
            style = Style()
            style.set_id(id)
            style.set_name(name)
            style.set_description(description)
            result = style

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, key):
        """Suchen eines Styles mit vorgegebener ID.

        :param key Primärschlüsselattribut
        :return Style-Objekt, das dem übergebenen Schlüssel entspricht
        """
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, name, description FROM styles WHERE id={}".format(key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if tuples[0] is not None:
            (id, name, description) = tuples[0]
            style = Style()
            style.set_id(id)
            style.set_name(name)
            style.set_description(description)
            result = style

        self._cnx.commit()
        cursor.close()

        return result

    def insert(self, style):
        """Einfügen eines Style-Objekts in die Datenbank.

        :param style das zu speichernde Objekt
        :return das bereits übergebene Objekt, jedoch mit ggf. korrigierter ID.
        """
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM styles")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            style.set_id(maxid[0] + 1)

        command = "INSERT INTO styles (id, name, description) VALUES (%s, %s, %s)"
        data = (style.get_id(), style.get_name(), style.get_description())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return style

    def update(self, style):
        """Wiederholtes Schreiben eines Objekts in die Datenbank.

        :param style das Objekt, das in die DB geschrieben werden soll
        """
        cursor = self._cnx.cursor()

        command = "UPDATE styles SET name=%s, description=%s WHERE id=%s"
        data = (style.get_name(), style.get_description(), style.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def delete(self, style):
        """Löschen der Daten eines Style-Objekts aus der Datenbank.

        :param style das aus der DB zu löschende "Objekt"
        """
        cursor = self._cnx.cursor()

        command = "DELETE FROM styles WHERE id={}".format(style.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

if (__name__ == "__main__"):
    with StyleMapper() as mapper:
        result = mapper.find_all()
        for s in result:
            print(s)
