from server.bo.BusinessObject import BusinessObject

class ClothingType(BusinessObject):
    """Realisierung eines Kleidungstyps"""
    
    def __init__(self):
        super().__init__()
        self._name = ""
        self._description = ""

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
        obj = ClothingType()
        obj.set_id(dictionary.get("id"))
        obj.set_name(dictionary.get("name"))
        obj.set_description(dictionary.get("description"))
        return obj