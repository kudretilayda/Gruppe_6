import mysql.connector
from mysql.connector import Error

def get_db_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="dragonhart192837465",
        database="digital_wardrobe"
    )


connection = get_db_connection()
if connection.is_connected():
    print("Verbindung erfolgreich!")
