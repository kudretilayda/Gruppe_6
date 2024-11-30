from server.bo.BusinessObject import BusinessObject

class Outfit(BusinessObject):
    """Realisierung eines Outfits"""
    
    def __init__(self):
        super().__init__()
        self._style_id = 0
        self._name = ""
        self._items = []  # Liste von ClothingItem IDs

    def get_style_id(self):
        return self._style_id

    def set_style_id(self, value):
        self._style_id = value

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def get_items(self):
        return self._items

    def set_items(self, items):
        self._items = items

    def add_item(self, item_id):
        if item_id not in self._items:
            self._items.append(item_id)

    def remove_item(self, item_id):
        if item_id in self._items:
            self._items.remove(item_id)

    @staticmethod
    def from_dict(dictionary=dict()):
        obj = Outfit()
        obj.set_id(dictionary.get("id"))
        obj.set_style_id(dictionary.get("style_id"))
        obj.set_name(dictionary.get("name"))
        obj.set_items(dictionary.get("items", []))
        return obj