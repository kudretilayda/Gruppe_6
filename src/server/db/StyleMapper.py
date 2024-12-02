from server.db.Mapper import Mapper
from server.bo.Style import Style

class StyleMapper(Mapper):
    """Mapper-Klasse für Style-Objekte."""

    def __init__(self):
        super().__init__()

    def find_all(self):
        """Auslesen aller Style-Objekte."""
        result = []
        cursor = self._get_connection().cursor()
        cursor.execute("SELECT * FROM style")
        tuples = cursor.fetchall()

        for (id, style_name, style_description, created_by) in tuples:
            style = Style()
            style.set_id(id)
            style.set_name(style_name)
            style.set_description(style_description)
            style.set_created_by(created_by)
            result.append(style)

        self._get_connection().commit()
        cursor.close()
        return result

    def find_by_id(self, key):
        """Suchen eines Style-Objekts nach ID."""
        result = None
        cursor = self._get_connection().cursor()
        command = "SELECT * FROM style WHERE id='{}'".format(key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if tuples is not None and len(tuples) > 0:
            (id, style_name, style_description, created_by) = tuples[0]
            result = Style()
            result.set_id(id)
            result.set_name(style_name)
            result.set_description(style_description)
            result.set_created_by(created_by)

        self._get_connection().commit()
        cursor.close()
        return result

    def find_by_creator(self, person_id):
        """Suchen von Style-Objekten nach Ersteller."""
        result = []
        cursor = self._get_connection().cursor()
        command = "SELECT * FROM style WHERE created_by='{}'".format(person_id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, style_name, style_description, created_by) in tuples:
            style = Style()
            style.set_id(id)
            style.set_name(style_name)
            style.set_description(style_description)
            style.set_created_by(created_by)
            result.append(style)

        self._get_connection().commit()
        cursor.close()
        return result

    def insert(self, style):
        """Einfügen eines Style-Objekts in die Datenbank."""
        cursor = self._get_connection().cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM style")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is None:
                style.set_id(1)
            else:
                style.set_id(maxid[0] + 1)

        command = "INSERT INTO style (id, style_name, style_description, created_by) VALUES ('{}','{}','{}','{}')" \
            .format(style.get_id(), style.get_name(), style.get_description(), style.get_created_by())
        cursor.execute(command)

        self._get_connection().commit()
        cursor.close()
        return style

    def update(self, style):
        """Aktualisieren eines Style-Objekts in der Datenbank."""
        cursor = self._get_connection().cursor()
        command = "UPDATE style SET style_name='{}', style_description='{}' WHERE id='{}'"\
            .format(style.get_name(), style.get_description(), style.get_id())
        cursor.execute(command)

        self._get_connection().commit()
        cursor.close()

    def delete(self, style):
        """Löschen eines Style-Objekts aus der Datenbank."""
        cursor = self._get_connection().cursor()
        # Zuerst alle zugehörigen Constraints löschen
        command = "DELETE FROM constraint_rule WHERE style_id='{}'".format(style.get_id())
        cursor.execute(command)
        # Dann den Style selbst löschen
        command = "DELETE FROM style WHERE id='{}'".format(style.get_id())
        cursor.execute(command)

        self._get_connection().commit()
        cursor.close()