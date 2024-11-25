import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost:3306",
        user="root",
        password="kik2001duman123",
        database="digital_wardrobe"
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