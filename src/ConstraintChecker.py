# constraint_checker.py
class ConstraintChecker:
    def __init__(self, db):
        self.db = db

    def check_binary_constraint(self, constraint, outfit_items):
        """Prüft Binary Constraints (z.B. Artikel A nicht mit Artikel B)"""
        query = """
            SELECT * FROM binary_constraint
            WHERE style_constraint_id = %s
        """
        result = self.db.query(query, (constraint['id'],))
        binary_constraint = result.fetchone()
        
        if not binary_constraint:
            return True
            
        # Prüfe ob beide Objekte im Outfit vorhanden sind
        has_object1 = any(item['id'] == binary_constraint['object1_id'] for item in outfit_items)
        has_object2 = any(item['id'] == binary_constraint['object2_id'] for item in outfit_items)
        
        # Bei Mutex dürfen nicht beide vorhanden sein
        if constraint['constraint_type_id'] == 'mutex':
            return not (has_object1 and has_object2)
            
        # Bei Implikation muss object2 vorhanden sein wenn object1 vorhanden ist
        if constraint['constraint_type_id'] == 'implication':
            return not has_object1 or (has_object1 and has_object2)
            
        return True

    def check_unary_constraint(self, constraint, outfit_items):
        """Prüft Unary Constraints (Bedingungen für einzelne Artikel)"""
        query = """
            SELECT * FROM unary_constraint
            WHERE style_constraint_id = %s
        """
        result = self.db.query(query, (constraint['id'],))
        unary_constraint = result.fetchone()
        
        if not unary_constraint:
            return True
            
        # Prüfe ob das betroffene Objekt im Outfit vorhanden ist
        has_object = any(item['id'] == unary_constraint['object_id'] for item in outfit_items)
        
        return has_object

    def check_cardinality_constraint(self, constraint, outfit_items):
        """Prüft Kardinalitäts-Constraints (Anzahl bestimmter Artikeltypen)"""
        query = """
            SELECT * FROM cardinality_constraint
            WHERE style_constraint_id = %s
        """
        result = self.db.query(query, (constraint['id'],))
        cardinality_constraint = result.fetchone()
        
        if not cardinality_constraint:
            return True
            
        # Zähle Artikel des spezifizierten Typs
        count = sum(1 for item in outfit_items if item['type_id'] == cardinality_constraint['type_id'])
        
        # Prüfe ob Anzahl innerhalb der erlaubten Grenzen liegt
        min_count = cardinality_constraint['min_count'] or 0
        max_count = cardinality_constraint['max_count'] or float('inf')
        
        return min_count <= count <= max_count

    def check_all_constraints(self, style_id, outfit_items):
        """Prüft alle Constraints eines Styles für ein Outfit"""
        # Hole alle Constraints für den Style
        query = """
            SELECT * FROM style_constraint
            WHERE style_id = %s
        """
        result = self.db.query(query, (style_id,))
        constraints = result.fetchall()
        
        for constraint in constraints:
            # Prüfe je nach Constraint-Typ
            if not self.check_binary_constraint(constraint, outfit_items):
                return False, f"Binary constraint {constraint['id']} violated"
                
            if not self.check_unary_constraint(constraint, outfit_items):
                return False, f"Unary constraint {constraint['id']} violated"
                
            if not self.check_cardinality_constraint(constraint, outfit_items):
                return False, f"Cardinality constraint {constraint['id']} violated"
                
        return True, "All constraints satisfied"
    

#Diese Implementierung bietet:
#ConstraintMapper für die Datenbankoperationen:
#CRUD-Operationen für Constraints
#Spezielle Methoden zum Abrufen von Constraints nach Style
#ConstraintHelper für die Geschäftslogik:
#Erstellung verschiedener Constraint-Typen
#Validierung von Outfits gegen Constraints
#Überprüfung spezifischer Constraint-Typen
#Vorschläge zur Behebung von Constraint-Verletzungen
#Die Constraints können verschiedene Regeln abbilden:
#Binäre Constraints (z.B. "Hemd muss zur Hose passen")
#Kardinalitäts-Constraints (z.B. "Maximal 1 Jacke")
#Farbconstraints (z.B. "Erlaubte Farbkombinationen")