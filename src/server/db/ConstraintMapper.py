# src/server/db/mapper/ConstraintMapper.py

from server.db.Mapper import Mapper
from server.bo.Constraint import Constraint

class ConstraintMapper(Mapper):
    """Mapper-Klasse für Constraint-Objekte.
    
    Da alle Constraint-Typen in der Constraint-Klasse durch das constraint_type 
    Attribut abgebildet werden, verwaltet dieser Mapper alle Constraint-Arten."""

    def __init__(self):
        super().__init__()

    def get_table_name(self):
        return "constraint_rule"

    def tuple_to_object(self, tuple):
        """Erstellt ein Constraint-Objekt aus einem DB-Tuple"""
        if not tuple:
            return None
            
        constraint = Constraint()
        constraint.set_id(tuple["id"])
        constraint.set_style_id(tuple["style_id"])
        constraint.set_constraint_type(tuple["constraint_type"])
        constraint.set_create_time(tuple["created_at"])
        
        # Zusätzliche Parameter je nach Constraint-Typ laden
        params = self._load_constraint_parameters(tuple["id"], tuple["constraint_type"])
        for key, value in params.items():
            constraint.add_parameter(key, value)
        
        return constraint

    def _load_constraint_parameters(self, constraint_id, constraint_type):
        """Lädt die spezifischen Parameter eines Constraints basierend auf seinem Typ"""
        params = {}
        with self._cursor() as cursor:
            if constraint_type == "binary":
                command = """
                    SELECT reference_object1_id, reference_object2_id, relation_type 
                    FROM constraint_parameters 
                    WHERE constraint_id=%s
                """
                cursor.execute(command, (constraint_id,))
                result = cursor.fetchone()
                if result:
                    params["reference_object1_id"] = result["reference_object1_id"]
                    params["reference_object2_id"] = result["reference_object2_id"]
                    params["relation_type"] = result["relation_type"]
                    
            elif constraint_type == "unary":
                command = """
                    SELECT reference_object_id, condition 
                    FROM constraint_parameters 
                    WHERE constraint_id=%s
                """
                cursor.execute(command, (constraint_id,))
                result = cursor.fetchone()
                if result:
                    params["reference_object_id"] = result["reference_object_id"]
                    params["condition"] = result["condition"]
                    
            elif constraint_type == "mutex":
                command = """
                    SELECT exclusive_items 
                    FROM constraint_parameters 
                    WHERE constraint_id=%s
                """
                cursor.execute(command, (constraint_id,))
                result = cursor.fetchone()
                if result:
                    params["exclusive_items"] = result["exclusive_items"].split(",")
                    
            elif constraint_type == "kardinalitaet":
                command = """
                    SELECT item_type_id, min_count, max_count 
                    FROM constraint_parameters 
                    WHERE constraint_id=%s
                """
                cursor.execute(command, (constraint_id,))
                result = cursor.fetchone()
                if result:
                    params["item_type_id"] = result["item_type_id"]
                    params["min_count"] = result["min_count"]
                    params["max_count"] = result["max_count"]
                    
            elif constraint_type == "implikation":
                command = """
                    SELECT if_item_id, then_item_id, else_item_id 
                    FROM constraint_parameters 
                    WHERE constraint_id=%s
                """
                cursor.execute(command, (constraint_id,))
                result = cursor.fetchone()
                if result:
                    params["if_item_id"] = result["if_item_id"]
                    params["then_item_id"] = result["then_item_id"]
                    params["else_item_id"] = result["else_item_id"]
                    
        return params

    def insert(self, constraint):
        """Fügt einen neuen Constraint in die Datenbank ein"""
        with self._cursor() as cursor:
            # Basis-Constraint einfügen
            command = "INSERT INTO constraint_rule (id, style_id, constraint_type) VALUES (%s, %s, %s)"
            cursor.execute(command, (
                constraint.get_id(),
                constraint.get_style_id(),
                constraint.get_constraint_type()
            ))
            
            # Parameter einfügen
            self._insert_constraint_parameters(cursor, constraint)
            
            self._cnx.commit()
            return constraint

    def _insert_constraint_parameters(self, cursor, constraint):
        """Fügt die typspezifischen Parameter eines Constraints ein"""
        params = constraint.get_parameters()
        
        if constraint.get_constraint_type() == "binary":
            command = """
                INSERT INTO constraint_parameters 
                (constraint_id, reference_object1_id, reference_object2_id, relation_type) 
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(command, (
                constraint.get_id(),
                params.get("reference_object1_id"),
                params.get("reference_object2_id"),
                params.get("relation_type")
            ))
            
        elif constraint.get_constraint_type() == "unary":
            command = """
                INSERT INTO constraint_parameters 
                (constraint_id, reference_object_id, condition) 
                VALUES (%s, %s, %s)
            """
            cursor.execute(command, (
                constraint.get_id(),
                params.get("reference_object_id"),
                params.get("condition")
            ))
            
        # Analog für andere Constraint-Typen...

    def update(self, constraint):
        """Aktualisiert einen bestehenden Constraint"""
        with self._cursor() as cursor:
            # Basis-Constraint aktualisieren
            command = "UPDATE constraint_rule SET style_id=%s, constraint_type=%s WHERE id=%s"
            cursor.execute(command, (
                constraint.get_style_id(),
                constraint.get_constraint_type(),
                constraint.get_id()
            ))
            
            # Parameter aktualisieren
            command = "DELETE FROM constraint_parameters WHERE constraint_id=%s"
            cursor.execute(command, (constraint.get_id(),))
            self._insert_constraint_parameters(cursor, constraint)
            
            self._cnx.commit()
            return constraint

    def find_by_style(self, style_id):
        """Findet alle Constraints eines Styles"""
        with self._cursor() as cursor:
            command = "SELECT * FROM constraint_rule WHERE style_id=%s"
            cursor.execute(command, (style_id,))
            tuples = cursor.fetchall()
            return [self.tuple_to_object(tuple) for tuple in tuples]