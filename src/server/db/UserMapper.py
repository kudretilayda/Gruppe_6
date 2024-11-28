# src/server/db/mapper/PersonMapper.py

from server.db.Mapper import Mapper
from server.bo.User import Person

class PersonMapper(Mapper):
    """Mapper-Klasse, die Person-Objekte auf eine relationale
    Datenbank abbildet."""
    
    def __init__(self):
        super().__init__()

    def find_all(self):
        """Auslesen aller Personen."""
        result = []
        with self._cursor() as cursor:
            cursor.execute("SELECT * FROM person")
            tuples = cursor.fetchall()
            for (id, google_id, firstname, lastname, nickname, create_time) in tuples:
                person = Person()
                person.set_id(id)
                person.set_google_id(google_id)
                person.set_firstname(firstname)
                person.set_lastname(lastname)
                person.set_nickname(nickname)
                person.set_create_time(create_time)
                result.append(person)
        return result

    def find_by_key(self, key):
        """Suchen einer Person mit vorgegebener ID"""
        with self._cursor() as cursor:
            command = "SELECT * FROM person WHERE id=%s"
            cursor.execute(command, (key,))
            tuples = cursor.fetchall()
            try:
                (id, google_id, firstname, lastname, nickname, create_time) = tuples[0]
                person = Person()
                person.set_id(id)
                person.set_google_id(google_id)
                person.set_firstname(firstname)
                person.set_lastname(lastname)
                person.set_nickname(nickname)
                person.set_create_time(create_time)
                return person
            except IndexError:
                return None

    def find_by_google_id(self, google_id):
        """Suchen einer Person mit vorgegebener Google ID"""
        with self._cursor() as cursor:
            command = "SELECT * FROM person WHERE google_id=%s"
            cursor.execute(command, (google_id,))
            tuples = cursor.fetchall()
            try:
                (id, google_id, firstname, lastname, nickname, create_time) = tuples[0]
                person = Person()
                person.set_id(id)
                person.set_google_id(google_id)
                person.set_firstname(firstname)
                person.set_lastname(lastname)
                person.set_nickname(nickname)
                person.set_create_time(create_time)
                return person
            except IndexError:
                return None

    def insert(self, person):
        """Einfügen einer Person in die Datenbank."""
        with self._cursor() as cursor:
            command = "INSERT INTO person (id, google_id, firstname, lastname, nickname) VALUES (%s, %s, %s, %s, %s)"
            data = (person.get_id(), person.get_google_id(), person.get_firstname(),
                   person.get_lastname(), person.get_nickname())
            cursor.execute(command, data)
            self._cnx.commit()
            return person

    def update(self, person):
        """Aktualisieren einer Person in der Datenbank."""
        with self._cursor() as cursor:
            command = "UPDATE person SET google_id=%s, firstname=%s, lastname=%s, nickname=%s WHERE id=%s"
            data = (person.get_google_id(), person.get_firstname(),
                   person.get_lastname(), person.get_nickname(), person.get_id())
            cursor.execute(command, data)
            self._cnx.commit()
            return person

    def delete(self, person):
        """Löschen einer Person aus der Datenbank."""
        with self._cursor() as cursor:
            command = "DELETE FROM person WHERE id=%s"
            cursor.execute(command, (person.get_id(),))
            self._cnx.commit()