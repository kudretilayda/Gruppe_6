from src.server.bo.Constraint import Constraint


class MutexConstraint(Constraint):
    """Realisierung einer MutexConstraint.

    Eine MutexConstraint besitzt zwei Objekte (`object1` und `object2`), die jeweils Attribute und Werte beinhalten.
    """
    def __init__(self, object1=None, object2=None):
        super().__init__()
        self._object1 = object1  # Das erste Objekt
        self._object2 = object2  # Das zweite Objekt

    def get_object1(self):
        """Auslesen des ersten Objekts."""
        return self._object1

    def set_object1(self, value):
        """Setzen des ersten Objekts."""
        self._object1 = value

    def get_object2(self):
        """Auslesen des zweiten Objekts."""
        return self._object2

    def set_object2(self, value):
        """Setzen des zweiten Objekts."""
        self._object2 = value

    def auswerten(self, obj):
        if self._object1 is not None and self._object2 is not None:
            # Beispielhafte Logik: Wenn die Attribute und Werte der beiden Objekte erfüllt sind,
            # dürfen sie nicht denselben Wert haben (Mutex-Prinzip).
            if self._object1.get_value() == self._object2.get_value():  # Beispielhafte Logik für Mutex
                return False
        return True

    def __str__(self):
        """Erzeugen einer einfachen textuellen Darstellung der jeweiligen Instanz.

        Diese besteht aus den beiden Objekten und deren Attributen und Werten.
        """
        return (
            f"MutexConstraint: "
            f"Object1: ({self._object1.get_attribute()}, {self._object1.get_value()}), "
            f"Object2: ({self._object2.get_attribute()}, {self._object2.get_value()})"
        )

    @staticmethod
    def from_dict(dictionary=None):
        """Umwandeln eines Python dict() in eine MutexConstraint."""
        if dictionary is None:
            dictionary = dict()
        
        object1 = dictionary.get("object1", None)  # Annahme, dass object1 ein Objekt mit den Methoden get_attribute() und get_value() ist
        object2 = dictionary.get("object2", None)  # Annahme, dass object2 ein Objekt mit den Methoden get_attribute() und get_value() ist
        
        return MutexConstraint(object1=object1, object2=object2)

