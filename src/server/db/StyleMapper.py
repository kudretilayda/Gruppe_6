from src.server.bo.Style import Style
from src.server.db.Mapper import Mapper


class StyleMapper(Mapper):
    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT id, style_name, style_description FROM digital_wardrobe.style")
        tuples = cursor.fetchall()

        for (style_id, name, description) in tuples:
            style = Style()
            style.set_style_id(style_id)
            style.set_name(name)
            style.set_features(description)
            result.append(style)

        self._cnx.commit()
        cursor.close()
        return result

    def find_by_name(self, name):
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT id, name, description FROM styles WHERE name LIKE '{}' ORDER BY id".format(name)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if tuples[0] is not None:
            (id, name, description) = tuples[0]
            style = Style()
            style.set_id(id)
            style.set_name(name)
            style.set_features(description)
            result = style

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, key):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, name, description FROM styles WHERE id={}".format(key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if tuples[0] is not None:
            (id, name, description) = tuples[0]
            style = Style()
            style.set_id(id)
            style.set_name(name)
            style.set_features(description)
            result = style

        self._cnx.commit()
        cursor.close()

        return result

    def insert(self, style):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM digital_wardrobe.style")
        tuples = cursor.fetchall()

        for (max_id) in tuples:
            style.set_id(max_id[0] + 1)

        command = "INSERT INTO digital_wardrobe.style (id, style_name, style_description) VALUES (%s, %s, %s)"
        data = (style.get_id(), style.get_name(), style.get_description())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return style

    def update(self, style):
        cursor = self._cnx.cursor()

        command = "UPDATE digital_wardrobe.style SET style_name=%s, style_description=%s WHERE id=%s"
        data = (style.get_name(), style.get_description(), style.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def delete(self, style):
        cursor = self._cnx.cursor()

        command = "DELETE FROM styles WHERE id={}".format(style.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()


if (__name__ == "__main__"):
    with StyleMapper() as mapper:
        result = mapper.find_all()
        for s in result:
            print(s)
