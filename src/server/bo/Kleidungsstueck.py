from src.server.bo.BusinessObject import BusinessObject


class Kleidungsstueck(BusinessObject):

    def __init__(self):
        super().__init__()
        self.__kleidungsstueck_id = 0
        self.__kleidungstyp = None
        self.__kleidungsstueck_name = ""
        self.__kleidungsstueck_usage = ""
        self.__kleidungsstueck_size = 0
        self.__kleidungsstueck_color = ""   # vllt Features wie size und color in constraints reinmachen

    def get_kleidungsstueck_id(self):
        return self.__kleidungsstueck_id

    def set_kleidungsstueck_id(self, kleidungsstueck_id: int):
        self.__kleidungsstueck_id = kleidungsstueck_id

    # Getter und Setter für kleidungstyp
    def get_kleidungstyp(self):
        return self.__kleidungstyp

    def set_kleidungstyp(self, kleidungstyp):
        self.__kleidungstyp = kleidungstyp

    # Getter und Setter für kleidungsstueck_name
    def get_kleidungsstueck_name(self):
        return self.__kleidungsstueck_name

    def set_kleidungsstueck_name(self, kleidungsstueck_name: str):
        self.__kleidungsstueck_name = kleidungsstueck_name

    def get_kleidungsstueck_size(self):
        return self.__kleidungsstueck_size

    def set_kleidungsstueck_size(self, kleidungsstueck_size: int):
        self.__kleidungsstueck_size = kleidungsstueck_size

    # Getter und Setter für kleidungsstueck_color
    def get_kleidungsstueck_color(self):
        return self.__kleidungsstueck_color

    def set_kleidungsstueck_color(self, kleidungsstueck_color: str):
        self.__kleidungsstueck_color = kleidungsstueck_color

    def __str__(self):
        return "Kleidungsstück ID: {}, Typ: {}, Name: {}, Größe: {}, Farbe: {}".format(
            self.get_kleidungsstueck_id(),
            self.get_kleidungstyp(),
            self.get_kleidungsstueck_name(),
            self.get_kleidungsstueck_size(),
            self.get_kleidungsstueck_color()
        )

    @staticmethod
    def from_dict(dictionary=None):

        if dictionary is None:
            dictionary = {}
        obj = Kleidungsstueck()
        obj.set_kleidungsstueck_id(dictionary.get("kleidungsstueck_id", 0))
        obj.set_kleidungstyp(dictionary.get("kleidungstyp", None))
        obj.set_kleidungsstueck_name(dictionary.get("kleidungsstueck_name", ""))
        obj.set_kleidungsstueck_size(dictionary.get("kleidungsstueck_size", 0))
        obj.set_kleidungsstueck_color(dictionary.get("kleidungsstueck_color", ""))
        return obj