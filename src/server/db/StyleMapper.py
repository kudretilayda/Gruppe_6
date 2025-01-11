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

    