from server.bo import BusinessObject as bo


class Style(bo.BusinessObject):
    def __init__(self):
        super().__init__()
        self.__style_id = 0
        self.__features = ""
        self.__constraints = []
        self.__kleidungstypen = []

    # Properties
    @property
    def style_id(self):
        return self.__style_id

    @style_id.setter
    def style_id(self, style_id: int):
        self.__style_id = style_id

    @property
    def features(self):
        return self.__features

    @features.setter
    def features(self, features: str):
        self.__features = features

    @property
    def constraints(self):
        return self.__constraints

    @constraints.setter
    def constraints(self, constraints: list):
        self.__constraints = constraints

    @property
    def kleidungstypen(self):
        return self.__kleidungstypen

    @kleidungstypen.setter
    def kleidungstypen(self, kleidungstypen: list):
        self.__kleidungstypen = kleidungstypen

    # String-Repräsentation
    def __str__(self):
        return f"Style: {self.style_id}, {self.features}, {self.constraints}, {self.kleidungstypen}"

    # Statische Methode zum Erstellen eines Objekts aus einem Dictionary
    @staticmethod
    def from_dict(dictionary=dict()):
        obj = Style()
        obj.style_id = dictionary.get("style_id", 0)
        obj.features = dictionary.get("features", "")
        obj.constraints = dictionary.get("constraints", [])
        obj.kleidungstypen = dictionary.get("kleidungstypen", [])
        return obj
