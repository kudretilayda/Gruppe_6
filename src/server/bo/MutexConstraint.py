from src.server.bo.Constraint import Constraint


class MutexConstraint(Constraint):
    def __init__(self, object1=None, object2=None):
        super().__init__()
        self._object1 = object1
        self._object2 = object2

    def get_object1(self):
        return self._object1

    def set_object1(self, value):
        self._object1 = value

    def get_object2(self):
        return self._object2

    def set_object2(self, value):
        self._object2 = value

    def auswerten(self, obj):
        if self._object1 is not None and self._object2 is not None:
            # Beispielhafte Logik: Wenn die Attribute und Werte der beiden Objekte erfüllt sind,
            # dürfen sie nicht denselben Wert haben (Mutex-Prinzip).
            if self._object1.get_value() == self._object2.get_value():  # Beispielhafte Logik für Mutex
                return False
        return True

    def __str__(self):
        return (
            f"MutexConstraint: "
            f"Object1: ({self._object1.get_attribute()}, {self._object1.get_value()}), "
            f"Object2: ({self._object2.get_attribute()}, {self._object2.get_value()})"
        )

    @staticmethod
    def from_dict(dictionary=None):
        if dictionary is None:
            dictionary = dict()
        
        object1 = dictionary.get("object1", None)
        object2 = dictionary.get("object2", None)
        
        return MutexConstraint(object1=object1, object2=object2)
