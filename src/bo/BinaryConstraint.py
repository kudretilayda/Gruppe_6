import Constraint


class BinaryConstraint(Constraint):
    def __init__(self, obj1, obj2):
        self._id = 0        # ID
        self._obj1 = obj1   # Bezugsobjekt 1
        self._obj2 = obj2   # Bezugsobjekt 2

    def get_obj1(self):
        """Auslesen des Attributs des ersten Objekts."""
        return self._obj1

    def set_obj1(self, value):
        """Setzen des Attributs des ersten Objekts."""
        self._obj1 = value

    def get_obj2(self):
        """Auslesen des Attributs des zweiten Objekts."""
        return self._obj2

    def set_obj2(self, value):
        """Setzen des Attributs des zweiten Objekts."""
        self._obj2 = value

    def auswertung(self):
        """Evaluierung der MutexConstraint.

        Überprüft, ob die angegebenen Attribute und Werte nicht gleichzeitig erfüllt sind.
        Gibt True zurück, wenn die Constraint eingehalten wird, andernfalls False.
        """
        if self._obj1 and self._obj2:
            return not (self._obj1_value == self._obj2_value)
        return True

    def __str__(self):
        """Erzeugen einer einfachen textuellen Darstellung der jeweiligen Instanz.

        Diese besteht aus der ID der Superklasse ergänzt durch die beiden Objekte
        und deren Werte.
        """
        return "MutexConstraint: {}, Obj1: ({}, {}), Obj2: ({}, {})".format(
            self.get_id(), self._obj1_attribute, self._obj1_value, self._obj2_attribute, self._obj2_value
        )

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in eine MutexConstraint."""
        obj = MutexConstraint()
        obj.set_id(dictionary["id"])  # Eigentlich Teil von BusinessObject!
        obj.set_obj1_attribute(dictionary["obj1_attribute"])
        obj.set_obj1_value(dictionary["obj1_value"])
        obj.set_obj2_attribute(dictionary["obj2_attribute"])
        obj.set_obj2_value(dictionary["obj2_value"])
        return obj