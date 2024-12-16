import mysql.connector

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'dragonhart192837465',
    'database': 'digital_wardrobe'
}

# Define the function
def get_db_connection():
    print("Attempting to connect to database...")  # Debugging
    try:
        connection = mysql.connector.connect(
            host=DB_CONFIG['host'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password'],
            database=DB_CONFIG['database']
        )
        print("Function get_db_connection executed successfully.")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Test connection
connection = get_db_connection()
if connection and connection.is_connected():
    print("Verbindung steht!")  # Connection successful
    connection.close()
else:
    print("Verbindung fehlgeschlagen!")  # Connection failed
