from server.bo.BusinessObject import BusinessObject


class ClothingItem(BusinessObject):
    """Klasse für ClothingItem-Objekte."""
    def __init__(self):
        super().__init__()
        self._wardrobe_id = None
        self._type_id = None
        self._product_name = None
        self._color = None
        self._brand = None
        self._season = None

    def get_wardrobe_id(self):
        return self._wardrobe_id

    def set_wardrobe_id(self, value):
        self._wardrobe_id = value

    def get_type_id(self):
        return self._type_id

    def set_type_id(self, value):
        self._type_id = value

    def get_product_name(self):
        return self._product_name

    def set_product_name(self, value):
        self._product_name = value

    def get_color(self):
        return self._color

    def set_color(self, value):
        self._color = value

    def get_brand(self):
        return self._brand

    def set_brand(self, value):
        self._brand = value

    def get_season(self):
        return self._season

    def set_season(self, value):
        self._season = value

    def to_dict(self):
        result = super().to_dict()
        result.update({
            'wardrobe_id': self.get_wardrobe_id(),
            'type_id': self.get_type_id(),
            'product_name': self.get_product_name(),
            'color': self.get_color(),
            'brand': self.get_brand(),
            'season': self.get_season()
        })
        return result