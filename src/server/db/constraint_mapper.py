from bo.constraint import Constraint
from db_connector import DBConnector

class ConstraintMapper:
    @staticmethod
    def find_by_id(constraint_id):
        conn = DBConnector.get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM constraint WHERE id = %s", (constraint_id,))
            data = cursor.fetchone()
            if data:
                if data['type'] == 'unary':
                    constraint = UnaryConstraint()
                    constraint.set_reference_object(data['reference_object'])
                elif data['type'] == 'binary':
                    constraint = BinaryConstraint()
                    constraint.set_reference_object1(data['reference_object1'])
                    constraint.set_reference_object2(data['reference_object2'])
                constraint.set_id(data['id'])
                return constraint
            return None
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def insert(constraint):
        conn = DBConnector.get_connection()
        cursor = conn.cursor()
        try:
            if isinstance(constraint, UnaryConstraint):
                cursor.execute("""
                    INSERT INTO constraint (type, reference_object) 
                    VALUES ('unary', %s)
                """, (constraint.get_reference_object(),))
            elif isinstance(constraint, BinaryConstraint):
                cursor.execute("""
                    INSERT INTO constraint (type, reference_object1, reference_object2) 
                    VALUES ('binary', %s, %s)
                """, (constraint.get_reference_object1(), constraint.get_reference_object2()))
            constraint_id = cursor.lastrowid
            conn.commit()
            constraint.set_id(constraint_id)
            return constraint_id
        finally:
            cursor.close()
            conn.close()