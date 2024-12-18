from src.server.db.Mapper import Mapper


class ConstraintMapper(Mapper):
    def __init__(self):
        super().__init__()

    def insert(self, constraint):
        """Fügt einen neuen Constraint in die DB ein"""
        cursor = self._cnx.cursor()

        # Basis-Constraint Daten
        command = "INSERT INTO constraint (style_id) VALUES (%s)"
        data = (constraint.get_style_id(),)
        cursor.execute(command, data)
        constraint.set_id(cursor.lastrowid)

        # Spezifische Constraint-Daten basierend auf Typ
        if isinstance(constraint, BinaryConstraint):
            command = """INSERT INTO binary_constraint 
                        (constraint_id, reference_type1_id, reference_type2_id) 
                        VALUES (%s, %s, %s)"""
            data = (constraint.get_id(),
                    constraint.get_reference_type1_id(),
                    constraint.get_reference_type2_id())
            cursor.execute(command, data)

            if isinstance(constraint, Mutex):
                command = "INSERT INTO mutex (binary_constraint_id) VALUES (%s)"
                cursor.execute(command, (constraint.get_id(),))
            elif isinstance(constraint, Implication):
                command = "INSERT INTO implication (binary_constraint_id) VALUES (%s)"
                cursor.execute(command, (constraint.get_id(),))

        elif isinstance(constraint, Cardinality):
            command = """INSERT INTO cardinality 
                        (constraint_id, reference_type_id, min_count, max_count) 
                        VALUES (%s, %s, %s, %s)"""
            data = (constraint.get_id(),
                    constraint.get_reference_type_id(),
                    constraint.get_min_count(),
                    constraint.get_max_count())
            cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()
        return constraint

    def find_by_id(self, id):
        """Findet einen Constraint anhand seiner ID"""
        cursor = self._cnx.cursor()

        # Basis-Constraint-Daten laden
        command = "SELECT * FROM constraint WHERE id=%s"
        cursor.execute(command, (id,))
        constraint_data = cursor.fetchone()

        if not constraint_data:
            return None

        