from src.server.db.Mapper import Mapper
from src.server.constraints.BinaryConstraint import BinaryConstraint
from src.server.constraints.CardinalityConstraint import CardinalityConstraint
from src.server.constraints.UnaryConstraint import UnaryConstraint
from src.server.constraints.ImplicationConstraint import ImplicationConstraint
from src.server.constraints.MutexConstraint import MutexConstraint


class ConstraintMapper(Mapper):
    def find_all(self):
        cursor = self._cnx.cursor()
        query = "SELECT * FROM digital_wardrobe.constraint_rule"
        cursor.execute(query)
        results = cursor.fetchall()
        constraints = []

        for result in results:
            constraint_type = result[1]
            if constraint_type == 'implication':
                constraints.append(ImplicationConstraint(result[0], result[2]))

            elif constraint_type == 'mutex':
                constraints.append(MutexConstraint(result[0], result[2]))

            elif constraint_type == 'cardinality':
                constraints.append(CardinalityConstraint(result[0], result[2], result[3]))

            elif constraint_type == 'unary':
                constraints.append(UnaryConstraint(result[0], result[2]))

            elif constraint_type == 'binary':
                constraints.append(BinaryConstraint(result[0], result[2], result[3]))
        return constraints

    def find_by_key(self, constraint_id):
        cursor = self._cnx.cursor()
        query = "SELECT * FROM digital_wardrobe.constraint_rule WHERE id = %s"
        cursor.execute(query, (constraint_id,))
        result = cursor.fetchone()

        if result:
            constraint_type = result[1]
            if constraint_type == 'implication':
                return ImplicationConstraint(result[0], result[2])

            elif constraint_type == 'mutex':
                return MutexConstraint(result[0], result[2])

            elif constraint_type == 'cardinality':
                return CardinalityConstraint(result[0], result[2], result[3])

            elif constraint_type == 'unary':
                return UnaryConstraint(result[0], result[2])

            elif constraint_type == 'binary':
                return BinaryConstraint(result[0], result[2], result[3])

            return None

        self._cnx.commit()
        cursor.close()

    def insert(self, constraint):
        cursor = self._cnx.cursor()
        if isinstance(constraint, ImplicationConstraint):
            query = ("INSERT INTO digital_wardrobe.implication_constraint (constraint_id, antecedent_object_id, "
                     "consequent_object_id) VALUES (%s, %s, %s)")
            cursor.execute(query, ('implication', constraint.condition, constraint.implication))

        elif isinstance(constraint, MutexConstraint):
            query = ("INSERT INTO digital_wardrobe.mutex_constraint (constraint_id, conflicting_object1_id,"
                     "conflicting_object2_id) VALUES (%s, %s, %s)")
            cursor.execute(query, ('mutex', constraint.object1, constraint.object2))

        elif isinstance(constraint, CardinalityConstraint):
            query = ("INSERT INTO digital_wardrobe.cardinality_constraint (constraint_id, reference_object_id, "
                     "min_value, max_value) VALUES (%s, %s, %s, %s)")
            cursor.execute(query, ('cardinality', constraint.object, constraint.min_count, constraint.max_count))

        elif isinstance(constraint, UnaryConstraint):
            query = ('INSERT INTO digital_wardrobe.unary_constraint (constraint_id, '
                     'reference_object_id) VALUES (%s, %s)')
            cursor.execute(query, ('unary', constraint.obj))

        elif isinstance(constraint, BinaryConstraint):
            query = ("INSERT INTO digital_wardrobe.binary_constraint (constraint_id, "
                     "reference_object1_id, reference_object2_id) VALUES (%s, %s, %s)")
            cursor.execute(query, ('binary', constraint.object1, constraint.object2))

        self._cnx.commit()
        cursor.close()

    def update(self, constraint):
        cursor = self._cnx.cursor()

        if isinstance(constraint, UnaryConstraint):
            query = ("UPDATE digital_wardrobe.unary_constraint "
                     "SET reference_object_id = %s "
                     "WHERE constraint_id = %s")
            data = (constraint.obj, constraint.constraint_id)
            cursor.execute(query, data)

        elif isinstance(constraint, BinaryConstraint):
            query = ("UPDATE digital_wardrobe.binary_constraint "
                     "SET reference_object1_id = %s, reference_object2_id = %s "
                     "WHERE constraint_id = %s")
            data = (constraint.object1, constraint.object2, constraint.constraint_id)
            cursor.execute(query, data)

        elif isinstance(constraint, ImplicationConstraint):
            query = ("UPDATE digital_wardrobe.implication_constraint "
                     "SET antecedent_object_id = %s, consequent_object_id = %s "
                     "WHERE constraint_id = %s")
            data = (constraint.condition, constraint.implication, constraint.constraint_id)
            cursor.execute(query, data)

        elif isinstance(constraint, MutexConstraint):
            query = ("UPDATE digital_wardrobe.mutex_constraint "
                     "SET conflicting_object1_id=%s, conflicting_object2_id=%s "
                     "WHERE constraint_id=%s")
            data = (constraint.object1, constraint.object2, constraint.constraint_id)
            cursor.execute(query, data)

        elif isinstance(constraint, CardinalityConstraint):
            query = ("UPDATE digital_wardrobe.cardinality_constraint "
                     "SET cardinality_constraint.reference_object_id = %s, min_value = %s, max_value = %s "
                     "WHERE constraint_id = %s")
            data = (constraint.object, constraint.min_count, constraint.max_count, constraint.constraint_id)
            cursor.execute(query, data)

        self._cnx.commit()
        cursor.close()

    def delete(self, constraint):
        cursor = self._cnx.cursor()

        if isinstance(constraint, UnaryConstraint):
            query = "DELETE FROM digital_wardrobe.unary_constraint WHERE constraint_id = %s"
            cursor.execute(query, constraint.constraint_id)

        elif isinstance(constraint, BinaryConstraint):
            query = "DELETE FROM digital_wardrobe.binary_constraint WHERE constraint_id=%s"
            cursor.execute(query, constraint.constraint_id)

        elif isinstance(constraint, ImplicationConstraint):
            query = "DELETE FROM digital_wardrobe.implication_constraint WHERE constraint_id=%s"
            cursor.execute(query, constraint.constraint_id)

        elif isinstance(constraint, MutexConstraint):
            query = "DELETE FROM digital_wardrobe.mutex_constraint WHERE constraint_id=%s"
            cursor.execute(query, constraint.constraint_id)

        elif isinstance(constraint, CardinalityConstraint):
            query = "DELETE FROM digital_wardrobe.cardinality_constraint WHERE constraint_id=%s"
            cursor.execute(query, constraint.constraint_id)

        # Constraint Rule löschen, um die Konsistenz zu wahren
        query = "DELETE FROM digital_wardrobe.constraint_rule WHERE id=%s"
        cursor.execute(query, (constraint.id,))

        self._cnx.commit()
        cursor.close()


"""
class ImplicationConstraint:
    def __init__(self, constraint_id, object1, object2):
        self.id = constraint_id
        self.object1 = object1
        self.object2 = object2

class MutexConstraint:
    def __init__(self, constraint_id, object1, object2):
        self.id = constraint_id
        self.object1 = object1
        self.object2 = object2

class CardinalityConstraint:
    def __init__(self, constraint_id, object, min_count, max_count):
        self.id = constraint_id
        self.object = object
        self.min_count = min_count
        self.max_count = max_count

class UnaryConstraint:
    def __init__(self, constraint_id, object, condition):
        self.id = constraint_id
        self.object = object
        self.condition = condition

class BinaryConstraint:
    def __init__(self, constraint_id, object1, object2, condition):
        self.id = constraint_id
        self.object1 = object1
        self.obeject2 = object2
        self.condition = condition
"""
