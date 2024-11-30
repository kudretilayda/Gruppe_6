from server.bo.BusinessObject import BusinessObject

class Style(BusinessObject):
    """Realisierung eines Styles"""
    
    def __init__(self):
        super().__init__()
        self._name = ""
        self._description = ""
        self._features = ""

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def get_description(self):
        return self._description

    def set_description(self, value):
        self._description = value

    def get_features(self):
        return self._features

    def set_features(self, value):
        self._features = value

    @staticmethod
    def from_dict(dictionary=dict()):
        obj = Style()
        obj.set_id(dictionary.get("id"))
        obj.set_name(dictionary.get("name"))
        obj.set_description(dictionary.get("description"))
        obj.set_features(dictionary.get("features"))
        return obj