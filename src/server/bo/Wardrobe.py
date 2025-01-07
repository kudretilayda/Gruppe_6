from src.server.bo.BusinessObject import BusinessObject


class Wardrobe(BusinessObject):
    def __init__(self):
        super().__init__()
        self._wardrobe_owner = 0
        self._items = []
        self._outfits = []

    def get_wardrobe_owner(self):
        return self._wardrobe_owner

    def set_wardrobe_owner(self, user):
        self._wardrobe_owner = user

    def get_items(self):
        return self._items

    def set_items(self, item):
        self._items.append(item)

    def get_outfits(self):
        return self._outfits

    def set_outfits(self, outfit):
        self._outfits.append(outfit)

    def __str__(self):
        # Gibt eine textuelle Darstellung des Kühlschranks zurück, hier nur die ID
        return f"ID: {self._id}"

    @classmethod
    def from_dict(cls=None):
        if cls is None:
            cls = dict()

        from ClothingItem import ClothingItem
        obj = Wardrobe()
        obj.set_id(cls['id'])
