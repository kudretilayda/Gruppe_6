from server.bo import Constraint 


class ImplicationConstraint(Constraint): 
    """Realisierung einer ImplicationConstraint.

    Eine ImplicationConstraint besitzt eine Bedingung (condition_attribute, condition_value) 
    und eine Implikation (implication_attribute, implication_value).
    """
    def __init__(self):
        super().__init__()    
        self._condition_attribute = ""  # Das Attribut der Bedingung
        self._condition_value = ""      # Der Wert der Bedingung
        self._implication_attribute = ""  # Das Attribut der Implikation
        self._implication_value = ""      # Der Wert der Implikation                       

    def get_condition_attribute(self):
        """Auslesen des Attributs der Bedingung."""
        return self._condition_attribute

    def set_condition_attribute(self, value):
        """Setzen des Attributs der Bedingung."""
        self._condition_attribute = value

    def get_condition_value(self):
        """Auslesen des Wertes der Bedingung."""
        return self._condition_value

    def set_condition_value(self, value):
        """Setzen des Wertes der Bedingung."""
        self._condition_value = value

    def get_implication_attribute(self):
        """Auslesen des Attributs der Implikation."""
        return self._implication_attribute

    def set_implication_attribute(self, value):
        """Setzen des Attributs der Implikation."""
        self._implication_attribute = value 
    
    def get_implication_value(self):
        """Auslesen des Wertes der Implikation."""
        return self._implication_value    

    def set_implication_value(self, value):
        """Setzen des Wertes der Implikation."""
        self._implication_value = value

    def auswertung(self):
        """Evaluieren der ImplicationConstraint.

        Überprüft, ob die Bedingung erfüllt ist und falls ja, ob die Implikation ebenfalls erfüllt ist.
        Gibt True zurück, wenn die Implikation eingehalten wird, andernfalls False.
        """
        if self._condition_attribute and self._condition_value:
            # Beispielhafte Evaluierungslogik:
            # Wenn die Bedingung gilt, muss die Implikation ebenfalls gelten.
            if self._condition_value:  # Beispiel: Wenn die Bedingung wahr ist
                return self._implication_value  # Die Implikation muss wahr sein
        return True

    def __str__(self):
        """Erzeugen einer einfachen textuellen Darstellung der jeweiligen Instanz.
        
        Diese besteht aus der ID der Superklasse ergänzt durch die Bedingung 
        (Attribut und Wert) und die Implikation (Attribut und Wert).
        """
        return (
            f"ImplicationConstraint: {self.get_id()}, "
            f"Bedingung: ({self._condition_attribute}, {self._condition_value}), "
            f"Implikation: ({self._implication_attribute}, {self._implication_value})"
        )

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in eine ImplicationConstraint."""
        obj = ImplicationConstraint()
        obj.set_id(dictionary["id"])  # Eigentlich Teil von BusinessObject!
        obj.set_condition_attribute(dictionary.get("condition_attribute", ""))
        obj.set_condition_value(dictionary.get("condition_value", ""))
        obj.set_implication_attribute(dictionary.get("implication_attribute", ""))
        obj.set_implication_value(dictionary.get("implication_value", ""))
        return obj
