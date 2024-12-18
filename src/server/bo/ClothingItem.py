#InstanzEbene

from src.server.bo.BusinessObject import BusinessObject


class ClothingItem(BusinessObject):

    def __init__(self):
        super().__init__()
        self._type_id = None # ID des zugehörigen ClothingType
        self._wardrobe_id = 0
        self._name = ""

    def get_type_id(self):
        return self._type_id

    def set_type_id(self, item_id: int):
        self._type_id = item_id

    def get_name(self):
        return self._name

    def set_item_name(self, item_name: str):
        self._name = item_name



    @staticmethod
    def from_dict(dictionary=dict()):

        obj = ClothingItem()
        obj.set_id(dictionary.get("id", 0))
        obj.set_type.get(dictionary("type_id", 0))
        obj.set_name.get(dictionary("name", ""))
        return obj
