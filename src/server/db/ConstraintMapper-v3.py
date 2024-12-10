from src.server.db.Mapper import Mapper
from src.server.constraints.BinaryConstraint import BinaryConstraint
from src.server.constraints.CardinalityConstraint import CardinalityConstraint
from src.server.constraints.UnaryConstraint import UnaryConstraint
from src.server.constraints.ImplicationConstraint import ImplicationConstraint
from src.server.constraints.MutexConstraint import MutexConstraint


class ConstraintMapper(Mapper):
    def find_by_key(self, constraint_id):
        cursor = self._cnx.cursor()
        query = "SELECT * FROM digital_wardrobe.constraint_rule WHERE id = %s"
        cursor.execute(query, (constraint_id,))
        result = cursor.fetchone()

        if result:
            constraint_type = result[2]
            if constraint_type == 'unary':
                query = "SELECT reference_object_id FROM unary_constraint WHERE id = %s"
                cursor.execute(query, (constraint_id,))
                unary_data = cursor.fetchone()
                return UnaryConstraint(result[0], result[3], result[4], result[5], unary_data[0])

            elif constraint_type == 'binary':
                query = "SELECT reference_object1_id, reference_object2_id FROM binary_constraint WHERE id = %s"
                cursor.execute(query, (constraint_id,))
                binary_data = cursor.fetchone()
                return BinaryConstraint(result[0], result[3], result[4], result[5], binary_data[0], binary_data[1])

            elif constraint_type == 'implication':
                # Placeholder for implication-specific logic
                return ImplicationConstraint(result[0], result[3], result[4], result[5])

            elif constraint_type == 'mutex':
                # Placeholder for mutex-specific logic
                return MutexConstraint(result[0], result[3], result[4], result[5])

            elif constraint_type == 'kardinalitaet':
                # Placeholder for cardinality-specific logic
                return CardinalityConstraint(result[0], result[3], result[4], result[5])

        self._cnx.commit()
        cursor.close()
        return None

    def find_all(self):
        cursor = self._cnx.cursor()
        query = "SELECT * FROM constraint_rule"
        cursor.execute(query)
        results = cursor.fetchall()
        constraints = []

        for result in results:
            constraint_type = result[2]
            if constraint_type == 'unary':
                query = "SELECT reference_object_id FROM unary_constraint WHERE id = %s"
                cursor.execute(query, (result[0],))
                unary_data = cursor.fetchone()
                constraints.append(UnaryConstraint(result[0], result[3], result[4], result[5], unary_data[0]))

            elif constraint_type == 'binary':
                query = "SELECT reference_object1_id, reference_object2_id FROM binary_constraint WHERE id = %s"
                cursor.execute(query, (result[0],))
                binary_data = cursor.fetchone()
                constraints.append(BinaryConstraint(result[0], result[3], result[4], result[5], binary_data[0], binary_data[1]))

            elif constraint_type == 'implication':
                constraints.append(ImplicationConstraint(result[0], result[3], result[4], result[5]))

            elif constraint_type == 'mutex':
                constraints.append(MutexConstraint(result[0], result[3], result[4], result[5]))

            elif constraint_type == 'kardinalitaet':
                constraints.append(CardinalityConstraint(result[0], result[3], result[4], result[5]))

        self._cnx.commit()
        cursor.close()
        return constraints

    def insert(self, constraint):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM constraint_rule")
        max_id = cursor.fetchone()[0]
        constraint.set_id(max_id + 1 if max_id else 1)

        query = ("INSERT INTO constraint_rule (id, style_id, constraint_type, attribute, constrain, val) "
                 "VALUES (%s, %s, %s, %s, %s, %s)")
        cursor.execute(query, (constraint.id, constraint.style_id, constraint.type, constraint.attribute,
                               constraint.constrain, constraint.value))

        if isinstance(constraint, UnaryConstraint):
            unary_query = "INSERT INTO unary_constraint (id, reference_object_id) VALUES (%s, %s)"
            cursor.execute(unary_query, (constraint.id, constraint.reference_object_id))

        elif isinstance(constraint, BinaryConstraint):
            binary_query = "INSERT INTO binary_constraint (id, reference_object1_id, reference_object2_id) VALUES (%s, %s, %s)"
            cursor.execute(binary_query, (constraint.id, constraint.reference_object1_id, constraint.reference_object2_id))

        self._cnx.commit()
        cursor.close()

    def update(self, constraint):
        cursor = self._cnx.cursor()
        query = ("UPDATE constraint_rule SET style_id=%s, attribute=%s, constrain=%s, val=%s WHERE id=%s")
        cursor.execute(query, (constraint.style_id, constraint.attribute, constraint.constrain, constraint.value, constraint.id))

        if isinstance(constraint, UnaryConstraint):
            unary_query = "UPDATE unary_constraint SET reference_object_id=%s WHERE id=%s"
            cursor.execute(unary_query, (constraint.reference_object_id, constraint.id))

        elif isinstance(constraint, BinaryConstraint):
            binary_query = "UPDATE binary_constraint SET reference_object1_id=%s, reference_object2_id=%s WHERE id=%s"
            cursor.execute(binary_query, (constraint.reference_object1_id, constraint.reference_object2_id, constraint.id))

        self._cnx.commit()
        cursor.close()

    def delete(self, constraint):
        cursor = self._cnx.cursor()

        if isinstance(constraint, UnaryConstraint):
            unary_query = "DELETE FROM unary_constraint WHERE id=%s"
            cursor.execute(unary_query, (constraint.id,))

        elif isinstance(constraint, BinaryConstraint):
            binary_query = "DELETE FROM binary_constraint WHERE id=%s"
            cursor.execute(binary_query, (constraint.id,))

        query = "DELETE FROM constraint_rule WHERE id=%s"
        cursor.execute(query, (constraint.id,))

        self._cnx.commit()
        cursor.close()
