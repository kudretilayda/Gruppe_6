from .Mapper import Mapper
from server.db import Kleiderschrank

class KleiderschrankMapper(Mapper):
    """Mapper class for Kleiderschrank objects"""
    
    def find_by_id(self, id):
        result = None
        cursor = self._get_connection().cursor()
        command = "SELECT id, person_id, name, created_at FROM kleiderschrank WHERE id=%s"
        cursor.execute(command, (id,))
        tuples = cursor.fetchall()

        try:
            (id, person_id, name, created_at) = tuples[0]
            result = Kleiderschrank()
            result.id = id
            result.person_id = person_id
            result.name = name
            result.created_at = created_at
        except IndexError:
            result = None

        self._get_connection().commit()
        cursor.close()
        return result

    def find_by_person_id(self, person_id):
        result = []
        cursor = self._get_connection().cursor()
        command = "SELECT id, person_id, name, created_at FROM kleiderschrank WHERE person_id=%s"
        cursor.execute(command, (person_id,))
        tuples = cursor.fetchall()

        for (id, person_id, name, created_at) in tuples:
            kleiderschrank = Kleiderschrank()
            kleiderschrank.id = id
            kleiderschrank.person_id = person_id
            kleiderschrank.name = name
            kleiderschrank.created_at = created_at
            result.append(kleiderschrank)

        self._get_connection().commit()
        cursor.close()
        return result

    def insert(self, kleiderschrank):
        cursor = self._get_connection().cursor()
        command = "INSERT INTO kleiderschrank (person_id, name) VALUES (%s, %s)"
        data = (kleiderschrank.person_id, kleiderschrank.name)
        cursor.execute(command, data)
        
        kleiderschrank.id = cursor.lastrowid
        self._get_connection().commit()
        cursor.close()
        return kleiderschrank

    def update(self, kleiderschrank):
        cursor = self._get_connection().cursor()
        command = "UPDATE kleiderschrank SET name=%s WHERE id=%s"
        data = (kleiderschrank.name, kleiderschrank.id)
        cursor.execute(command, data)
        
        self._get_connection().commit()
        cursor.close()
        return kleiderschrank

    def delete(self, kleiderschrank):
        cursor = self._get_connection().cursor()
        command = "DELETE FROM kleiderschrank WHERE id=%s"
        cursor.execute(command, (kleiderschrank.id,))
        
        self._get_connection().commit()
        cursor.close()
        return True