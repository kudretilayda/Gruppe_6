# src/db/mapper/style_mapper.py
from .Mapper import Mapper
from server.db import Style

class StyleMapper(Mapper):
    """Mapper class for Style objects"""
    
    def find_by_id(self, id):
        result = None
        cursor = self._get_connection().cursor()
        command = "SELECT id, name, features, created_at FROM style WHERE id=%s"
        cursor.execute(command, (id,))
        tuples = cursor.fetchall()

        try:
            (id, name, features, created_at) = tuples[0]
            result = Style()
            result.id = id
            result.name = name
            result.features = features
            result.created_at = created_at
            
            # Load associated constraints
            result.constraints = self._load_constraints(id)
        except IndexError:
            result = None

        self._get_connection().commit()
        cursor.close()
        return result

    def _load_constraints(self, style_id):
        cursor = self._get_connection().cursor()
        command = """
            SELECT c.id, c.type, c.bezugsobjekt1, c.bezugsobjekt2 
            FROM constraint c
            JOIN style_constraint sc ON c.id = sc.constraint_id
            WHERE sc.style_id = %s
        """
        cursor.execute(command, (style_id,))
        constraints = []
        
        for (id, type, obj1, obj2) in cursor.fetchall():
            constraint = self._create_constraint(type, id, obj1, obj2)
            constraints.append(constraint)
            
        cursor.close()
        return constraints

    def insert(self, style):
        cursor = self._get_connection().cursor()
        command = "INSERT INTO style (name, features) VALUES (%s, %s)"
        data = (style.name, style.features)
        cursor.execute(command, data)
        
        style.id = cursor.lastrowid
        
        # Insert constraints
        if style.constraints:
            self._insert_constraints(style.id, style.constraints)
            
        self._get_connection().commit()
        cursor.close()
        return style