from config import get_db_connection

def test_db():
    try:
        conn = get_db_connection()
        if conn.is_connected():
            print("Successfully connected to MySQL database!")
            cursor = conn.cursor()
            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()
            print("Available tables:", tables)
        else:
            print("Connection failed")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if 'conn' in locals() and conn.is_connected():
            conn.close()
            print("Connection closed")


if __name__ == "__main__":
    test_db()