from src.server.db.Mapper import Mapper
from src.server.bo.Style import Style

class StyleMapper(Mapper):
    def find_all(self):
        results = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * FROM digital_wardrobe.style")
        tuples = cursor.fetchall()

        for (id, style_features, style_constraints) in tuples:
            style = Style()
            style.set_id(id)
            style.set_style_features(style_features)
            style.set_style_constraints(style_constraints)
            results.append(style)

        self._cnx.commit()
        cursor.close()
        return results

    def find_by_key(self, key):
        results = None
        cursor = self._cnx.cursor()
        command = f"SELECT * FROM style WHERE id={key}"
        cursor.execute(command)
        tuples = cursor.fetchall()

        if tuples:
            (id, style_features, style_constraints) = tuples[0]
            results = Style()
            results.set_id(id)
            results.set_style_features(style_features)
            results.set_style_constraints(style_constraints)

        self._cnx.commit()
        cursor.close()
        return results

    def insert(self, style):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM digital_wardrobe.style")
        max_id = cursor.fetchone()[0]
        style.set_id(max_id + 1 if max_id else 1)

        command = ("INSERT INTO digital_wardrobe.style (id, style_features, style_constraints) "
                   "VALUES (%s, %s, %s)")
        data = (style.get_id(), style.get_features(), style.get_constraints())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return style

    def update(self, style):
        cursor = self._cnx.cursor()
        command = ("UPDATE digital_wardrobe.style "
                   "SET style_features=%s, style_constraints=%s "
                   "WHERE id=%s")
        data = (style.get_features(), style.get_constraints(), style.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def delete(self, style):
        cursor = self._cnx.cursor()
        command = f"DELETE FROM style WHERE id={style.get_id()}"
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

    def find_by_closet_items(self, available_items):
        results = []
        cursor = self._cnx.cursor()

        # Formatierte Liste der Kleidungsstücke für die SQL-Abfrage
        item_types = ",".join([f"'{item}'" for item in available_items])
        
        # Abfrage für Styles, bei denen alle benötigten Kleidungsstücke im Kleiderschrank vorhanden sind
        query = f"""
            SELECT s.id, s.style_features, s.style_constraints 
            FROM digital_wardrobe.style AS s
            JOIN digital_wardrobe.style_items AS si ON s.id = si.style_id
            WHERE si.item_type IN ({item_types})
            GROUP BY s.id
            HAVING COUNT(DISTINCT si.item_type) = (SELECT COUNT(*) 
                                                   FROM digital_wardrobe.style_items 
                                                   WHERE style_id = s.id);
        """

        cursor.execute(query)
        tuples = cursor.fetchall()

        for (id, style_features, style_constraints) in tuples:
            style = Style()
            style.set_id(id)
            style.set_style_features(style_features)
            style.set_style_constraints(style_constraints)
            results.append(style)

        self._cnx.commit()
        cursor.close()
        return results
