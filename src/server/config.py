import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost", 
        user="root",
        password="demo",
        database="digital_wardrobe"
    )


connection = get_db_connection()
if connection.is_connected():
    print("Verbindung erfolgreich!")
