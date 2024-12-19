from src.server.db.Mapper import Mapper
from src.server.bo.Constraints.Constraint import (
    UnaryConstraint,
    BinaryConstraint,
    ImplicationConstraint,
    MutexConstraint,
    CardinalityConstraint)


class ConstraintMapper(Mapper):

    def find_all(self):
        result = []
        cursor = self._cnx.cursor()

        query = ("SELECT id, style_id, constraint_type, attribute, constrain, val "
                 "FROM digital_wardrobe.constraint_rule")
        cursor.execute(query)
        tuples = cursor.fetchall()

        for (constraint_id, style_id, constraint_type, attribute, condition, value) in tuples:
            if constraint_type == "unary":
                unary_query = "SELECT reference_object_id FROM digital_wardrobe.unary_constraint WHERE id = %s"
                cursor.execute(unary_query, (constraint_id,))
                unary_data = cursor.fetchone()
                if unary_data:
                    result.append(UnaryConstraint(style_id, unary_data[0], attribute, condition, value))

            elif constraint_type == "binary":
                binary_query = ("SELECT reference_object1_id, reference_object2_id "
                                "FROM digital_wardrobe.binary_constraint WHERE id = %s")
                cursor.execute(binary_query, (constraint_id,))
                binary_data = cursor.fetchone()
                if binary_data:
                    result.append(
                        BinaryConstraint(style_id, binary_data[0], binary_data[1], attribute, condition, value))

            elif constraint_type == "implication":
                result.append(ImplicationConstraint(style_id, None, None))

            elif constraint_type == "mutex":
                # result.append(MutexConstraint(style_id, []))
                result.append(MutexConstraint(style_id, []))


            elif constraint_type == "cardinality":
                # result.append(CardinalityConstraint(style_id, [], min_count, max_count))
                result.append(CardinalityConstraint(style_id, [], int(condition), int(value)))

            self._cnx.commit()
            cursor.close()
            return result

    def find_by_key(self, key):
        cursor = self._cnx.cursor()
        query = ("SELECT id, style_id, constraint_type, attribute, constrain, val "
                 "FROM digital_wardrobe.constraint_rule WHERE id = %s")
        cursor.execute(query, (key,))
        result = cursor.fetchone()

        if result:
            (constraint_id, style_id, constraint_type, attribute, condition, value) = result

            if constraint_type == "unary":
                unary_query = ("SELECT reference_object_id "
                               "FROM digital_wardrobe.unary_constraint WHERE id = %s")
                cursor.execute(unary_query, (constraint_id,))
                unary_data = cursor.fetchone()
                if unary_data:
                    return UnaryConstraint(style_id, unary_data[0], attribute, condition, value)

            elif constraint_type == "binary":
                binary_query = ("SELECT reference_object1_id, reference_object2_id "
                                "FROM digital_wardrobe.binary_constraint WHERE id = %s")
                cursor.execute(binary_query, (constraint_id,))
                binary_data = cursor.fetchone()
                if binary_data:
                    return BinaryConstraint(style_id, binary_data[0], binary_data[1], attribute, condition, value)

            elif constraint_type == "implication":
                return ImplicationConstraint(style_id, None, None)

            elif constraint_type == "mutex":
                result.append(MutexConstraint(style_id, []))
                return result

            elif constraint_type == "cardinality":
                min_count = int(condition) if condition and condition.isdigit() else 0
                max_count = int(value) if value and value.isdigit() else 0
                result.append(CardinalityConstraint(style_id, [], min_count, max_count))
                return result

        cursor.close()
        return None

    def insert(self, constraint):
        cursor = self._cnx.cursor()

        query_rule = """INSERT INTO digital_wardrobe.constraint_rule 
        (style_id, constraint_type, attribute, constrain, val) VALUES (%s, %s, %s, %s, %s)"""

        cursor.execute(query_rule, (
            constraint.style_id,
            constraint.constraint_type,
            constraint.attribute,
            constraint.condition,
            constraint.val
        ))

        constraint_id = cursor.lastrowid

        if isinstance(constraint, UnaryConstraint):
            unary_query = ("INSERT INTO digital_wardrobe.unary_constraint (id, reference_object_id) "
                           "VALUES (%s, %s)")
            cursor.execute(unary_query, (constraint_id, constraint.reference_object_id))

        elif isinstance(constraint, BinaryConstraint):
            binary_query = """INSERT INTO digital_wardrobe.binary_constraint 
            (id, reference_object1_id, reference_object2_id) VALUES (%s, %s, %s)"""
            cursor.execute(binary_query, (constraint_id, constraint.object_1, constraint.object_2))

        self._cnx.commit()
        cursor.close()
        return constraint

    def update(self, constraint):
        cursor = self._cnx.cursor()
        query_rule = """UPDATE digital_wardrobe.constraint_rule 
            SET style_id = %s, attribute = %s, constrain = %s, val = %s WHERE id = %s"""
        cursor.execute(query_rule, (
            constraint.style_id,
            constraint.attribute,
            constraint.condition,
            constraint.val,
            constraint.style_id
        ))

        if isinstance(constraint, UnaryConstraint):
            unary_query = ("UPDATE digital_wardrobe.unary_constraint "
                           "SET reference_object_id = %s WHERE id = %s")
            cursor.execute(unary_query, (constraint.reference_object_id, constraint.style_id))

        elif isinstance(constraint, BinaryConstraint):
            binary_query = """UPDATE digital_wardrobe.binary_constraint 
                SET reference_object1_id = %s, reference_object2_id = %s WHERE id = %s"""
            cursor.execute(binary_query, (constraint.object_1, constraint.object_2, constraint.style_id))

        self._cnx.commit()
        cursor.close()

    def delete(self, constraint):
        cursor = self._cnx.cursor()

        if isinstance(constraint, UnaryConstraint):
            unary_query = "DELETE FROM digital_wardrobe.unary_constraint WHERE id = %s"
            cursor.execute(unary_query, (constraint.style_id,))

        elif isinstance(constraint, BinaryConstraint):
            binary_query = "DELETE FROM digital_wardrobe.binary_constraint WHERE id = %s"
            cursor.execute(binary_query, (constraint.style_id,))

        query_rule = "DELETE FROM digital_wardrobe.constraint_rule WHERE id = %s"
        cursor.execute(query_rule, (constraint.style_id,))

        self._cnx.commit()
        cursor.close()
