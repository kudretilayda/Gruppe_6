import mysql.connector

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
