from src.server.bo.BusinessObject import BusinessObject


<<<<<<< HEAD
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
=======
class Wardrobe(BusinessObject):
    def __init__(self):
        super().__init__()
        self._wardrobe_owner = 0
        self._inhalt = []
        self._outfits = []

    def get_wardrobe_owner(self):
        return self._wardrobe_owner

    def set_wardrobe_owner(self, user):
        self._wardrobe_owner = user
>>>>>>> cb40ce594841218d73ecccfcb843f3b4c9718885

    def get_inhalt(self):
        return self._inhalt

<<<<<<< HEAD
    def set_inhalt(self, value):
        self._inhalt = value
=======
    def set_inhalt(self, values):
        self._inhalt = values
>>>>>>> cb40ce594841218d73ecccfcb843f3b4c9718885

    def get_outfits(self):
        return self._outfits

<<<<<<< HEAD
    def set_outfits(self, value):
        self._outfits = value
=======
    def set_outfits(self, values):
        self._outfits = values
>>>>>>> cb40ce594841218d73ecccfcb843f3b4c9718885
