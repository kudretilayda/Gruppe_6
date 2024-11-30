from src.server.bo.Constraint import Constraint


class CardinalityConstraint(Constraint):
    """Realisierung einer CardinalityConstraint.

    Eine CardinalityConstraint besitzt ein Objekt (_object), 
    eine Mindestanzahl (_min_count) und eine Höchstanzahl (_max_count),
    sowie eine Auswertungsfunktion, die die Bedingung bewertet.
    """
    def __init__(self, _min_count=0, _max_count=0, _object=None):
        super().__init__()
        self._min_count = _min_count  # Minimale Kardinalität
        self._max_count = _max_count  # Maximale Kardinalität
        self._object = _object        # Das Objekt

    # Getter und Setter für _min_count
    def get_min_count(self):
        return self._min_count

    def set_min_count(self, value):
        self._min_count = value

    # Getter und Setter für _max_count
    def get_max_count(self):
        return self._max_count

    def set_max_count(self, value):
        self._max_count = value

    # Getter und Setter für _object
    def get_object(self):
        return self._object

    def set_object(self, value):
        self._object = value

    def auswerten(self, collection):
        """Evaluierung der Kardinalität innerhalb der Sammlung (collection).
        
        :param collection: Sammlung, in der die Kardinalität geprüft wird.
        :return: True, wenn die Kardinalitätsbedingung erfüllt ist, sonst False.
        """
        obj_count = collection.count(self._object)
        return self._min_count <= obj_count <= self._max_count

    def __str__(self):
        """Erzeugen einer einfachen textuellen Darstellung der jeweiligen Instanz."""
        return (
            f"CardinalityConstraint: (Min: {self._min_count}, Max: {self._max_count}, "
            f"Object: {self._object})"
        )

    @classmethod
    def from_dict(cls, dictionary=None):
        """Erstellt eine Instanz aus einem Dictionary.
        
        :param dictionary: Dictionary mit den Kardinalitätsinformationen.
        :return: Instanz der CardinalityConstraint-Klasse.
        """
        if dictionary is None:
            dictionary = {}
        return cls(
            _min_count=dictionary.get("min_count", 0),
            _max_count=dictionary.get("max_count", 0),
            _object=dictionary.get("object", None)
        )
