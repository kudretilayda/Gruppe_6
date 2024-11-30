from src.server.bo.Constraint import Constraint


class MutexConstraint(Constraint):
    """Realisierung einer MutexConstraint.

    Eine MutexConstraint besitzt zwei Objekte (`obj1` und `obj2`), die jeweils Attribute und Werte beinhalten.
    """
    def __init__(self, obj1=None, obj2=None):
        super().__init__()
        self._obj1 = obj1  # Das erste Objekt
        self._obj2 = obj2  # Das zweite Objekt

    def get_obj1(self):
        """Auslesen des ersten Objekts."""
        return self._obj1

    def set_obj1(self, value):
        """Setzen des ersten Objekts."""
        self._obj1 = value

    def get_obj2(self):
        """Auslesen des zweiten Objekts."""
        return self._obj2

    def set_obj2(self, value):
        """Setzen des zweiten Objekts."""
        self._obj2 = value

    def auswerten(self, obj):

        if self._obj1 is not None and self._obj2 is not None:
            # Beispielhafte Logik: Wenn die Attribute und Werte der beiden Objekte erfüllt sind,
            # dürfen sie nicht denselben Wert haben (Mutex-Prinzip).
            if self._obj1.get_value() == self._obj2.get_value():  # Beispielhafte Logik für Mutex
                return False
        return True

    def __str__(self):
        """Erzeugen einer einfachen textuellen Darstellung der jeweiligen Instanz.

        Diese besteht aus den beiden Objekten und deren Attributen und Werten.
        """
        return (
            f"MutexConstraint: "
            f"Obj1: ({self._obj1.get_attribute()}, {self._obj1.get_value()}), "
            f"Obj2: ({self._obj2.get_attribute()}, {self._obj2.get_value()})"
        )

    @staticmethod
    def from_dict(dictionary=None):
        """Umwandeln eines Python dict() in eine MutexConstraint."""
        if dictionary is None:
            dictionary = dict()
        
        # Wir nehmen an, dass die Objekte aus einem Dictionary erstellt werden müssen,
        # die Attribute obj1 und obj2 müssen dabei Instanzen von anderen Klassen sein, 
        # die mit get_attribute() und get_value() arbeiten.
        obj1 = dictionary.get("obj1", None)  # Annahme, dass obj1 ein Objekt mit den Methoden get_attribute() und get_value() ist
        obj2 = dictionary.get("obj2", None)  # Annahme, dass obj2 ein Objekt mit den Methoden get_attribute() und get_value() ist
        
        return MutexConstraint(obj1=obj1, obj2=obj2)
