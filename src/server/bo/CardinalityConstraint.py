from src.server.bo.Constraint import Constraint


class CardinalityConstraint(Constraint):
    def __init__(self, _min_count=0, _max_count=0, _object=None):
        super().__init__()
        self.constraint_id = 0
        self.min_count = _min_count
        self.max_count = _max_count
        self.object = _object

    def get_min_count(self):
        return self.min_count

    def set_min_count(self, value):
        self.min_count = value

    def get_max_count(self):
        return self.max_count

    def set_max_count(self, value):
        self.max_count = value

    def get_object(self):
        return self.object

    def set_object(self, value):
        self.object = value

    def auswerten(self, collection):
        obj_count = collection.count(self.object)
        return self.min_count <= obj_count <= self.max_count

    def __str__(self):
        return (
            f"CardinalityConstraint: (Min: {self.min_count}, Max: {self.max_count}, "
            f"Object: {self.object})"
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
