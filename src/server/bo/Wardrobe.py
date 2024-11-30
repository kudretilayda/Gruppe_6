from server.bo.BusinessObject import BusinessObject

class Wardrobe(BusinessObject):
    """Realisierung eines Kleiderschranks"""
    
    def __init__(self):
        super().__init__()
        self._owner_id = 0
        self._items = []  # Liste von ClothingItem IDs

    def get_owner_id(self):
        return self._owner_id

    def set_owner_id(self, value):
        self._owner_id = value

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
        obj = Wardrobe()
        obj.set_id(dictionary.get("id"))
        obj.set_owner_id(dictionary.get("owner_id"))
        obj.set_items(dictionary.get("items", []))
        return obj