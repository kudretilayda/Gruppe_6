from src.server.constraints.Constraint import Constraint


class MutexConstraint(Constraint):
    def __init__(self, object1=None, object2=None):
        super().__init__()
        self.constraint_id = 0
        self.object1 = object1
        self.object2 = object2

    def get_object1(self):
        return self.object1

    def set_object1(self, value):
        self.object1 = value

    def get_object2(self):
        return self.object2

    def set_object2(self, value):
        self.object2 = value

    def auswerten(self, obj):
        if self.object1 is not None and self.object2 is not None:
            # Beispielhafte Logik: Wenn die Attribute und Werte der beiden Objekte erfüllt sind,
            # dürfen sie nicht denselben Wert haben (Mutex-Prinzip).
            if self.object1.get_value() == self.object2.get_value():  # Beispielhafte Logik für Mutex
                return False
        return True

    def __str__(self):
        return (
            f"MutexConstraint: "
            f"Object1: ({self.object1.get_attribute()}, {self.object1.get_value()}), "
            f"Object2: ({self.object2.get_attribute()}, {self.object2.get_value()})"
        )

    @staticmethod
    def from_dict(dictionary=None):
        if dictionary is None:
            dictionary = dict()
        
        object1 = dictionary.get("object1", None)
        object2 = dictionary.get("object2", None)
        
        return MutexConstraint(object1=object1, object2=object2)
