import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",  # Dein MySQL Username
        password="Kik7285hhg2001-",  # Dein MySQL Passwort
        database="digital_wardrobe"  # Name deiner Datenbank
    )
    return connection

def test_connection():
    try:
        conn = get_db_connection()
        print("Verbindung erfolgreich!")
        
        # Teste Zugriff auf deine Tabellen
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clothing_item LIMIT 1")
        result = cursor.fetchall()
        print("Daten aus clothing_item:", result)
        
        cursor.close()
        conn.close()
        
    except Exception as e:
        print(f"Fehler: {e}")

if __name__ == "__main__":
    test_connection()