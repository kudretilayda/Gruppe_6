from src.server.bo.BusinessObject import BusinessObject


class Wardrobe(BusinessObject):

    def __init__(self):
        super().__init__()
        self._wardrobe_id = 0
        self._wardrobe_name = ""
        self._owner_id = 0
        self._creation_date = None

    def get_id(self):
        return self._wardrobe_id

    def set_id(self, wardrobe_id: int):
        self._wardrobe_id = wardrobe_id

    def get_wardrobe_name(self):
        return self._wardrobe_name

    def set_wardrobe_name(self, wardrobe_name: str):
        self._wardrobe_name = wardrobe_name

    def get_owner_id(self):
        return self._owner_id

    def set_owner_id(self, owner_id: int):
        self._owner_id = owner_id

    def get_creation_date(self):
        return self._creation_date

    def set_creation_date(self, creation_date):
        self._creation_date = creation_date

    def __str__(self):
        return "Wardrobe ID: {}, Name: {}, Owner ID: {}, Created: {}".format(
            self.get_id(),
            self.get_wardrobe_name(),
            self.get_owner_id(),
            self.get_creation_date()
        )

    @staticmethod
    def from_dict(dictionary=None):
        if dictionary is None:
            dictionary = {}
        obj = Wardrobe()
        obj.set_id(dictionary.get("wardrobe_id", 0))
        obj.set_wardrobe_name(dictionary.get("wardrobe_name", ""))
        obj.set_owner_id(dictionary.get("owner_id", 0))
        obj.set_creation_date(dictionary.get("creation_date", None))
        return obj