from server.db.Mapper import Mapper
from server.bo.ConstraintRule import Constraint, BinaryConstraint, UnaryConstraint
import uuid

class ConstraintMapper(Mapper):
    def __init__(self):
        super().__init__()

    def find_by_style(self, style_id):
        cursor = self._cnx.cursor()
        command = """
            SELECT cr.*, bc.reference_object1_id, bc.reference_object2_id,
                   uc.reference_object_id
            FROM constraint_rule cr
            LEFT JOIN binary_constraint bc ON cr.id = bc.id
            LEFT JOIN unary_constraint uc ON cr.id = uc.id
            WHERE cr.style_id=%s"""
        cursor.execute(command, (style_id,))
        tuples = cursor.fetchall()
        result = []

        for tuple in tuples:
            if tuple[4]:  # Binary constraint
                constraint = BinaryConstraint()
                constraint.set_reference_object1_id(tuple[4])
                constraint.set_reference_object2_id(tuple[5])
            elif tuple[6]:  # Unary constraint
                constraint = UnaryConstraint()
                constraint.set_reference_object_id(tuple[6])
            else:
                constraint = Constraint()

            constraint.set_id(tuple[0])
            constraint.set_style_id(tuple[1])
            constraint.set_constraint_type(tuple[2])
            result.append(constraint)

        self._cnx.commit()
        cursor.close()
        return result

    def insert(self, constraint):
        cursor = self._cnx.cursor()
        try:
            if not constraint.get_id():
                constraint.set_id(str(uuid.uuid4()))

            command = "INSERT INTO constraint_rule (id, style_id, constraint_type) VALUES (%s,%s,%s)"
            data = (constraint.get_id(), constraint.get_style_id(), constraint.get_constraint_type())
            cursor.execute(command, data)

            if isinstance(constraint, BinaryConstraint):
                command = """INSERT INTO binary_constraint 
                           (id, reference_object1_id, reference_object2_id)
                           VALUES (%s,%s,%s)"""
                data = (constraint.get_id(), constraint.get_reference_object1_id(),
                       constraint.get_reference_object2_id())
                cursor.execute(command, data)
            elif isinstance(constraint, UnaryConstraint):
                command = "INSERT INTO unary_constraint (id, reference_object_id) VALUES (%s,%s)"
                data = (constraint.get_id(), constraint.get_reference_object_id())
                cursor.execute(command, data)

            self._cnx.commit()
            return constraint
        except:
            self._cnx.rollback()
            raise
        finally:
            cursor.close()

    def delete(self, constraint):
        cursor = self._cnx.cursor()
        try:
            # Constraints will be cascade deleted from binary/unary tables
            command = "DELETE FROM constraint_rule WHERE id=%s"
            cursor.execute(command, (constraint.get_id(),))
            self._cnx.commit()
        except:
            self._cnx.rollback()
            raise
        finally:
            cursor.close()
