from server.bo.User import User  # Import der User-Klasse
from server.db.Mapper import Mapper

class UserMapper(Mapper):
    def find_by_id(self, user_id: str) -> User:
        cursor = self._get_connection().cursor()
        cursor.execute("SELECT * FROM user WHERE id=%s", (user_id,))
        tuples = cursor.fetchall()
        
        try:
            if tuples:
                (id, google_id, first_name, last_name, nick_name, email, created_at) = tuples[0]
                user = User()
                user.set_id(id)
                user.set_google_id(google_id)
                user.set_first_name(first_name)
                user.set_last_name(last_name)
                user.set_nick_name(nick_name)
                user.set_email(email)
                user.set_created_at(created_at)
                return user
            return None
        finally:
            cursor.close()

    def find_by_google_id(self, google_id: str) -> User:
        cursor = self._get_connection().cursor()
        cursor.execute("SELECT * FROM user WHERE google_id=%s", (google_id,))
        tuples = cursor.fetchall()
        
        try:
            if tuples:
                (id, google_id, first_name, last_name, nick_name, email, created_at) = tuples[0]
                user = User()
                user.set_id(id)
                user.set_google_id(google_id)
                user.set_first_name(first_name)
                user.set_last_name(last_name)
                user.set_nick_name(nick_name)
                user.set_email(email)
                user.set_created_at(created_at)
                return user
            return None
        finally:
            cursor.close()

    def insert(self, user: User):
        cursor = self._get_connection().cursor()
        cursor.execute("""
            INSERT INTO user (id, google_id, first_name, last_name, nick_name, email)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (user.get_id(), user.get_google_id(), user.get_first_name(),
              user.get_last_name(), user.get_nick_name(), user.get_email()))
        self._get_connection().commit()
        cursor.close()
        return user

    def update(self, user: User) -> User:
        cursor = self._get_connection().cursor()
        cursor.execute("""
            UPDATE user 
            SET google_id=%s, first_name=%s, last_name=%s, nick_name=%s, email=%s
            WHERE id=%s
        """, (user.get_google_id(), user.get_first_name(), user.get_last_name(),
              user.get_nick_name(), user.get_email(), user.get_id()))
        self._get_connection().commit()
        cursor.close()
        return user

    def delete(self, user_id: str):
        cursor = self._get_connection().cursor()
        cursor.execute("DELETE FROM user WHERE id=%s", (user_id,))
        self._get_connection().commit()
        cursor.close()
        return True
