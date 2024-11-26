from src.server.bo.BusinessObject import BusinessObject


class Kleiderschrank(BusinessObject):
    def __init__(self):
        super().__init__()
        self._eigentuemer = 0
        self._inhalt = []
        self._outfits = []

    def get_eigentuemer(self):
        return self._eigentuemer

    def set_eigentuemer(self, user):
        self._eigentuemer = user

    def get_inhalt(self):
        return self._inhalt

    def set_inhalt(self, value):
        self._inhalt = value

    def get_outfits(self):
        return self._outfits

    def set_outfits(self, value):
        self._outfits = value
