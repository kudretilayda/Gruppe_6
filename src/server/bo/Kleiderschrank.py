from src.server.bo.BusinessObject import BusinessObject
import User


class Kleiderschrank(BusinessObject):
    def __init__(self):
        super().__init__()

    def get_inhalt(self):
        return self._inhalt

    def set_inhalt(self, value):
        self._inhalt = value

    def get_outfits(self):
        return self._outfits

    def set_outfits(self, value):
        self._outfits = value
