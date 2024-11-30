from database.db_connector import DBConnector

class PersonMapper:
    @staticmethod
    def find_by_id(person_id):
        conn = DBConnector.get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM person WHERE id = %s", (person_id,))
            return cursor.fetchone()
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def find_by_google_id(google_id):
        conn = DBConnector.get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM person WHERE google_id = %s", (google_id,))
            return cursor.fetchone()
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def insert(person):
        conn = DBConnector.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO person (nachname, vorname, nickname, google_id) 
                VALUES (%s, %s, %s, %s)
            """, (person['nachname'], person['vorname'], person['nickname'], person['google_id']))
            person_id = cursor.lastrowid
            conn.commit()
            return person_id
        finally:
            cursor.close()
            conn.close()