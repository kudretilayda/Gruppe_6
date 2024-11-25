from src.server.db.database import Database

def test_db_connection():
    db = Database()
    if db.connection and db.connection.is_connected():
        print("Erfolgreich mit der Datenbank verbunden")
    else:
        print("Fehler bei der Verbindung zur Datenbank")

test_db_connection()

