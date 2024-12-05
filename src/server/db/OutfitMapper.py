from server.db.Mapper import Mapper
from server.bo.Outfit import Outfit
import uuid

class OutfitMapper(Mapper):
    def __init__(self):
        super().__init__()

    def find_by_id(self, outfit_id):
        cursor = self._cnx.cursor()
        command = """SELECT o.*, oi.clothing_item_id 
                    FROM outfit o 
                    LEFT JOIN outfit_items oi ON o.id = oi.outfit_id 
                    WHERE o.id=%s"""
        cursor.execute(command, (outfit_id,))
        tuples = cursor.fetchall()

        try:
            first_row = tuples[0]
            outfit = Outfit()
            outfit.set_id(first_row[0])
            outfit.set_outfit_name(first_row[1])
            outfit.set_style_id(first_row[2])
            outfit.set_created_by(first_row[3])
            outfit.set_created_at(first_row[4])
            
            items = [t[5] for t in tuples if t[5] is not None]
            outfit.set_items(items)
            return outfit
        except IndexError:
            return None
        finally:
            self._cnx.commit()
            cursor.close()

    def find_by_person(self, person_id):
        cursor = self._cnx.cursor()
        command = """SELECT DISTINCT o.* 
                    FROM outfit o 
                    LEFT JOIN outfit_items oi ON o.id = oi.outfit_id 
                    WHERE o.created_by=%s"""
        cursor.execute(command, (person_id,))
        tuples = cursor.fetchall()
        result = []

        for row in tuples:
            outfit = Outfit()
            outfit.set_id(row[0])
            outfit.set_outfit_name(row[1])
            outfit.set_style_id(row[2])
            outfit.set_created_by(row[3])
            outfit.set_created_at(row[4])
            
            command = "SELECT clothing_item_id FROM outfit_items WHERE outfit_id=%s"
            cursor.execute(command, (outfit.get_id(),))
            items = [item[0] for item in cursor.fetchall()]
            outfit.set_items(items)
            result.append(outfit)

        self._cnx.commit()
        cursor.close()
        return result

    def insert(self, outfit):
        cursor = self._cnx.cursor()
        try:
            if not outfit.get_id():
                outfit.set_id(str(uuid.uuid4()))

            command = "INSERT INTO outfit (id, outfit_name, style_id, created_by) VALUES (%s,%s,%s,%s)"
            data = (outfit.get_id(), outfit.get_outfit_name(), outfit.get_style_id(), outfit.get_created_by())
            cursor.execute(command, data)
            
            for item_id in outfit.get_items():
                command = "INSERT INTO outfit_items (outfit_id, clothing_item_id) VALUES (%s,%s)"
                cursor.execute(command, (outfit.get_id(), item_id))
                
            self._cnx.commit()
            return outfit
        except:
            self._cnx.rollback()
            raise
        finally:
            cursor.close()

    def update(self, outfit):
        cursor = self._cnx.cursor()
        try:
            command = "UPDATE outfit SET outfit_name=%s, style_id=%s WHERE id=%s"
            data = (outfit.get_outfit_name(), outfit.get_style_id(), outfit.get_id())
            cursor.execute(command, data)
            
            cursor.execute("DELETE FROM outfit_items WHERE outfit_id=%s", (outfit.get_id(),))
            for item_id in outfit.get_items():
                cursor.execute("INSERT INTO outfit_items (outfit_id, clothing_item_id) VALUES (%s,%s)", 
                             (outfit.get_id(), item_id))
                
            self._cnx.commit()
        except:
            self._cnx.rollback()
            raise
        finally:
            cursor.close()

    def delete(self, outfit):
        cursor = self._cnx.cursor()
        try:
            cursor.execute("DELETE FROM outfit_items WHERE outfit_id=%s", (outfit.get_id(),))
            cursor.execute("DELETE FROM outfit WHERE id=%s", (outfit.get_id(),))
            self._cnx.commit()
        except:
            self._cnx.rollback()
            raise
        finally:
            cursor.close()