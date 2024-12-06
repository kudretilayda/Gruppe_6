from server.db.Mapper import Mapper
from server.bo.ConstraintRule import MutexConstraint
import uuid

class MutexMapper(Mapper):
    def __init__(self):
        super().__init__()

    def find_by_id(self, constraint_id):
        cursor = self._cnx.cursor()
        command = """SELECT cr.id, cr.style_id, mt.type_id
                    FROM constraint_rule cr
                    JOIN mutex_types mt ON cr.id = mt.mutex_id
                    WHERE cr.id=%s"""
        cursor.execute(command, (constraint_id,))
        tuples = cursor.fetchall()

        try:
            constraint = MutexConstraint()
            constraint.set_id(tuples[0][0])
            constraint.set_style_id(tuples[0][1])
            for tuple in tuples:
                constraint.add_excluded_type(tuple[2])
            return constraint
        except IndexError:
            return None
        finally:
            self._cnx.commit()
            cursor.close()

    def find_by_style(self, style_id):
        cursor = self._cnx.cursor()
        command = """SELECT cr.id, cr.style_id, mt.type_id
                    FROM constraint_rule cr
                    JOIN mutex_types mt ON cr.id = mt.mutex_id
                    WHERE cr.style_id=%s"""
        cursor.execute(command, (style_id,))
        tuples = cursor.fetchall()
        
        constraints = {}
        for tuple in tuples:
            if tuple[0] not in constraints:
                constraint = MutexConstraint()
                constraint.set_id(tuple[0])
                constraint.set_style_id(tuple[1])
                constraints[tuple[0]] = constraint
            constraints[tuple[0]].add_excluded_type(tuple[2])

        self._cnx.commit()
        cursor.close()
        return list(constraints.values())

    def insert(self, constraint):
        cursor = self._cnx.cursor()
        try:
            if not constraint.get_id():
                constraint.set_id(str(uuid.uuid4()))

            command = """INSERT INTO constraint_rule 
                        (id, style_id, constraint_type) VALUES (%s,%s,'mutex')"""
            cursor.execute(command, (constraint.get_id(), constraint.get_style_id()))

            for type_id in constraint.get_excluded_types():
                command = """INSERT INTO mutex_types 
                           (mutex_id, type_id) VALUES (%s,%s)"""
                cursor.execute(command, (constraint.get_id(), type_id))

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
            cursor.execute("""DELETE FROM mutex_types WHERE mutex_id=%s""", 
                         (constraint.get_id(),))
            
            for type_id in constraint.get_excluded_types():
                command = """INSERT INTO mutex_types 
                           (mutex_id, type_id) VALUES (%s,%s)"""
                cursor.execute(command, (constraint.get_id(), type_id))
                
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