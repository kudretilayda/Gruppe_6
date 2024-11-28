from src.server.bo.Constraint import Constraint


class CardinalityConstraint(Constraint):
    """Realisierung einer CardinalityConstraint.

    Eine CardinalityConstraint besitzt zwei Objekte (obj1, obj2), 
    eine Mindestanzahl (_min_count) und eine Höchstanzahl (_max_count),
    sowie eine Auswertungsfunktion, die die Bedingung bewertet.
    """
    def __init__(self, _min_count=0, _max_count=0, _obj1=None, _obj2=None):
        super().__init__()
        self._min_count = _min_count  # Minimale Kardinalität
        self._max_count = _max_count  # Maximale Kardinalität
        self._obj1 = _obj1            # Erstes Objekt
        self._obj2 = _obj2            # Zweites Objekt

    def get_min_count(self):
        return self._min_count

    def set_min_count(self, value):
        self._min_count = value

    def get_max_count(self):
        return self._max_count

    def set_max_count(self, value):
        self._max_count = value

    def get_obj1(self):
        return self._obj1

    def set_obj1(self, value):
        self._obj1 = value

    def get_obj2(self):
        return self._obj2

    def set_obj2(self, value):
        self._obj2 = value

    def auswerten(self, collection):
        if self._min_count <= self._max_count:
            # Logik zur Evaluierung, falls spezifischere Bedingungen gelten
            return True
        return False

    def __str__(self):
        """Erzeugen einer einfachen textuellen Darstellung der jeweiligen Instanz."""
        return (
            f"CardinalityConstraint: (Min: {self._min_count}, Max: {self._max_count}, "
            f"Obj1: {self._obj1}, Obj2: {self._obj2})"
        )

    @classmethod
    def from_dict(cls, dictionary=None):
        if dictionary is None:
            dictionary = {}
        return cls(
            _min_count=dictionary.get("min_count", 0),
            _max_count=dictionary.get("max_count", 0),
            _obj1=dictionary.get("obj1", None),
            _obj2=dictionary.get("obj2", None)
        )

