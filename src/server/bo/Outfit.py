from src.server.bo.BusinessObject import BusinessObject


class Outfit(BusinessObject):

    def __init__(self):
        super().__init__()
        self._outfit_id = 0
        self._outfit_name = ""
        self.item = []
        self.style = None

    def get_outfit_id(self):
        return self._outfit_id

    def set_outfit_id(self, outfit_id: int):
        self._outfit_id = outfit_id

    def get_items(self):
        return self._item

    def set_items(self, item):
        self.item = item

    def get_style(self):
        return self.style

    def set_style(self, style):
        self.style = style

    def get_outfit_name(self):
        return self._outfit_name

    def set_outfit_name(self, outfit_name):
        self._outfit_name = outfit_name

    def __str__(self):
        return "Outfit: {}, {}, {}".format(self._outfit_id, self.item, self.style())

    @staticmethod
    def from_dict(dictionary=dict(), style_instance=None):
        obj = Outfit()
        obj.set_outfit_id(dictionary("outfit_id", 0))
        obj.set_items(dictionary("kleidungsstuecke", []))
        obj.set_style(style_instance)
        return obj
