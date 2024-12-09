from src.server.bo.BusinessObject import BusinessObject


class Wardrobe(BusinessObject):
    def __init__(self):
        super().__init__()
        self._wardrobe_owner = 0
        self._inhalt = []
        self._outfits = []

    def get_eigentuemer(self):
        return self._wardrobe_owner

    def set_wardrobe_owner(self, user):
        self._wardrobe_owner = user

    def get_inhalt(self):
        return self._inhalt

    def set_inhalt(self, value):
        self._inhalt = value

    def get_outfits(self):
        return self._outfits

    def set_outfits(self, value):
        self._outfits = value
