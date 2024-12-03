from src.server.bo.BusinessObject import BusinessObject


class Style (BusinessObject):

    def __init__(self):
        super().__init__()
        self.__style_id = 0
        self.__features = ""
        self.__constraints = []
        self.__kleidungstypen = []
    
    def get_style_id(self):
        return self.__style_id

    def set_style_id(self, style_id: int):
        self.__style_id = style_id

    def get_features(self):
        return self.__features

    def set_features(self, features: str):
        self.__features = features

    def get_constraints(self):
        return self.__constraints

    def set_constraints(self, constraints: list):
        self.__constraints = constraints

    def get_kleidungstypen(self):
        return self.__kleidungstypen

    def set_kleidungstypen(self, kleidungstypen: list):
        self.__kleidungstypen = kleidungstypen

    def __str__(self):
        
        return "Style: {}, {}, {}, {}".format(
            self.__style_id,
            self.__features,
            self.__constraints,
            self.__kleidungstypen
        )

    @staticmethod
    def from_dict(dictionary=None):
        
        if dictionary is None:
            dictionary = dict()
        obj = Style()
        obj.set_style_id(dictionary.get("style_id", 0))
        obj.set_features(dictionary.get("features", ""))
        obj.set_constraints(dictionary.get("constraints", []))
        obj.set_kleidungstypen(dictionary.get("kleidungstypen", []))
        return obj

    def set_name(self, name):
        pass
