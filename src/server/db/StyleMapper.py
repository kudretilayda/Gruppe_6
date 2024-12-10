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



if __name__ == "__main__":
    with StyleMapper() as mapper:
        result = mapper.find_all()
        for s in result:
            print(s)
