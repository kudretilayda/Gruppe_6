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