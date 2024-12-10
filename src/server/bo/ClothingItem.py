from src.server.bo.BusinessObject import BusinessObject


<<<<<<< HEAD
class Kleidungsstueck(BusinessObject):

    def __init__(self):
        super().__init__()
        self.__kleidungsstueck_id = 0
        self.__kleidungstyp = None
        self.__kleidungsstueck_name = ""
        self.__kleidungsstueck_size = 0
        self.__kleidungsstueck_color = ""

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

=======
class ClothingItem(BusinessObject):

    def __init__(self):
        super().__init__()
        self._item_id = 0
        self._wardrobe_id = 0
        self._item_name = ""
        self._clothing_type = None

    def get_id(self):
        return self._item_id

    def set_id(self, item_id: int):
        self._item_id = item_id

    def get_clothing_type(self):
        return self._clothing_type

    def set_clothing_type(self, clothing_type):
        self._clothing_type = clothing_type

    def get_item_name(self):
        return self._item_name

    def set_item_name(self, item_name: str):
        self._item_name = item_name

    def __str__(self):
        return "Kleidungsstück ID: {}, Typ: {}, Name: {}".format(
            self.get_id(),
            self.get_clothing_type(),
            self.get_item_name(),
        )

    def set_wardrobe_id(self, wardrobe_id):
        self._wardrobe_id = wardrobe_id

>>>>>>> cb40ce594841218d73ecccfcb843f3b4c9718885
    @staticmethod
    def from_dict(dictionary=None):

        if dictionary is None:
            dictionary = {}
<<<<<<< HEAD
        obj = Kleidungsstueck()
        obj.set_kleidungsstueck_id(dictionary.get("kleidungsstueck_id", 0))
        obj.set_kleidungstyp(dictionary.get("kleidungstyp", None))
        obj.set_kleidungsstueck_name(dictionary.get("kleidungsstueck_name", ""))
        obj.set_kleidungsstueck_size(dictionary.get("kleidungsstueck_size", 0))
        obj.set_kleidungsstueck_color(dictionary.get("kleidungsstueck_color", ""))
=======
        obj = ClothingItem()
        obj.set_id(dictionary.get("clothingitem", 0))
        obj.set_clothing_type(dictionary.get("clothingitem", None))
        obj.set_item_name(dictionary.get("clothingitem_name", ""))
>>>>>>> cb40ce594841218d73ecccfcb843f3b4c9718885
        return obj
