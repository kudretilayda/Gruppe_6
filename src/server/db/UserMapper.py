from server.db.Mapper import Mapper
from server.bo.User import User
import uuid

class PersonMapper(Mapper):
    def __init__(self):
        super().__init__()

    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * from person")
        tuples = cursor.fetchall()

        for (id, google_id, first_name, last_name, nick_name, email, created_at) in tuples:
            person = User()
            person.set_id(id)
            person.set_google_id(google_id)
            person.set_first_name(first_name)
            person.set_last_name(last_name)
            person.set_nick_name(nick_name)
            person.set_email(email)
            person.set_created_at(created_at)
            result.append(person)

        self._cnx.commit()
        cursor.close()
        return result

    def find_by_google_id(self, google_id):
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT * FROM person WHERE google_id=%s"
        cursor.execute(command, (google_id,))
        tuples = cursor.fetchall()

        try:
            (id, google_id, first_name, last_name, nick_name, email, created_at) = tuples[0]
            person = User()
            person.set_id(id)
            person.set_google_id(google_id)
            person.set_first_name(first_name)
            person.set_last_name(last_name)
            person.set_nick_name(nick_name)
            person.set_email(email)
            person.set_created_at(created_at)
            result = person
        except IndexError:
            result = None

        self._cnx.commit()
        cursor.close()
        return result

    def insert(self, person):
        cursor = self._cnx.cursor()

        if not person.get_id():
            person.set_id(str(uuid.uuid4()))

        command = """INSERT INTO person 
                    (id, google_id, first_name, last_name, nick_name, email) 
                    VALUES (%s,%s,%s,%s,%s,%s)"""
        data = (person.get_id(), person.get_google_id(), person.get_first_name(),
                person.get_last_name(), person.get_nick_name(), person.get_email())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return person

    def update(self, person):
        cursor = self._cnx.cursor()
        command = """UPDATE person 
                    SET google_id=%s, first_name=%s, last_name=%s, 
                    nick_name=%s, email=%s WHERE id=%s"""
        data = (person.get_google_id(), person.get_first_name(),
                person.get_last_name(), person.get_nick_name(),
                person.get_email(), person.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def delete(self, person):
        cursor = self._cnx.cursor()
        command = "DELETE FROM person WHERE id=%s"
        cursor.execute(command, (person.get_id(),))
        self._cnx.commit()
        cursor.close()

if __name__ == "__main__":
    with PersonMapper() as mapper:
        result = mapper.find_all()
        for p in result:
            print(p)