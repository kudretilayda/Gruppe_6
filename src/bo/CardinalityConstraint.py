import BusinessObject


class CardinalityConstraint(BusinessObject):
    """Realisierung einer CardinalityConstraint.

    Eine CardinalityConstraint besitzt zwei Attribute (obj1_attribute, obj2_attribute),
    zwei Werte (obj1_value, obj2_value), eine Mindestanzahl (_min_count) und eine Höchstanzahl (_max_count),
    sowie eine Auswertungsfunktion, die die Bedingung bewertet.
    """
    def __init__(self, _min_count=0, _max_count=0, _obj1_attribute="",
                 _obj1_value="", _obj2_attribute="", _obj2_value=""):
        super().__init__()
        self._min_count = _min_count      # Minimale Kardinalität
        self._max_count = _max_count      # Maximale Kardinalität
        self._obj1_attribute = _obj1_attribute  # Das Attribut des ersten Objekts
        self._obj1_value = _obj1_value      # Der Wert des Attributs des ersten Objekts
        self._obj2_attribute = _obj2_attribute  # Das Attribut des zweiten Objekts
        self._obj2_value = _obj2_value      # Der Wert des Attributs des zweiten Objekts

    def get_min_count(self):
        """Auslesen der minimalen Kardinalität."""
        return self._min_count

    def set_min_count(self, value):
        """Setzen der minimalen Kardinalität."""
        self._min_count = value

    def get_max_count(self):
        """Auslesen der maximalen Kardinalität."""
        return self._max_count

    def set_max_count(self, value):
        """Setzen der maximalen Kardinalität."""
        self._max_count = value

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
        """Evaluierung der CardinalityConstraint.

        Überprüft, ob die Constraint eingehalten wird.
        Beispielhafte Logik: Überprüft, ob die Werte innerhalb der Kardinalitätsgrenzen liegen.
        """
        if self._min_count <= self._max_count:
            # Logik zur Evaluierung, falls spezifischere Bedingungen gelten
            return True
        return False

    def __str__(self):
        """Erzeugen einer einfachen textuellen Darstellung der jeweiligen Instanz.

        Diese besteht aus der ID der Superklasse ergänzt durch die Kardinalitätsgrenzen
        und die beiden Objekte mit deren Attributen und Werten.
        """
        return (
            f"CardinalityConstraint: {self.get_id()}, "
            f"Min: {self._min_count}, Max: {self._max_count}, "
            f"Obj1: ({self._obj1_attribute}, {self._obj1_value}), "
            f"Obj2: ({self._obj2_attribute}, {self._obj2_value})"
        )

    @staticmethod
    def from_dict(dictionary=None):
        """Umwandeln eines Python dict() in eine CardinalityConstraint."""
        if dictionary is None:
            dictionary = dict()
        obj = CardinalityConstraint(
            _min_count=dictionary.get("min_count", 0),
            _max_count=dictionary.get("max_count", 0),
            _obj1_attribute=dictionary.get("obj1_attribute", ""),
            _obj1_value=dictionary.get("obj1_value", ""),
            _obj2_attribute=dictionary.get("obj2_attribute", ""),
            _obj2_value=dictionary.get("obj2_value", "")
        )
        obj.set_id(dictionary["id"])  # Eigentlicher Teil von BusinessObject!
        return obj
