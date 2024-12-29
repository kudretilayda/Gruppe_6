from src.server.bo.BusinessObject import BusinessObject


class Style (BusinessObject):

    def __init__(self):
        super().__init__()
        self._style_id = int
        self._style_features = ""
        self.style_constraints = []
        self.clothing_type = []
    
    def get_style_id(self):
        return self._style_id

    def set_style_id(self, style_id: int):
        self._style_id = style_id

    def get_style_features(self):
        return self._style_features

    def set_style_features(self, features: str):
        self._style_features = features

    def get_style_constraints(self):
        return self.style_constraints

    def set_style_constraints(self, constraint):
        self.style_constraints.append(constraint)

    def get_clothing_type(self):
        return self.clothing_type

    def set_clothing_type(self, clothing_type):
        self.clothing_type.append(clothing_type)

    def __str__(self):
        return "Style: {}, {}, {}, {}".format(self._style_id,
                                              self._style_features,
                                              self.style_constraints,
                                              self.clothing_type)

    def validate(self):
        for constraint in self.style_constraints:
            if constraint.validate():
                return True
            else:
                return False


    @staticmethod
    def from_dict(dictionary=None):
        
        if dictionary is None:
            dictionary = dict()
        obj = Style()
        obj.set_style_id(dictionary.get("style_id", 0))
        obj.set_style_features(dictionary.get("style_features", ""))
        obj.set_style_constraints(dictionary.get("style_constraints", []))
        obj.set_clothing_type(dictionary.get("clothing_type", []))
        return obj
