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

    def get_inhalt(self):
        return self._items

    def set_inhalt(self, values):
        self._items = values

    def get_outfits(self):
        return self._outfits

    def set_outfits(self, values):
        self._outfits = values

    @classmethod
    def from_dict(cls, payload):
        pass
