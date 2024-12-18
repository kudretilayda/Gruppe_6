#InstanzEbene

from src.server.bo.BusinessObject import BusinessObject
from typing import List



class Outfit(BusinessObject):

    def __init__(self):
        super().__init__()
        self._style_id = None #IDdeszugehörigenStyle
        self._items = [] #ListevonClothingItems
        self._name = ""

    def get_style_id(self) -> int:
        return self._style_id

    def set_style_id(self, style_id: int):
        self._style_id = style_id

    def get_items(self) -> List['ClothingItem']:
        return self._items

    def add_item(self, item: 'ClothingItem'):
        if item not in self._items:
            self._items.append(item)

    def remove_item(self, item: 'ClothingItem'):
        if item in self._items:
            self._items.remove(item)

    def validate_integrity(self, style: 'Style') -> bool:
        """Prüft die Integrität gegen einen Style"""
        return style.validate_outfit(self)

    @staticmethod
    def from_dict(dictionary=dict()):
        obj = Outfit()
        obj.set_id(dictionary.get("id", 0))
        obj.set_style_id(dictionary.get("style_id", 0))
        obj.set_name(dictionary.get("name", ""))
        return obj