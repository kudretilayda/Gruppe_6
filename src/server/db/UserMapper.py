from src.server.db.Mapper import Mapper
from src.server.bo.User import User


class UserMapper(Mapper):
    def find_all(self):
        result = []
        cursor = self._cnx().cursor()
        cursor.execute("SELECT * FROM digital_wardrobe.person")
        tuples = cursor.fetchall()

        for (user_id, google_id, firstname, lastname, nickname, created_at) in tuples:
            user = User()
            user.set_user_id(user_id)
            user.set_google_id(google_id)
            user.set_firstname(firstname)
            user.set_lastname(lastname)
            user.set_nickname(nickname)
            result.append(user)

        self._cnx().commit()
        cursor.close()
        return result

    def find_by_key(self, key):
        result = None
        cursor = self._cnx().cursor()
        command = "SELECT * FROM person WHERE id='{}'".format(key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if tuples is not None and len(tuples) > 0:
            (user_id, google_id, firstname, lastname, nickname, created_at) = tuples[0]
            result = User()
            result.set_id(user_id)
            result.set_google_id(google_id)
            result.set_firstname(firstname)
            result.set_lastname(lastname)
            result.set_nickname(nickname)

        self._cnx().commit()
        cursor.close()
        return result

    def find_by_google_id(self, google_id):
        result = None
        cursor = self._cnx().cursor()
        command = "SELECT * FROM person WHERE google_id='{}'".format(google_id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if tuples is not None and len(tuples) > 0:
            (user_id, google_id, firstname, lastname, nickname, created_at) = tuples[0]
            result = User()
            result.set_id(user_id)
            result.set_google_id(google_id)
            result.set_firstname(firstname)
            result.set_lastname(lastname)
            result.set_nickname(nickname)

        self._cnx().commit()
        cursor.close()
        return result

    def insert(self, person):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM digital_wardrobe.person")
        max_id = cursor.fetchone()[0]
        person.set_id(max_id + 1 if max_id else 1)

        command = ("INSERT INTO digital_wardrobe.person "
                   "(id, google_id, lastname, firstname, nickname, email) "
                   "VALUES (%s, %s, %s, %s, %s, %s)")
        data = (person.get_id(), person.get_google_id(), person.get_lastname(),
                person.get_firstname(), person.get_nickname(), person.get_email())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return person

    def update(self, person):
        cursor = self._cnx.cursor()
        command = ("UPDATE digital_wardrobe.person SET google_id=%s, lastname=%s, firstname=%s, "
                   "nickname=%s, email=%s WHERE id=%s")
        data = (person.get_google_id(), person.get_lastname(), person.get_firstname(),
                person.get_nickname(), person.get_email(), person.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def delete(self, person):
        cursor = self._cnx().cursor()
        command = "DELETE FROM person WHERE id='{}'".format(person.get_id())
        cursor.execute(command)

        self._cnx().commit()
        cursor.close()
