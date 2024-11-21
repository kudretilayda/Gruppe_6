import Constraint


class Kleidungsstueck(Constraint):
    """Realisierung einer exemplarischen Kleidungsstückklasse.

    Ein Kleidungsstück besitzt einen Namen und eine Beschreibung.
    """

    def __init__(self):
        super().__init__()
        self._name = ""  # Der Name des Kleidungsstücks.
        self._beschreibung = ""  # Die Beschreibung des Kleidungsstücks.

    def get_name(self):
        """Auslesen des Namens."""
        return self._name

    def set_name(self, value):
        """Setzen des Namens."""
        self._name = value

    def get_beschreibung(self):
        """Auslesen der Beschreibung."""
        return self._beschreibung

    def set_beschreibung(self, value):
        """Setzen der Beschreibung."""
        self._beschreibung = value

    def auswertung(self, obj) -> bool:
        """Evaluierung der Constraint.

        Diese Methode muss in den Unterklassen implementiert werden.
        """
        raise NotImplementedError("Die Methode 'auswertung' muss in der Unterklasse implementiert werden.")

    def __str__(self):
        """Erzeugen einer einfachen textuellen Darstellung der jeweiligen Instanz.
        
        Diese besteht aus der ID der Superklasse ergänzt durch den Namen und die Beschreibung 
        des jeweiligen Kleidungsstücks.
        """
        return "Kleidungsstück: {}, Name: {}, Beschreibung: {}".format(
            self.get_id(), self._name, self._beschreibung
        )

    @staticmethod
    def from_dict(dictionary=None):
        """Umwandeln eines Python dict() in ein Kleidungsstück."""
        if dictionary is None:
            dictionary = dict()
        obj = Kleidungsstueck()
        obj.set_id(dictionary["id"])  # Eigentlicher Teil von BusinessObject!
        obj.set_name(dictionary.get("name", ""))
        obj.set_beschreibung(dictionary.get("beschreibung", ""))
        return obj
