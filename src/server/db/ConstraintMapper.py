# src/server/bo/constraint_rule.py

from server.bo import BusinessObject

class Constraint(BusinessObject):
    """Basisklasse für alle Constraint-Regeln."""

    def __init__(self):
        super().__init__()
        self._style_id = None
        self._constraint_type = None  # Enum: 'binary', 'unary', 'implikation', 'mutex', 'kardinalitaet'

    def get_style_id(self):
        """Auslesen der Style ID."""
        return self._style_id

    def set_style_id(self, value):
        """Setzen der Style ID."""
        self._style_id = value

    def get_constraint_type(self):
        """Auslesen des Constraint-Typs."""
        return self._constraint_type

    def set_constraint_type(self, value):
        """Setzen des Constraint-Typs."""
        self._constraint_type = value

    def to_dict(self):
        """Umwandeln des Constraint-Objekts in ein Python dict()."""
        result = super().to_dict()
        result.update({
            'style_id': self.get_style_id(),
            'constraint_type': self.get_constraint_type()
        })
        return result

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in ein Constraint-Objekt."""
        obj = Constraint()
        obj.set_id(dictionary.get('id'))
        obj.set_style_id(dictionary.get('style_id'))
        obj.set_constraint_type(dictionary.get('constraint_type'))
        return obj
