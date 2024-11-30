from server.db.Mapper import Mapper
from server.bo.User import Person

class PersonMapper(Mapper):
    """Mapper-Klasse für Person-Objekte"""

    def __init__(self):
        super().__init__()

    def find_all(self):
        """Alle Person-Objekte auslesen"""
        result = []
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM person")
        tuples = cursor.fetchall()

        for (id, google_id, first_name, last_name, nickname, created_at) in tuples:
            person = Person()
            person.set_id(id)
            person.set_google_id(google_id)
            person.set_first_name(first_name)
            person.set_last_name(last_name)
            person.set_nickname(nickname)
            result.append(person)

        self._connection.commit()
        cursor.close()

        return result

    def find_by_id(self, id):
        """Eine Person anhand ihrer ID auslesen"""
        result = None
        cursor = self._connection.cursor()
        command = "SELECT * FROM person WHERE id={}".format(id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, google_id, first_name, last_name, nickname, created_at) = tuples[0]
            person = Person()
            person.set_id(id)
            person.set_google_id(google_id)
            person.set_first_name(first_name)
            person.set_last_name(last_name)
            person.set_nickname(nickname)
            result = person
        except IndexError:
            result = None

        self._connection.commit()
        cursor.close()
        return result

    def find_by_google_id(self, google_id):
        """Eine Person anhand ihrer Google ID auslesen"""
        result = None
        cursor = self._connection.cursor()
        command = "SELECT * FROM person WHERE google_id='{}'".format(google_id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, google_id, first_name, last_name, nickname, created_at) = tuples[0]
            person = Person()
            person.set_id(id)
            person.set_google_id(google_id)
            person.set_first_name(first_name)
            person.set_last_name(last_name)
            person.set_nickname(nickname)
            result = person
        except IndexError:
            result = None

        self._connection.commit()
        cursor.close()
        return result

    def insert(self, person):
        """Eine neue Person anlegen"""
        cursor = self._connection.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM person")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is not None:
                person.set_id(maxid[0] + 1)
            else:
                person.set_id(1)

        command = "INSERT INTO person (id, google_id, first_name, last_name, nickname) VALUES (%s, %s, %s, %s, %s)"
        data = (person.get_id(), person.get_google_id(), person.get_first_name(), 
                person.get_last_name(), person.get_nickname())
        cursor.execute(command, data)

        self._connection.commit()
        cursor.close()
        return person

    def update(self, person):
        """Eine Person aktualisieren"""
        cursor = self._connection.cursor()

        command = "UPDATE person SET google_id=%s, first_name=%s, last_name=%s, nickname=%s WHERE id=%s"
        data = (person.get_google_id(), person.get_first_name(), person.get_last_name(),
                person.get_nickname(), person.get_id())
        cursor.execute(command, data)

        self._connection.commit()
        cursor.close()

    def delete(self, person):
        """Eine Person löschen"""
        cursor = self._connection.cursor()

        command = "DELETE FROM person WHERE id={}".format(person.get_id())
        cursor.execute(command)

        self._connection.commit()
        cursor.close()