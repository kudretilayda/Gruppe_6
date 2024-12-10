from src.server.db.Mapper import Mapper
from src.server.constraints import Constraint


class ConstraintMapper(Mapper):
    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * FROM constraint_rule")
        tuples = cursor.fetchall()

        for (id, style_id, constraint_type, attribute, constrain, val) in tuples:
            constraint = Constraint()
            constraint.set_id(id)
            constraint.set_style_id(style_id)
            constraint.set_constraint_type(constraint_type)
            constraint.set_attribute(attribute)
            constraint.set_constrain(constrain)
            constraint.set_value(val)

            if constraint_type == 'unary':
                cursor.execute(f"SELECT reference_object_id FROM unary_constraint WHERE id={id}")
                unary_data = cursor.fetchone()
                if unary_data:
                    constraint.set_reference_object_id(unary_data[0])
            elif constraint_type == 'binary':
                cursor.execute(f"SELECT reference_object1_id, reference_object2_id FROM binary_constraint WHERE id={id}")
                binary_data = cursor.fetchone()
                if binary_data:
                    constraint.set_reference_object1_id(binary_data[0])
                    constraint.set_reference_object2_id(binary_data[1])
            elif constraint_type == 'implikation':
                # Add specific fields for implication constraints if needed
                pass
            elif constraint_type == 'mutex':
                # Add specific fields for mutex constraints if needed
                pass
            elif constraint_type == 'kardinalitaet':
                # Add specific fields for cardinality constraints if needed
                pass

            result.append(constraint)

        self._cnx.commit()
        cursor.close()
        return result

    def find_by_key(self, key):
        result = None
        cursor = self._cnx.cursor()
        command = f"SELECT * FROM constraint_rule WHERE id={key}"
        cursor.execute(command)
        tuples = cursor.fetchall()

        if tuples:
            (id, style_id, constraint_type, attribute, constrain, val) = tuples[0]
            result = Constraint()
            result.set_id(id)
            result.set_style_id(style_id)
            result.set_constraint_type(constraint_type)
            result.set_attribute(attribute)
            result.set_constrain(constrain)
            result.set_value(val)

            if constraint_type == 'unary':
                cursor.execute(f"SELECT reference_object_id FROM unary_constraint WHERE id={id}")
                unary_data = cursor.fetchone()
                if unary_data:
                    result.set_reference_object_id(unary_data[0])
            elif constraint_type == 'binary':
                cursor.execute(f"SELECT reference_object1_id, reference_object2_id FROM binary_constraint WHERE id={id}")
                binary_data = cursor.fetchone()
                if binary_data:
                    result.set_reference_object1_id(binary_data[0])
                    result.set_reference_object2_id(binary_data[1])
            elif constraint_type == 'implikation':
                pass
            elif constraint_type == 'mutex':
                pass
            elif constraint_type == 'kardinalitaet':
                pass

        self._cnx.commit()
        cursor.close()
        return result

    def insert(self, constraint):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM constraint_rule")
        max_id = cursor.fetchone()[0]
        constraint.set_id(max_id + 1 if max_id else 1)

        command = ("INSERT INTO constraint_rule (id, style_id, constraint_type, attribute, constrain, val) "
                   "VALUES (%s, %s, %s, %s, %s, %s)")
        data = (constraint.get_id(), constraint.get_style_id(), constraint.get_constraint_type(),
                constraint.get_attribute(), constraint.get_constrain(), constraint.get_value())
        cursor.execute(command, data)

        if constraint.get_constraint_type() == 'unary':
            unary_command = ("INSERT INTO unary_constraint (id, reference_object_id, attribute, constrain, val) "
                             "VALUES (%s, %s, %s, %s, %s)")
            unary_data = (constraint.get_id(), constraint.get_reference_object_id(),
                          constraint.get_attribute(), constraint.get_constrain(), constraint.get_value())
            cursor.execute(unary_command, unary_data)
        elif constraint.get_constraint_type() == 'binary':
            binary_command = ("INSERT INTO binary_constraint (id, reference_object1_id, reference_object2_id) "
                              "VALUES (%s, %s, %s)")
            binary_data = (constraint.get_id(), constraint.get_reference_object1_id(), constraint.get_reference_object2_id())
            cursor.execute(binary_command, binary_data)
        elif constraint.get_constraint_type() == 'implikation':
            pass
        elif constraint.get_constraint_type() == 'mutex':
            pass
        elif constraint.get_constraint_type() == 'kardinalitaet':
            pass

        self._cnx.commit()
        cursor.close()
        return constraint

    def update(self, constraint):
        pass

    def delete(self, constraint):
        cursor = self._cnx.cursor()

        if constraint.get_constraint_type() == 'unary':
            cursor.execute(f"DELETE FROM unary_constraint WHERE id={constraint.get_id()}")
        elif constraint.get_constraint_type() == 'binary':
            cursor.execute(f"DELETE FROM binary_constraint WHERE id={constraint.get_id()}")
        elif constraint.get_constraint_type() == 'implikation':
            pass
        elif constraint.get_constraint_type() == 'mutex':
            pass
        elif constraint.get_constraint_type() == 'kardinalitaet':
            pass

        cursor.execute(f"DELETE FROM constraint_rule WHERE id={constraint.get_id()}")
        self._cnx.commit()
        cursor.close()
