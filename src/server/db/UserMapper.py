# src/server/db/mapper/UserMapper.py

from server.db.Mapper import Mapper
from server.bo.User import Person

class UserMapper(Mapper):
    """Mapper-Klasse für Person-Objekte."""

    def __init__(self):
        super().__init__()

    def find_all(self):
        """Auslesen aller Person-Objekte."""
        result = []
        cursor = self._get_connection().cursor()
        cursor.execute("SELECT * FROM person")
        tuples = cursor.fetchall()

        for (id, google_id, firstname, lastname, nickname, created_at) in tuples:
            person = Person()
            person.set_id(id)
            person.set_google_id(google_id)
            person.set_firstname(firstname)
            person.set_lastname(lastname)
            person.set_nickname(nickname)
            person.set_creation_date(created_at)
            result.append(person)

        self._get_connection().commit()
        cursor.close()
        return result

    def find_by_id(self, key):
        """Suchen eines Person-Objekts nach ID."""
        result = None
        cursor = self._get_connection().cursor()
        command = "SELECT * FROM person WHERE id='{}'".format(key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if tuples is not None and len(tuples) > 0:
            (id, google_id, firstname, lastname, nickname, created_at) = tuples[0]
            result = Person()
            result.set_id(id)
            result.set_google_id(google_id)
            result.set_firstname(firstname)
            result.set_lastname(lastname)
            result.set_nickname(nickname)
            result.set_creation_date(created_at)

        self._get_connection().commit()
        cursor.close()
        return result

    def find_by_google_id(self, google_id):
        """Suchen eines Person-Objekts nach Google ID."""
        result = None
        cursor = self._get_connection().cursor()
        command = "SELECT * FROM person WHERE google_id='{}'".format(google_id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if tuples is not None and len(tuples) > 0:
            (id, google_id, firstname, lastname, nickname, created_at) = tuples[0]
            result = Person()
            result.set_id(id)
            result.set_google_id(google_id)
            result.set_firstname(firstname)
            result.set_lastname(lastname)
            result.set_nickname(nickname)
            result.set_creation_date(created_at)

        self._get_connection().commit()
        cursor.close()
        return result

    def insert(self, person):
        """Einfügen eines Person-Objekts in die Datenbank."""
        cursor = self._get_connection().cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM person")
        tuples = cursor.fetchall()
        
        for (maxid) in tuples:
            if maxid[0] is None:
                person.set_id(1)
            else:
                person.set_id(maxid[0] + 1)

        command = "INSERT INTO person (id, google_id, firstname, lastname, nickname) VALUES ('{}','{}','{}','{}','{}')" \
            .format(person.get_id(), person.get_google_id(), person.get_firstname(), 
                    person.get_lastname(), person.get_nickname())
        cursor.execute(command)

        self._get_connection().commit()
        cursor.close()
        return person

    def update(self, person):
        """Aktualisieren eines Person-Objekts in der Datenbank."""
        cursor = self._get_connection().cursor()
        command = "UPDATE person SET firstname='{}', lastname='{}', nickname='{}' WHERE id='{}'"\
            .format(person.get_firstname(), person.get_lastname(), person.get_nickname(), person.get_id())
        cursor.execute(command)

        self._get_connection().commit()
        cursor.close()

    def delete(self, person):
        """Löschen eines Person-Objekts aus der Datenbank."""
        cursor = self._get_connection().cursor()
        command = "DELETE FROM person WHERE id='{}'".format(person.get_id())
        cursor.execute(command)

        self._get_connection().commit()
        cursor.close()