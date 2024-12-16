from bo.clothing_item import ClothingItem
from db_connector import DBConnector

class ClothingItemMapper:
    @staticmethod
    def find_by_id(item_id):
        conn = DBConnector.get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM clothing_item WHERE id = %s", (item_id,))
            data = cursor.fetchone()
            if data:
                item = ClothingItem()
                item.set_id(data['id'])
                item.set_type(data['type_id'])
                return item
            return None
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def insert(item):
        conn = DBConnector.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO clothing_item (type_id) 
                VALUES (%s)
            """, (item.get_type(),))
            item_id = cursor.lastrowid
            conn.commit()
            item.set_id(item_id)
            return item_id
        finally:
            cursor.close()
            conn.close()