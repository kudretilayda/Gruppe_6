# src/db/mapper/person_mapper.py
from .Mapper import Mapper
from server.db import Person

class PersonMapper(Mapper):
    """Mapper class for Person objects"""
    
    def find_by_id(self, id):
        result = None
        cursor = self._get_connection().cursor()
        command = "SELECT id, google_id, vorname, nachname, nickname, created_at FROM person WHERE id=%s"
        cursor.execute(command, (id,))
        tuples = cursor.fetchall()

        try:
            (id, google_id, vorname, nachname, nickname, created_at) = tuples[0]
            result = Person()
            result.id = id
            result.google_id = google_id
            result.vorname = vorname
            result.nachname = nachname
            result.nickname = nickname
            result.created_at = created_at
        except IndexError:
            result = None

        self._get_connection().commit()
        cursor.close()
        return result

    def find_by_google_id(self, google_id):
        result = None
        cursor = self._get_connection().cursor()
        command = "SELECT id, google_id, vorname, nachname, nickname, created_at FROM person WHERE google_id=%s"
        cursor.execute(command, (google_id,))
        tuples = cursor.fetchall()

        try:
            (id, google_id, vorname, nachname, nickname, created_at) = tuples[0]
            result = Person()
            result.id = id
            result.google_id = google_id
            result.vorname = vorname
            result.nachname = nachname
            result.nickname = nickname
            result.created_at = created_at
        except IndexError:
            result = None

        self._get_connection().commit()
        cursor.close()
        return result

    def insert(self, person):
        cursor = self._get_connection().cursor()
        command = "INSERT INTO person (google_id, vorname, nachname, nickname) VALUES (%s, %s, %s, %s)"
        data = (person.google_id, person.vorname, person.nachname, person.nickname)
        cursor.execute(command, data)
        
        person.id = cursor.lastrowid
        self._get_connection().commit()
        cursor.close()
        return person

    def update(self, person):
        cursor = self._get_connection().cursor()
        command = "UPDATE person SET google_id=%s, vorname=%s, nachname=%s, nickname=%s WHERE id=%s"
        data = (person.google_id, person.vorname, person.nachname, person.nickname, person.id)
        cursor.execute(command, data)
        
        self._get_connection().commit()
        cursor.close()
        return person

    def delete(self, person):
        cursor = self._get_connection().cursor()
        command = "DELETE FROM person WHERE id=%s"
        cursor.execute(command, (person.id,))
        
        self._get_connection().commit()
        cursor.close()
        return True