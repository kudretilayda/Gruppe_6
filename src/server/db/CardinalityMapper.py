from server.db.Mapper import Mapper
from server.bo.ConstraintRule import CardinalityConstraint
import uuid

class CardinalityMapper(Mapper):
    def __init__(self):
        super().__init__()

    def find_by_id(self, constraint_id):
        cursor = self._cnx.cursor()
        command = """SELECT cr.*, k.clothing_type_id, k.min_count, k.max_count
                    FROM constraint_rule cr
                    JOIN kardinalitaet k ON cr.id = k.id
                    WHERE cr.id=%s"""
        cursor.execute(command, (constraint_id,))
        tuples = cursor.fetchall()

        try:
            (id, style_id, constraint_type, type_id, min_count, max_count) = tuples[0]
            constraint = CardinalityConstraint()
            constraint.set_id(id)
            constraint.set_style_id(style_id)
            constraint.set_clothing_type_id(type_id)
            constraint.set_min_count(min_count)
            constraint.set_max_count(max_count)
            return constraint
        except IndexError:
            return None
        finally:
            self._cnx.commit()
            cursor.close()

    def find_by_style(self, style_id):
        cursor = self._cnx.cursor()
        command = """SELECT cr.*, k.clothing_type_id, k.min_count, k.max_count
                    FROM constraint_rule cr
                    JOIN kardinalitaet k ON cr.id = k.id
                    WHERE cr.style_id=%s"""
        cursor.execute(command, (style_id,))
        tuples = cursor.fetchall()
        result = []

        for tuple in tuples:
            constraint = CardinalityConstraint()
            constraint.set_id(tuple[0])
            constraint.set_style_id(tuple[1])
            constraint.set_clothing_type_id(tuple[3])
            constraint.set_min_count(tuple[4])
            constraint.set_max_count(tuple[5])
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
                        (id, style_id, constraint_type) VALUES (%s,%s,'kardinalitaet')"""
            cursor.execute(command, (constraint.get_id(), constraint.get_style_id()))

            command = """INSERT INTO kardinalitaet 
                        (id, clothing_type_id, min_count, max_count) 
                        VALUES (%s,%s,%s,%s)"""
            data = (constraint.get_id(), constraint.get_clothing_type_id(),
                   constraint.get_min_count(), constraint.get_max_count())
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
            command = """UPDATE kardinalitaet 
                        SET clothing_type_id=%s, min_count=%s, max_count=%s 
                        WHERE id=%s"""
            data = (constraint.get_clothing_type_id(), constraint.get_min_count(),
                   constraint.get_max_count(), constraint.get_id())
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
