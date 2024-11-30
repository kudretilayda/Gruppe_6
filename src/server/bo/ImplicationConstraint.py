from src.server.bo.Constraint import Constraint


class ImplicationConstraint(Constraint):    
    """Realisierung einer ImplicationConstraint.

    Eine ImplicationConstraint besitzt eine Bedingung (condition) und eine Implikation (implication),
    die jeweils durch zwei Objekte (obj1, obj2) dargestellt werden.
    """
    def __init__(self, condition=None, implication=None):
        super().__init__()    
        self._condition = condition  # Bedingung
        self._implication = implication  # Implikation

    def get_condition(self):
        """Auslesen der Bedingung (condition)."""
        return self._condition

    def set_condition(self, value):
        """Setzen der Bedingung (condition)."""
        self._condition = value

    def get_implication(self):
        """Auslesen der Implikation (implication)."""
        return self._implication

    def set_implication(self, value):
        """Setzen der Implikation (implication)."""
        self._implication = value

    def auswerten(self, obj):
        """Evaluieren der ImplicationConstraint.

        Überprüft, ob die Bedingung erfüllt ist und falls ja, ob die Implikation ebenfalls erfüllt ist.
        Gibt True zurück, wenn die Implikation eingehalten wird, andernfalls False.
        """
        if self._condition is not None:
            # Beispielhafte Evaluierungslogik:
            # Wenn die Bedingung erfüllt ist, muss die Implikation ebenfalls erfüllt sein.
            if self._condition:  # Beispiel: Wenn die Bedingung wahr ist
                return self._implication  # Die Implikation muss wahr sein
        return True

    def __str__(self):
        """Erzeugen einer einfachen textuellen Darstellung der jeweiligen Instanz."""
        return (
            f"ImplicationConstraint: "
            f"Bedingung: {self._condition}, "
            f"Implikation: {self._implication}"
        )

    @staticmethod
    def from_dict(dictionary=None):
        if dictionary is None:
            dictionary = dict()
        obj = ImplicationConstraint()
        obj.set_condition(dictionary.get("condition", None))  # Bedingung
        obj.set_implication(dictionary.get("implication", None))  # Implikation
        return obj

