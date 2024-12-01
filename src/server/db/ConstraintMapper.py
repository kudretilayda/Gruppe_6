import mysql.connector as connector
from src.server.bo.Constraint import Constraint
from src.server.bo.BinaryConstraint import BinaryConstraint
from src.server.bo.CardinalityConstraint import CardinalityConstraint
from src.server.bo.UnaryConstraint import UnaryConstraint
from src.server.bo.ImplicationConstraint import ImplicationConstraint
from src.server.bo.MutexConstraint import MutexConstraint


class ConstraintMapper:
    def __init__(self, connection):
        self.connection = connection

    def find_by_id(self, constraint_id):
        cursor = self.connection.cursor()
        query = "SELECT * FROM constraints WHERE id = %s"
        cursor.execute(query, (constraint_id,))
        result = cursor.fetchone()
        if result:
            constraint_type = result[1]
            if constraint_type == 'implication':
                return ImplicationConstraint(result[0], result[2], result[3])
            elif constraint_type == 'mutex':
                return MutexConstraint(result[0], result[2], result[3])
            elif constraint_type == 'cardinality':
                return CardinalityConstraint(result[0], result[2], result[3], result[4])
            elif constraint_type == 'unary':
                return UnaryConstraint(result[0], result[2], result[3])
            elif constraint_type == 'binary':
                return BinaryConstraint(result[0], result[2], result[3], result[4])
        return None

    def find_all(self):
        cursor = self.connection.cursor()
        query = "SELECT * FROM constraints"
        cursor.execute(query)
        results = cursor.fetchall()
        constraints = []
        for result in results:
            constraint_type = result[1]
            if constraint_type == 'implication':
                constraints.append(ImplicationConstraint(result[0], result[2], result[3]))
            elif constraint_type == 'mutex':
                constraints.append(MutexConstraint(result[0], result[2], result[3]))
            elif constraint_type == 'cardinality':
                constraints.append(CardinalityConstraint(result[0], result[2], result[3], result[4]))
            elif constraint_type == 'unary':
                constraints.append(UnaryConstraint(result[0], result[2], result[3]))
            elif constraint_type == 'binary':
                constraints.append(BinaryConstraint(result[0], result[2], result[3], result[4]))
        return constraints

    def save(self, constraint):
        cursor = self.connection.cursor()
        if isinstance(constraint, ImplicationConstraint):
            query = "INSERT INTO constraints (type, object1, object2) VALUES (%s, %s, %s)"
            cursor.execute(query, ('implication', constraint.object1, constraint.object2))
        elif isinstance(constraint, MutexConstraint):
            query = "INSERT INTO constraints (type, object1, object2) VALUES (%s, %s, %s)"
            cursor.execute(query, ('mutex', constraint.object1, constraint.object2))
        elif isinstance(constraint, CardinalityConstraint):
            query = "INSERT INTO constraints (type, object, min_count, max_count) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, ('cardinality', constraint.object, constraint.min_count, constraint.max_count))
        elif isinstance(constraint, UnaryConstraint):
            query = 'INSERT INTO constraints (type, object, condition) VALUES (%s, %s, %s)'
            cursor.execute(query, ('unary', constraint.object, constraint.condition))
        elif isinstance(constraint, BinaryConstraint):
            query = "INSERT INTO constraints (type, object1, object2, condition) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, ('binary', constraint.object1, constraint.object2, constraint.condition))
        self.connection.commit()


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