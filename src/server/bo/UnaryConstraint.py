# src/server/bo/unary_constraint.py

class UnaryConstraint(Constraint):
    """Klasse für unäre Constraints (Bedingungen für einzelne Kleidungsstücke)."""

    def __init__(self):
        super().__init__()
        self._reference_object_id = None  # ID des Kleidungstyps
        self.set_constraint_type('unary')

    def get_reference_object_id(self):
        """Auslesen der ID des Referenzobjekts."""
        return self._reference_object_id

    def set_reference_object_id(self, value):
        """Setzen der ID des Referenzobjekts."""
        self._reference_object_id = value

    def to_dict(self):
        """Umwandeln des UnaryConstraint-Objekts in ein Python dict()."""
        result = super().to_dict()
        result.update({
            'reference_object_id': self.get_reference_object_id()
        })
        return result


# src/server/bo/mutex_constraint.py

class MutexConstraint(BinaryConstraint):
    """Klasse für Mutex-Constraints (wechselseitiger Ausschluss)."""

    def __init__(self):
        super().__init__()
        self.set_constraint_type('mutex')


# src/server/bo/implication_constraint.py

class ImplicationConstraint(BinaryConstraint):
    """Klasse für Implikations-Constraints (Wenn-Dann-Beziehungen)."""

    def __init__(self):
        super().__init__()
        self.set_constraint_type('implikation')


# src/server/bo/cardinality_constraint.py

class CardinalityConstraint(UnaryConstraint):
    """Klasse für Kardinalitäts-Constraints (Mengenbeschränkungen)."""

    def __init__(self):
        super().__init__()
        self._min_value = 0
        self._max_value = None
        self.set_constraint_type('kardinalitaet')

    def get_min_value(self):
        """Auslesen des Minimalwerts."""
        return self._min_value

    def set_min_value(self, value):
        """Setzen des Minimalwerts."""
        self._min_value = value

    def get_max_value(self):
        """Auslesen des Maximalwerts."""
        return self._max_value

    def set_max_value(self, value):
        """Setzen des Maximalwerts."""
        self._max_value = value

    def to_dict(self):
        """Umwandeln des CardinalityConstraint-Objekts in ein Python dict()."""
        result = super().to_dict()
        result.update({
            'min_value': self.get_min_value(),
            'max_value': self.get_max_value()
        })
        return result