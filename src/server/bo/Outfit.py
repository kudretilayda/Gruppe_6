from src.server.bo.BusinessObject import BusinessObject


class Outfit(BusinessObject):

    def __init__(self):
        super().__init__()
        self._outfit_id = 0
        self._items = []
        self._style = None

    def get_outfit_id(self):
        return self._outfit_id

    def set_outfit_id(self, outfit_id: int):
        self._outfit_id = outfit_id

    def get_items(self):
        return self._items

    def set_items(self, items: list):
        self._items = items

    def get_style(self):
        return self._style

    def set_style(self, style):
        self._style = style

    def __str__(self):
        return "Outfit: {}, {}, {}".format(
            self._outfit_id,
            self._items,
            self._style()
        )

    @staticmethod
    def from_dict(dictionary=None, style_instance=None):
        if dictionary is None:
            dictionary = dict()
        obj = Outfit()
        obj.set_outfit_id(dictionary.get("outfit_id", 0))
        obj.set_items(dictionary.get("kleidungsstuecke", []))
        obj.set_style(style_instance)
        return obj
