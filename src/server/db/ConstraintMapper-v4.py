from src.server.db.Mapper import Mapper
from src.server.constraints.UnaryConstraint import UnaryConstraint
from src.server.constraints.BinaryConstraint import BinaryConstraint
from src.server.constraints.ImplicationConstraint import ImplicationConstraint
from src.server.constraints.MutexConstraint import MutexConstraint
from src.server.constraints.CardinalityConstraint import CardinalityConstraint


class ConstraintMapper(Mapper):
    """
    Mapper-Klasse für die Verwaltung von Constraints in der Datenbank.
    """

    def find_by_key(self, constraint_id):
        cursor = self._cnx.cursor()
        query = "SELECT * FROM constraint_rule WHERE id = %s"
        cursor.execute(query, (constraint_id,))
        result = cursor.fetchone()

        if result:
            constraint_type = result[2]
            if constraint_type == 'unary':
                query = "SELECT reference_object_id FROM unary_constraint WHERE id = %s"
                cursor.execute(query, (constraint_id,))
                unary_data = cursor.fetchone()
                return UnaryConstraint(
                    style_id=result[1],
                    reference_object=unary_data[0],
                    attribute=result[3],
                    condition=result[4],
                    value=result[5]
                )

            elif constraint_type == 'binary':
                query = "SELECT reference_object1_id, reference_object2_id FROM binary_constraint WHERE id = %s"
                cursor.execute(query, (constraint_id,))
                binary_data = cursor.fetchone()
                return BinaryConstraint(
                    style_id=result[1],
                    object1=binary_data[0],
                    object2=binary_data[1],
                    attribute=result[3],
                    condition=result[4],
                    value=result[5]
                )

            elif constraint_type == 'implication':
                # Hier kann spezifische Logik für Implikationen hinzugefügt werden
                return ImplikationConstraint(
                    style_id=result[1],
                    condition_a=None,  # Platzhalter für echte Logik
                    condition_b=None
                )

            elif constraint_type == 'mutex':
                # Hier kann spezifische Logik für Mutex hinzugefügt werden
                return MutexConstraint(
                    style_id=result[1],
                    objects=None  # Platzhalter für echte Logik
                )

            elif constraint_type == 'cardinality':
                # Hier kann spezifische Logik für Kardinalitäts-Constraints hinzugefügt werden
                return CardinalityConstraint(
                    style_id=result[1],
                    objects=None,  # Platzhalter für echte Logik
                    min_count=int(result[4]),
                    max_count=int(result[5])
                )

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
                constraints.append(UnaryConstraint(
                    style_id=result[1],
                    reference_object=unary_data[0],
                    attribute=result[3],
                    condition=result[4],
                    value=result[5]
                ))

            elif constraint_type == 'binary':
                query = "SELECT reference_object1_id, reference_object2_id FROM binary_constraint WHERE id = %s"
                cursor.execute(query, (result[0],))
                binary_data = cursor.fetchone()
                constraints.append(BinaryConstraint(
                    style_id=result[1],
                    object1=binary_data[0],
                    object2=binary_data[1],
                    attribute=result[3],
                    condition=result[4],
                    value=result[5]
                ))

            elif constraint_type == 'implication':
                constraints.append(ImplikationConstraint(
                    style_id=result[1],
                    condition_a=None,  # Platzhalter
                    condition_b=None
                ))

            elif constraint_type == 'mutex':
                constraints.append(MutexConstraint(
                    style_id=result[1],
                    objects=None  # Platzhalter
                ))

            elif constraint_type == 'cardinality':
                constraints.append(CardinalityConstraint(
                    style_id=result[1],
                    objects=None,  # Platzhalter
                    min_count=int(result[4]),
                    max_count=int(result[5])
                ))

        self._cnx.commit()
        cursor.close()
        return constraints

    def insert(self, constraint):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM constraint_rule")
        max_id = cursor.fetchone()[0]
        constraint_id = max_id + 1 if max_id else 1

        query = ("INSERT INTO constraint_rule (id, style_id, constraint_type, attribute, constrain, val) "
                 "VALUES (%s, %s, %s, %s, %s, %s)")
        cursor.execute(query, (
            constraint_id,
            constraint.style_id,
            constraint.constraint_type,
            constraint.attribute,
            constraint.condition,
            constraint.value
        ))

        if isinstance(constraint, UnaryConstraint):
            unary_query = "INSERT INTO unary_constraint (id, reference_object_id) VALUES (%s, %s)"
            cursor.execute(unary_query, (constraint_id, constraint.reference_object))

        elif isinstance(constraint, BinaryConstraint):
            binary_query = "INSERT INTO binary_constraint (id, reference_object1_id, reference_object2_id) VALUES (%s, %s, %s)"
            cursor.execute(binary_query, (constraint_id, constraint.object1, constraint.object2))

        self._cnx.commit()
        cursor.close()

    def update(self, constraint):
        cursor = self._cnx.cursor()
        query = ("UPDATE constraint_rule SET style_id=%s, attribute=%s, constrain=%s, val=%s WHERE id=%s")
        cursor.execute(query, (
            constraint.style_id,
            constraint.attribute,
            constraint.condition,
            constraint.value,
            constraint.id
        ))

        if isinstance(constraint, UnaryConstraint):
            unary_query = "UPDATE unary_constraint SET reference_object_id=%s WHERE id=%s"
            cursor.execute(unary_query, (constraint.reference_object, constraint.id))

        elif isinstance(constraint, BinaryConstraint):
            binary_query = "UPDATE binary_constraint SET reference_object1_id=%s, reference_object2_id=%s WHERE id=%s"
            cursor.execute(binary_query, (constraint.object1, constraint.object2, constraint.id))

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
