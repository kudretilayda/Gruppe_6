from server.bo import Constraint

class MutexConstraint(Constraint): 
    """Realisierung einer MutexConstraint.

    Eine MutexConstraint besitzt zwei Attribute (obj1_attribute, obj2_attribute),
    zwei Werte (obj1_value, obj2_value) und eine Auswertungsfunktion, die die Bedingung
    und Implikation bewertet.
    """
    def __init__(self):
        super().__init__()
        self._obj1_attribute = ""  # Das Attribut des ersten Objekts
        self._obj1_value = ""      # Der Wert des Attributs des ersten Objekts
        self._obj2_attribute = ""  # Das Attribut des zweiten Objekts
        self._obj2_value = ""      # Der Wert des Attributs des zweiten Objekts

    def get_obj1_attribute(self):
        """Auslesen des Attributs des ersten Objekts."""
        return self._obj1_attribute

    def set_obj1_attribute(self, value):
        """Setzen des Attributs des ersten Objekts."""
        self._obj1_attribute = value

    def get_obj1_value(self):
        """Auslesen des Wertes des ersten Objekts."""
        return self._obj1_value

    def set_obj1_value(self, value):
        """Setzen des Wertes des ersten Objekts."""
        self._obj1_value = value

    def get_obj2_attribute(self):
        """Auslesen des Attributs des zweiten Objekts."""
        return self._obj2_attribute

    def set_obj2_attribute(self, value):
        """Setzen des Attributs des zweiten Objekts."""
        self._obj2_attribute = value

    def get_obj2_value(self):
        """Auslesen des Wertes des zweiten Objekts."""
        return self._obj2_value

    def set_obj2_value(self, value):
        """Setzen des Wertes des zweiten Objekts."""
        self._obj2_value = value

    def auswertung(self):
        """Evaluierung der MutexConstraint.

        Überprüft, ob die angegebenen Attribute und Werte nicht gleichzeitig erfüllt sind.
        Gibt True zurück, wenn die Constraint eingehalten wird, andernfalls False.
        """
        if self._obj1_attribute and self._obj1_value and self._obj2_attribute and self._obj2_value:
            # Beispielhafte Logik, hier könnte weitere spezifische Logik hinzukommen
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