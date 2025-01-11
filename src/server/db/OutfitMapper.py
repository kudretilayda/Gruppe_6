from src.server.bo.ClothingItem import ClothingItem
from src.server.db.Mapper import Mapper
from src.server.bo.Outfit import Outfit


class OutfitMapper(Mapper):
    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * FROM digital_wardrobe.outfit")
        tuples = cursor.fetchall()

        for (id, outfit_name, style_id) in tuples:
            outfit = Outfit()
            outfit.set_id(id)
            outfit.set_outfit_name(outfit_name)
            outfit.set_style(style_id)
            result.append(outfit)

        self._cnx.commit()
        cursor.close()
        return result

    def find_by_key(self, key):
        result = None
        cursor = self._cnx.cursor()
        command = f"SELECT * FROM outfit WHERE id={key}"
        cursor.execute(command)
        tuples = cursor.fetchall()

        if tuples:
            (id, outfit_name, style_id) = tuples[0]
            result = Outfit()
            result.set_id(id)
            result.set_outfit_name(outfit_name)
            result.set_style(style_id)

        self._cnx.commit()
        cursor.close()
        return result

    