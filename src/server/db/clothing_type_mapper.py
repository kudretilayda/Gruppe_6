from bo.clothing_type import ClothingType
from db_connector import DBConnector

class ClothingTypeMapper:
    @staticmethod
    def find_by_id(type_id):
        conn = DBConnector.get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM clothing_type WHERE id = %s", (type_id,))
            data = cursor.fetchone()
            if data:
                type = ClothingType()
                type.set_id(data['id'])
                type.set_name(data['name'])
                type.set_usage(data['usage'])
                return type
            return None
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def insert(type):
        conn = DBConnector.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO clothing_type (name, usage) 
                VALUES (%s, %s)
            """, (type.get_name(), type.get_usage()))
            type_id = cursor.lastrowid
            conn.commit()
            type.set_id(type_id)
            return type_id
        finally:
            cursor.close()
            conn.close()