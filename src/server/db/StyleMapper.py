from server.db.Mapper import Mapper
from server.bo.Style import Style

class StyleMapper(Mapper):
    """Mapper-Klasse für Style-Objekte"""

    def __init__(self):
        super().__init__()

    def find_all(self):
        """Alle Styles auslesen"""
        result = []
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM style")
        tuples = cursor.fetchall()

        for (id, name, description, features, created_at) in tuples:
            style = Style()
            style.set_id(id)
            style.set_name(name)
            style.set_description(description)
            style.set_features(features)
            result.append(style)

        self._connection.commit()
        cursor.close()
        return result

    def find_by_id(self, id):
        """Einen Style anhand seiner ID auslesen"""
        result = None
        cursor = self._connection.cursor()
        command = "SELECT * FROM style WHERE id={}".format(id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, name, description, features, created_at) = tuples[0]
            style = Style()
            style.set_id(id)
            style.set_name(name)
            style.set_description(description)
            style.set_features(features)
            result = style
        except IndexError:
            result = None

        self._connection.commit()
        cursor.close()
        return result

    def insert(self, style):
        """Einen neuen Style anlegen"""
        cursor = self._connection.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM style")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is not None:
                style.set_id(maxid[0] + 1)
            else:
                style.set_id(1)

        command = "INSERT INTO style (id, name, description, features) VALUES (%s, %s, %s, %s)"
        data = (style.get_id(), style.get_name(), style.get_description(), style.get_features())
        cursor.execute(command, data)

        self._connection.commit()
        cursor.close()
        return style

    def update(self, style):
        """Einen Style aktualisieren"""
        cursor = self._connection.cursor()

        command = "UPDATE style SET name=%s, description=%s, features=%s WHERE id=%s"
        data = (style.get_name(), style.get_description(), style.get_features(), style.get_id())
        cursor.execute(command, data)

        self._connection.commit()
        cursor.close()

    def delete(self, style):
        """Einen Style löschen"""
        cursor = self._connection.cursor()

        command = "DELETE FROM style WHERE id={}".format(style.get_id())
        cursor.execute(command)

        self._connection.commit()
        cursor.close()