#Unvollständig - nochmak überarbeiten#

# src/db/mapper/constraint_mapper.py
from typing import List, Optional, Type
from .Mapper import Mapper

class ConstraintMapper(Mapper):
    """Mapper class for handling all types of constraints"""
    
    def __init__(self):
        super().__init__()
        # Mapping of constraint types to their respective classes
        self._constraint_types = {
            'mutex': Mutex,
            'kardinalitaet': Kardinalitaet,
            'implikation': Implikation
        }

    def find_by_id(self, id: int) -> Optional[Constraint]:
        """Finds a constraint by its ID"""
        cursor = self._get_connection().cursor()
        
        try:
            # First get the base constraint info
            command = """
                SELECT id, type, created_at 
                FROM constraint 
                WHERE id=%s
            """
            cursor.execute(command, (id,))
            constraint_data = cursor.fetchone()
            
            if not constraint_data:
                return None
                
            constraint_id, constraint_type, created_at = constraint_data
            
            # Get specific constraint details based on type
            if constraint_type in ['mutex', 'implikation']:
                command = """
                    SELECT bezugsobjekt1, bezugsobjekt2
                    FROM binary_constraint
                    WHERE constraint_id=%s
                """
                cursor.execute(command, (id,))
                binary_data = cursor.fetchone()
                
                constraint = self._constraint_types[constraint_type]()
                constraint.id = constraint_id
                constraint.created_at = created_at
                constraint.bezugsobjekt1 = binary_data[0]
                constraint.bezugsobjekt2 = binary_data[1]
                
            elif constraint_type == 'kardinalitaet':
                command = """
                    SELECT bezugsobjekt, min_count, max_count
                    FROM unary_constraint
                    WHERE constraint_id=%s
                """
                cursor.execute(command, (id,))
                unary_data = cursor.fetchone()
                
                constraint = Kardinalitaet()
                constraint.id = constraint_id
                constraint.created_at = created_at
                constraint.bezugsobjekt = unary_data[0]
                constraint.min_count = unary_data[1]
                constraint.max_count = unary_data[2]
                
            return constraint
            
        finally:
            cursor.close()

    def find_by_style(self, style_id: int) -> List[Constraint]:
        """Finds all constraints associated with a style"""
        cursor = self._get_connection().cursor()
        constraints = []
        
        try:
            # Get all constraints for the style
            command = """
                SELECT c.id, c.type, c.created_at
                FROM constraint c
                JOIN style_constraint sc ON c.id = sc.constraint_id
                WHERE sc.style_id = %s
            """
            cursor.execute(command, (style_id,))
            constraint_data = cursor.fetchall()
            
            for (id, type, created_at) in constraint_data:
                constraint = self.find_by_id(id)
                if constraint:
                    constraints.append(constraint)
                    
            return constraints
            
        finally:
            cursor.close()

    def insert(self, constraint: Constraint) -> Constraint:
        """Inserts a new constraint"""
        cursor = self._get_connection().cursor()
        
        try:
            # Insert base constraint info
            command = """
                INSERT INTO constraint (type) 
                VALUES (%s)
            """
            cursor_type = type(constraint).__name__.lower()
            cursor.execute(command, (cursor_type,))
            constraint.id = cursor.lastrowid
            
            # Insert specific constraint details
            if isinstance(constraint, BinaryConstraint):
                command = """
                    INSERT INTO binary_constraint 
                    (constraint_id, bezugsobjekt1, bezugsobjekt2)
                    VALUES (%s, %s, %s)
                """
                data = (constraint.id, constraint.bezugsobjekt1, constraint.bezugsobjekt2)
                cursor.execute(command, data)
                
            elif isinstance(constraint, Kardinalitaet):
                command = """
                    INSERT INTO unary_constraint 
                    (constraint_id, bezugsobjekt, min_count, max_count)
                    VALUES (%s, %s, %s, %s)
                """
                data = (constraint.id, constraint.bezugsobjekt, 
                       constraint.min_count, constraint.max_count)
                cursor.execute(command, data)
            
            self._get_connection().commit()
            return constraint
            
        except Exception:
            self._get_connection().rollback()
            raise
        finally:
            cursor.close()

    def update(self, constraint: Constraint) -> Constraint:
        """Updates an existing constraint"""
        cursor = self._get_connection().cursor()
        
        try:
            if isinstance(constraint, BinaryConstraint):
                command = """
                    UPDATE binary_constraint 
                    SET bezugsobjekt1=%s, bezugsobjekt2=%s
                    WHERE constraint_id=%s
                """
                data = (constraint.bezugsobjekt1, constraint.bezugsobjekt2, constraint.id)
                cursor.execute(command, data)
                
            elif isinstance(constraint, Kardinalitaet):
                command = """
                    UPDATE unary_constraint 
                    SET bezugsobjekt=%s, min_count=%s, max_count=%s
                    WHERE constraint_id=%s
                """
                data = (constraint.bezugsobjekt, constraint.min_count, 
                       constraint.max_count, constraint.id)
                cursor.execute(command, data)
            
            self._get_connection().commit()
            return constraint
            
        except Exception:
            self._get_connection().rollback()
            raise
        finally:
            cursor.close()

    def delete(self, constraint: Constraint) -> bool:
        """Deletes a constraint"""
        cursor = self._get_connection().cursor()
        
        try:
            # Delete specific constraint details first
            if isinstance(constraint, BinaryConstraint):
                command = "DELETE FROM binary_constraint WHERE constraint_id=%s"
                cursor.execute(command, (constraint.id,))
                
            elif isinstance(constraint, Kardinalitaet):
                command = "DELETE FROM unary_constraint WHERE constraint_id=%s"
                cursor.execute(command, (constraint.id,))
            
            # Delete base constraint
            command = "DELETE FROM constraint WHERE id=%s"
            cursor.execute(command, (constraint.id,))
            
            self._get_connection().commit()
            return True
            
        except Exception:
            self._get_connection().rollback()
            raise
        finally:
            cursor.close()

    def assign_to_style(self, style_id: int, constraint: Constraint) -> bool:
        """Assigns a constraint to a style"""
        cursor = self._get_connection().cursor()
        
        try:
            command = """
                INSERT INTO style_constraint (style_id, constraint_id)
                VALUES (%s, %s)
            """
            cursor.execute(command, (style_id, constraint.id))
            self._get_connection().commit()
            return True
            
        except Exception:
            self._get_connection().rollback()
            raise
        finally:
            cursor.close()

    def remove_from_style(self, style_id: int, constraint: Constraint) -> bool:
        """Removes a constraint from a style"""
        cursor = self._get_connection().cursor()
        
        try:
            command = """
                DELETE FROM style_constraint 
                WHERE style_id=%s AND constraint_id=%s
            """
            cursor.execute(command, (style_id, constraint.id))
            self._get_connection().commit()
            return True
            
        except Exception:
            self._get_connection().rollback()
            raise
        finally:
            cursor.close()

    