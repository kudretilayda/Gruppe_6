# src/server/bo/unary_constraint.py
from server.bo.Constraint import Constraint

from server.bo.Constraint import Constraint

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

