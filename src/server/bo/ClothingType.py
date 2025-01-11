from src.server.bo.BusinessObject import BusinessObject

# Die Klasse ClothingType erbt von der Basisklasse BusinessObject und repräsentiert einen Kleidungstyp.
class ClothingType(BusinessObject):
    def __init__(self):
        super().__init__()
        self._name = ""
        self._usage = ""

    # Getter-Methode für die ID des Kleidungstyps
    def get_id(self):
        return self._id

    # Setter-Methode für die ID des Kleidungstyps
    def set_id(self, value):
        self._id = value

    # Getter-Methode für den Namen des Kleidungstyps
    def get_name(self):
        return self._name

    # Setter-Methode für den Namen des Kleidungstyps
    def set_name(self, value):
        self._name = value

    # Getter-Methode für den Verwendungszweck des Kleidungstyps
    def get_usage(self):
        return self._usage

    # Setter-Methode für den Verwendungszweck des Kleidungstyps
    def set_usage(self, value):
        self._usage = value

    # Überschreibt die Standard-String-Repräsentation des Objekts für Debugging und Logging
    def __str__(self):
        return "Kleidungstyp: {}, Name: {}, Verwendung: {}".format(
            self.get_id(), self._name, self._usage
        )
    # Statische Methode, die ein ClothingType-Objekt aus einem Dictionary erstellt

    @staticmethod
    def from_dict(dictionary=None):
        if dictionary is None:
            dictionary = {}
        obj = ClothingType()
        # Extrahiert Daten aus dem Dictionary und initialisiert die Attribute
        obj.set_id(dictionary.get("clothing_type_id", 0))
        obj.set_name(dictionary.get("clothing_type_name", ""))
        obj.set_usage(dictionary.get("clothing_type_usage", 0))
        return obj