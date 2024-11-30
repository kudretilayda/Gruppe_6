from bo.user import Person
from db.db_connector import DBConnector

class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, username, password):
        if self.username == username and self.password == password:
            print("Login successful!")
            return True
        else:
            print("Invalid username or password.")
            return False

    def create_user(self, firstname, lastname, nickname, google_id):
        # Erstelle einen neuen Benutzer in der Datenbank
        person = Person(firstname, lastname, nickname, google_id)
        person_id = self.save_person(person)
        print(f"Created user with ID: {person_id}")
        return person_id

    def delete_user(self, person_id):
        # Lösche den Benutzer mit der angegebenen ID aus der Datenbank
        conn = DBConnector.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM person WHERE id = %s", (person_id,))
            conn.commit()
            print(f"Deleted user with ID: {person_id}")
        finally:
            cursor.close()
            conn.close()

    def update_user(self, person_id, new_firstname, new_lastname, new_nickname):
        # Aktualisiere die Benutzerdaten in der Datenbank
        conn = DBConnector.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("UPDATE person SET firstname = %s, lastname = %s, nickname = %s WHERE id = %s",
                           (new_firstname, new_lastname, new_nickname, person_id))
            conn.commit()
            print(f"Updated user with ID: {person_id}")
        finally:
            cursor.close()
            conn.close()

    def view_user_list(self):
        # Hole eine Liste aller registrierten Benutzer aus der Datenbank
        conn = DBConnector.get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM person")
            users = cursor.fetchall()
            print("List of all users:")
            for user in users:
                print(f"{user['id']} - {user['firstname']} {user['lastname']} ({user['nickname']})")
        finally:
            cursor.close()
            conn.close()

    def save_person(self, person):
        # Speichere einen neuen Benutzer in der Datenbank
        conn = DBConnector.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO person (firstname, lastname, nickname, google_id) VALUES (%s, %s, %s, %s)",
                           (person.firstname, person.lastname, person.nickname, person.google_id))
            person_id = cursor.lastrowid
            conn.commit()
            return person_id
        finally:
            cursor.close()
            conn.close()