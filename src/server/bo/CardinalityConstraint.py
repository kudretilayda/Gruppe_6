from src.server.bo.Constraint import Constraint


class CardinalityConstraint(Constraint):
    """Realisierung einer CardinalityConstraint.

    Eine CardinalityConstraint besitzt zwei Attribute (obj1_attribute, obj2_attribute),
    zwei Werte (obj1_value, obj2_value), eine Mindestanzahl (_min_count) und eine Höchstanzahl (_max_count),
    sowie eine Auswertungsfunktion, die die Bedingung bewertet.
    """
    def __init__(self, _min_count=0, _max_count=0, _obj1_attribute="",
                 _obj1_value="", _obj2_attribute="", _obj2_value=""):
        super().__init__()
        self._min_count = _min_count            # Minimale Kardinalität
        self._max_count = _max_count            # Maximale Kardinalität
        self._obj1_attribute = _obj1_attribute  # Das Attribut des ersten Objekts
        self._obj1_value = _obj1_value          # Der Wert des Attributs des ersten Objekts
        self._obj2_attribute = _obj2_attribute  # Das Attribut des zweiten Objekts
        self._obj2_value = _obj2_value          # Der Wert des Attributs des zweiten Objekts

    def get_min_count(self):
        return self._min_count

    def set_min_count(self, value):
        self._min_count = value

    def get_max_count(self):
        return self._max_count

    def set_max_count(self, value):
        self._max_count = value

    def get_obj1_attribute(self):
        return self._obj1_attribute

    def set_obj1_attribute(self, value):
        self._obj1_attribute = value

    def get_obj1_value(self):
        return self._obj1_value

    def set_obj1_value(self, value):
        self._obj1_value = value

    def get_obj2_attribute(self):
        return self._obj2_attribute

    def set_obj2_attribute(self, value):
        self._obj2_attribute = value

    def get_obj2_value(self):
        return self._obj2_value

    def set_obj2_value(self, value):
        self._obj2_value = value

    def auswerten(self, collection):
        if self._min_count <= self._max_count:
            # Logik zur Evaluierung, falls spezifischere Bedingungen gelten
            return True
        return False

    def __str__(self):
        """Erzeugen einer einfachen textuellen Darstellung der jeweiligen Instanz."""
        return (
            f"CardinalityConstraint: (Min: {self._min_count}, Max: {self._max_count},  "
            f"Obj1: ({self._obj1_attribute}, {self._obj1_value}), "
            f"Obj2: ({self._obj2_attribute}, {self._obj2_value}))"
        )

    @classmethod
    def from_dict(cls, dictionary=None):
        if dictionary is None:
            dictionary = {}
        return cls(
            _min_count=dictionary.get("min_count", 0),
            _max_count=dictionary.get("max_count", 0),
            _obj1_attribute=dictionary.get("obj1_attribute", ""),
            _obj1_value=dictionary.get("obj1_value", ""),
            _obj2_attribute=dictionary.get("obj2_attribute", ""),
            _obj2_value=dictionary.get("obj2_value", "")
        )
