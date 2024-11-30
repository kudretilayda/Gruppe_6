# src/server/db/OutfitMapper.py

from server.db.Mapper import Mapper
from server.bo.Outfit import Outfit

class OutfitMapper(Mapper):
    def __init__(self):
        super().__init__()

    def get_table_name(self):
        return "outfit"

    def tuple_to_object(self, tuple):
        outfit = Outfit()
        outfit.set_id(tuple["id"])
        outfit.set_style_id(tuple["style_id"])
        outfit.set_name(tuple["name"])
        outfit.set_create_time(tuple["created_at"])
        
        # Items laden
        outfit.set_items(self._get_items_of_outfit(outfit.get_id()))
        return outfit

    def _get_items_of_outfit(self, outfit_id):
        """Helper zum Laden der Items eines Outfits"""
        items = []
        with self._cursor() as cursor:
            command = """
                SELECT clothing_item_id FROM outfit_items 
                WHERE outfit_id=%s
            """
            cursor.execute(command, (outfit_id,))
            tuples = cursor.fetchall()
            for tuple in tuples:
                items.append(tuple["clothing_item_id"])
        return items

    def insert(self, outfit):
        with self._cursor() as cursor:
            # Outfit einfügen
            command = "INSERT INTO outfit (id, style_id, name) VALUES (%s, %s, %s)"
            cursor.execute(command, (
                outfit.get_id(),
                outfit.get_style_id(),
                outfit.get_name()
            ))

            # Items-Zuordnungen einfügen
            for item_id in outfit.get_items():
                command = "INSERT INTO outfit_items (outfit_id, clothing_item_id) VALUES (%s, %s)"
                cursor.execute(command, (outfit.get_id(), item_id))

            self._cnx.commit()
            return outfit

    def update(self, outfit):
        with self._cursor() as cursor:
            # Outfit updaten
            command = "UPDATE outfit SET style_id=%s, name=%s WHERE id=%s"
            cursor.execute(command, (
                outfit.get_style_id(),
                outfit.get_name(),
                outfit.get_id()
            ))

            # Items neu zuordnen
            cursor.execute("DELETE FROM outfit_items WHERE outfit_id=%s", (outfit.get_id(),))
            for item_id in outfit.get_items():
                command = "INSERT INTO outfit_items (outfit_id, clothing_item_id) VALUES (%s, %s)"
                cursor.execute(command, (outfit.get_id(), item_id))

            self._cnx.commit()
            return outfit