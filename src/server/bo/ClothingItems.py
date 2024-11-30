from server.bo.BusinessObject import BusinessObject

class ClothingItem(BusinessObject):
    """Realisierung eines Kleidungsstücks"""
    
    def __init__(self):
        super().__init__()
        self._wardrobe_id = 0
        self._type_id = 0
        self._name = ""
        self._description = ""

    def get_wardrobe_id(self):
        return self._wardrobe_id

    def set_wardrobe_id(self, value):
        self._wardrobe_id = value

    def get_type_id(self):
        return self._type_id

    def set_type_id(self, value):
        self._type_id = value

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def get_description(self):
        return self._description

    def set_description(self, value):
        self._description = value

    @staticmethod
    def from_dict(dictionary=dict()):
        obj = ClothingItem()
        obj.set_id(dictionary.get("id"))
        obj.set_wardrobe_id(dictionary.get("wardrobe_id"))
        obj.set_type_id(dictionary.get("type_id"))
        obj.set_name(dictionary.get("name"))
        obj.set_description(dictionary.get("description"))
        return obj