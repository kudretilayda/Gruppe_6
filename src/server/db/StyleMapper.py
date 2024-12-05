from server.db.Mapper import Mapper
from server.bo.Style import Style
import uuid

class StyleMapper(Mapper):
    def __init__(self):
        super().__init__()

    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * from style")
        tuples = cursor.fetchall()

        for (id, style_name, style_description, created_by, created_at) in tuples:
            style = Style()
            style.set_id(id)
            style.set_style_name(style_name)
            style.set_style_description(style_description)
            style.set_created_by(created_by)
            style.set_created_at(created_at)
            result.append(style)

        self._cnx.commit()
        cursor.close()
        return result

    def find_by_id(self, style_id):
        cursor = self._cnx.cursor()
        command = "SELECT * FROM style WHERE id=%s"
        cursor.execute(command, (style_id,))
        tuples = cursor.fetchall()

        try:
            (id, style_name, style_description, created_by, created_at) = tuples[0]
            style = Style()
            style.set_id(id)
            style.set_style_name(style_name)
            style.set_style_description(style_description)
            style.set_created_by(created_by)
            style.set_created_at(created_at)
            return style
        except IndexError:
            return None
        finally:
            self._cnx.commit()
            cursor.close()

    def find_by_person(self, person_id):
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT * FROM style WHERE created_by=%s"
        cursor.execute(command, (person_id,))
        tuples = cursor.fetchall()

        for (id, style_name, style_description, created_by, created_at) in tuples:
            style = Style()
            style.set_id(id)
            style.set_style_name(style_name)
            style.set_style_description(style_description)
            style.set_created_by(created_by)
            style.set_created_at(created_at)
            result.append(style)

        self._cnx.commit()
        cursor.close()
        return result

    def insert(self, style):
        cursor = self._cnx.cursor()
        
        if not style.get_id():
            style.set_id(str(uuid.uuid4()))

        command = "INSERT INTO style (id, style_name, style_description, created_by) VALUES (%s,%s,%s,%s)"
        data = (style.get_id(), style.get_style_name(), style.get_style_description(), style.get_created_by())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return style

    def update(self, style):
        cursor = self._cnx.cursor()
        command = "UPDATE style SET style_name=%s, style_description=%s WHERE id=%s"
        data = (style.get_style_name(), style.get_style_description(), style.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def delete(self, style):
        cursor = self._cnx.cursor()
        command = "DELETE FROM style WHERE id=%s"
        cursor.execute(command, (style.get_id(),))
        self._cnx.commit()
        cursor.close()