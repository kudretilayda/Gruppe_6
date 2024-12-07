from server.db.Mapper import Mapper
from server.bo.ConstraintRule import ImplicationConstraint
import uuid

class ImplicationMapper(Mapper):
    def __init__(self):
        super().__init__()

    def find_by_id(self, constraint_id):
        cursor = self._cnx.cursor()
        command = """SELECT cr.*, i.if_type_id, i.then_type_id
                    FROM constraint_rule cr
                    JOIN implikation i ON cr.id = i.id
                    WHERE cr.id=%s"""
        cursor.execute(command, (constraint_id,))
        tuples = cursor.fetchall()

        try:
            (id, style_id, constraint_type, if_id, then_id) = tuples[0]
            constraint = ImplicationConstraint()
            constraint.set_id(id)
            constraint.set_style_id(style_id)
            constraint.set_if_type_id(if_id)
            constraint.set_then_type_id(then_id)
            return constraint
        except IndexError:
            return None
        finally:
            self._cnx.commit()
            cursor.close()

    def find_by_style(self, style_id):
        cursor = self._cnx.cursor()
        command = """SELECT cr.*, i.if_type_id, i.then_type_id
                    FROM constraint_rule cr
                    JOIN implikation i ON cr.id = i.id
                    WHERE cr.style_id=%s"""
        cursor.execute(command, (style_id,))
        tuples = cursor.fetchall()
        result = []

        for tuple in tuples:
            constraint = ImplicationConstraint()
            constraint.set_id(tuple[0])
            constraint.set_style_id(tuple[1])
            constraint.set_if_type_id(tuple[3])
            constraint.set_then_type_id(tuple[4])
            result.append(constraint)

        self._cnx.commit()
        cursor.close()
        return result

    def insert(self, constraint):
        cursor = self._cnx.cursor()
        try:
            if not constraint.get_id():
                constraint.set_id(str(uuid.uuid4()))

            command = """INSERT INTO constraint_rule 
                        (id, style_id, constraint_type) VALUES (%s,%s,'implikation')"""
            cursor.execute(command, (constraint.get_id(), constraint.get_style_id()))

            command = """INSERT INTO implikation 
                        (id, if_type_id, then_type_id) VALUES (%s,%s,%s)"""
            data = (constraint.get_id(), constraint.get_if_type_id(),
                   constraint.get_then_type_id())
            cursor.execute(command, data)

            self._cnx.commit()
            return constraint
        except:
            self._cnx.rollback()
            raise
        finally:
            cursor.close()

    def update(self, constraint):
        cursor = self._cnx.cursor()
        try:
            command = """UPDATE implikation 
                        SET if_type_id=%s, then_type_id=%s WHERE id=%s"""
            data = (constraint.get_if_type_id(), constraint.get_then_type_id(),
                   constraint.get_id())
            cursor.execute(command, data)
            self._cnx.commit()
        except:
            self._cnx.rollback()
            raise
        finally:
            cursor.close()

    def delete(self, constraint):
        cursor = self._cnx.cursor()
        try:
            cursor.execute("""DELETE FROM constraint_rule WHERE id=%s""", 
                         (constraint.get_id(),))
            self._cnx.commit()
        except:
            self._cnx.rollback()
            raise
        finally:
            cursor.close()