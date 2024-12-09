from src.server.bo.BusinessObject import BusinessObject


class ClothingItem(BusinessObject):

    def __init__(self):
        super().__init__()
        self._item_id = 0
        self._clothing_type = None
        self._item_name = ""

    def get_item_id(self):
        return self._item_id

    def set_item_id(self, item_id: int):
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
            self.get_item_id(),
            self.get_clothing_type(),
            self.get_item_name(),
        )

    @staticmethod
    def from_dict(dictionary=None):

        if dictionary is None:
            dictionary = {}
        obj = ClothingItem()
        obj.set_item_id(dictionary.get("clothingitem", 0))
        obj.set_clothing_type(dictionary.get("clothingitem", None))
        obj.set_item_name(dictionary.get("clothingitem_name", ""))
        return obj
