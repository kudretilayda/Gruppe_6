from server.bo.BusinessObject import BusinessObject

class ClothingType(BusinessObject):
    """Klasse für ClothingType-Objekte."""
    def __init__(self):
        super().__init__()
        self._name = None
        self._description = None
        self._category = None

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def get_description(self):
        return self._description

    def set_description(self, value):
        self._description = value

    def get_category(self):
        return self._category

    def set_category(self, value):
        self._category = value

    def to_dict(self):
        result = super().to_dict()
        result.update({
            'name': self.get_name(),
            'description': self.get_description(),
            'category': self.get_category()
        })
        return result