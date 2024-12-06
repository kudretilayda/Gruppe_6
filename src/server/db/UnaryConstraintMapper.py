from server.db.Mapper import Mapper
from server.bo.ConstraintRule import UnaryConstaint
import uuid

class UnaryConstraintMapper(Mapper):
    def __init__(self):
        super().__init__()

    def find_by_id(self, constraint_id):
        cursor = self._cnx.cursor()
        command = """SELECT cr.*, uc.reference_object_id
                    FROM constraint_rule cr
                    JOIN unary_constraint uc ON cr.id = uc.id
                    WHERE cr.id=%s"""
        cursor.execute(command, (constraint_id,))
        tuples = cursor.fetchall()

        try:
            (id, style_id, constraint_type, ref_id) = tuples[0]
            constraint = UnaryConstraintMapper()
            constraint.set_id(id)
            constraint.set_style_id(style_id)
            constraint.set_reference_object_id(ref_id)
            return constraint
        except IndexError:
            return None
        finally:
            self._cnx.commit()
            cursor.close()

    def find_by_style(self, style_id):
        cursor = self._cnx.cursor()
        command = """SELECT cr.*, uc.reference_object_id
                    FROM constraint_rule cr
                    JOIN unary_constraint uc ON cr.id = uc.id
                    WHERE cr.style_id=%s"""
        cursor.execute(command, (style_id,))
        tuples = cursor.fetchall()
        result = []

        for tuple in tuples:
            constraint = UnaryConstraintMapper()
            constraint.set_id(tuple[0])
            constraint.set_style_id(tuple[1])
            constraint.set_reference_object_id(tuple[3])
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
                        (id, style_id, constraint_type) VALUES (%s,%s,'unary')"""
            cursor.execute(command, (constraint.get_id(), constraint.get_style_id()))

            command = """INSERT INTO unary_constraint 
                        (id, reference_object_id) VALUES (%s,%s)"""
            cursor.execute(command, (constraint.get_id(), 
                                   constraint.get_reference_object_id()))

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
            command = """UPDATE unary_constraint 
                        SET reference_object_id=%s WHERE id=%s"""
            cursor.execute(command, (constraint.get_reference_object_id(), 
                                   constraint.get_id()))
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