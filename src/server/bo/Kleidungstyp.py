from src.server.bo.BusinessObject import BusinessObject


class Kleidungstyp(BusinessObject):
    def __init__(self):
        super().__init__()
        self._id = int  # ID des Styles
        self._name = ""  # Der Name des Kleidungstyps
        self._verwendung = ""  # Die Anlässe wofür der Kleidungstyp ist

    def get_name(self):
        return self._name  # Auslesen des Namens

    def set_name(self, value):
        self._name = value  # Setzen des Namens

    def get_verwendung(self):
        """."""
        return self._verwendung  # Auslesen der Verwendung

    def set_verwendung(self, value):
        self._verwendung = value  # Setzen der Beschreibung

    def __str__(self):
        """Erzeugen einer einfachen textuellen Darstellung der jeweiligen Instanz.

        Diese besteht aus der ID der Superklasse ergänzt durch den Namen und die Beschreibung
        des jeweiligen Kleidungsstücks.
        """
        return "Kleidungsstück: {}, Name: {}, Beschreibung: {}".format(
            self.get_id(), self._name, self._verwendung
        )
