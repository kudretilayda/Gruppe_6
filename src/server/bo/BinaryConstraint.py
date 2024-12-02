# src/server/bo/binary_constraint.py

class BinaryConstraint(Constraint):
    """Klasse für binäre Constraints (Beziehungen zwischen zwei Kleidungsstücken)."""

    def __init__(self):
        super().__init__()
        self._reference_object1_id = None  # ID des ersten Kleidungstyps
        self._reference_object2_id = None  # ID des zweiten Kleidungstyps
        self.set_constraint_type('binary')

    def get_reference_object1_id(self):
        """Auslesen der ID des ersten Referenzobjekts."""
        return self._reference_object1_id

    def set_reference_object1_id(self, value):
        """Setzen der ID des ersten Referenzobjekts."""
        self._reference_object1_id = value

    def get_reference_object2_id(self):
        """Auslesen der ID des zweiten Referenzobjekts."""
        return self._reference_object2_id

    def set_reference_object2_id(self, value):
        """Setzen der ID des zweiten Referenzobjekts."""
        self._reference_object2_id = value

    def to_dict(self):
        """Umwandeln des BinaryConstraint-Objekts in ein Python dict()."""
        result = super().to_dict()
        result.update({
            'reference_object1_id': self.get_reference_object1_id(),
            'reference_object2_id': self.get_reference_object2_id()
        })
        return result

