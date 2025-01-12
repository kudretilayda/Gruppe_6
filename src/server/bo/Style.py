from src.server.bo.BusinessObject import BusinessObject

# Die Klasse Style erbt von der Basisklasse BusinessObject und repräsentiert einen Stil.
class Style(BusinessObject):

    def __init__(self):
        super().__init__()
#        self._style_id = int
        self._style_features = ""
        self.style_constraints = []
        self.clothing_type = []

    # Getter-Methode für die ID des Styles
#    def get_style_id(self):
#        return self._style_id

    # Setter-Methode für die ID des Styles
#    def set_style_id(self, style_id: int):
#        self._style_id = style_id

    # Getter-Methode für die Features des Styles
    def get_style_features(self):
        return self._style_features

    # Setter-Methode für die Features des Styles
    def set_style_features(self, features: str):
        self._style_features = features

    # Getter-Methode für die Constraints des Styles
    def get_style_constraints(self):
        return self.style_constraints

    # Setter-Methode für die Constraints des Styles
    def set_style_constraints(self, constraint):
        self.style_constraints.append(constraint)

    # Getter-Methode für die Kleidungstypen, die zum Style gehören
    def get_clothing_type(self):
        return self.clothing_type

    # Setter-Methode für die Kleidungstypen, die zum Style gehören
    def set_clothing_type(self, clothing_type):
        self.clothing_type.append(clothing_type)


    def __str__(self):
        return "Style: {}, {}, {}, {}".format(self._id,
                                              self._style_features,
                                              self.style_constraints,
                                              self.clothing_type)

    # Methode zur Validierung des Styles anhand seiner Constraints

    def validate(self):
        for constraint in self.style_constraints:
            if constraint.validate():
                return True
            else:
                return False

    # Statische Methode, die ein Style-Objekt aus einem Dictionary erstellt

    @staticmethod
    def from_dict(dictionary=None):

        if dictionary is None:
            dictionary = dict() # Leeres Dictionary falls None übergeben wird
        obj = Style()
        # Extrahiert Daten aus dem Dictionary und initialisiert die Attribute
        obj.set_id(dictionary.get("style_id", 0))
        obj.set_style_features(dictionary.get("style_features", ""))
        obj.set_style_constraints(dictionary.get("style_constraints", []))
        obj.set_clothing_type(dictionary.get("clothing_type", []))
        return obj