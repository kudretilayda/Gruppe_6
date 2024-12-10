from src.server.bo.BusinessObject import BusinessObject


class Style (BusinessObject):

    def __init__(self):
        super().__init__()
        self.__style_id = 0
        self.__style_features = ""
        self.__style_constraints = []
        self.__clothing_type = []
    
    def get_style_id(self):
        return self.__style_id

    def set_style_id(self, style_id: int):
        self.__style_id = style_id

    def get_style_features(self):
        return self.__style_features

    def set_style_features(self, features: str):
        self.__style_features = features

    def get_style_constraints(self):
        return self.__style_constraints

    def set_style_constraints(self, constraints: list):
        self.__style_constraints = constraints

    def get_clothing_type(self):
        return self.__clothing_type

    def set_clothing_type(self, clothing_type: list):
        self.__clothing_type  = clothing_type

    def __str__(self):
        
        return "Style: {}, {}, {}, {}".format(
            self.__style_id,
            self.__style_features,
            self.__style_constraints,
            self.__clothing_type
        )

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

    def set_name(self, name):
        pass
