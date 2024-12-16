import mysql.connector

<<<<<<< Updated upstream
def get_db_connection():
    return mysql.connector.connect(
        host="localhost", 
        user="root",
        password="Kik7285hhg2001-",
        database="digital_wardrobe"
    )


connection = get_db_connection()
if connection.is_connected():
    print("Verbindung erfolgreich!")
=======
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'dragonhart192837465',
    'database': 'Kleiderschrank_Draft'
}

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=DB_CONFIG['host'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password'],
            database=DB_CONFIG['database']
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

connection = get_db_connection()
if connection and connection.is_connected():
    print("Verbindung steht!")  # Connection successful
    connection.close()
else:
    print("Verbindung fehlgeschlagen!")  # Connection failed
>>>>>>> Stashed changes
