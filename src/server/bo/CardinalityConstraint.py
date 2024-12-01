from src.server.bo.Constraint import Constraint


class CardinalityConstraint(Constraint):
    def __init__(self, _min_count=0, _max_count=0, _object=None):
        super().__init__()
        self._min_count = _min_count
        self._max_count = _max_count
        self._object = _object

    def get_min_count(self):
        return self._min_count

    def set_min_count(self, value):
        self._min_count = value

    def get_max_count(self):
        return self._max_count

    def set_max_count(self, value):
        self._max_count = value

    def get_object(self):
        return self._object

    def set_object(self, value):
        self._object = value

    def auswerten(self, collection):
        obj_count = collection.count(self._object)
        return self._min_count <= obj_count <= self._max_count

    def __str__(self):
        return (
            f"CardinalityConstraint: (Min: {self._min_count}, Max: {self._max_count}, "
            f"Object: {self._object})"
        )

    @classmethod
    def from_dict(cls, dictionary=None):
        if dictionary is None:
            dictionary = {}
        return cls(
            _min_count=dictionary.get("min_count", 0),
            _max_count=dictionary.get("max_count", 0),
            _object=dictionary.get("object", None)
        )
