from database.db_connector import DBConnector

class WardrobeMapper:
    @staticmethod
    def find_by_owner(owner_id):
        conn = DBConnector.get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM kleiderschrank WHERE eigentuemer_id = %s", (owner_id,))
            return cursor.fetchone()
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def insert(wardrobe):
        conn = DBConnector.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO kleiderschrank (eigentuemer_id) 
                VALUES (%s)
            """, (wardrobe['eigentuemer_id'],))
            wardrobe_id = cursor.lastrowid
            conn.commit()
            return wardrobe_id
        finally:
            cursor.close()
            conn.close()