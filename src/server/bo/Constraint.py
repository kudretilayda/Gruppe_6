from server.bo.BusinessObject import BusinessObject


class Constraint(BusinessObject):
    """Realisierung einer Style-Regel"""
    
    def __init__(self):
        super().__init__()
        self._style_id = 0
        self._type = ""  # BINARY, UNARY, MUTEX, IMPLICATION, CARDINALITY
        self._value = ""  # JSON-String mit spezifischen Regeln

    def get_style_id(self):
        return self._style_id

    def set_style_id(self, value):
        self._style_id = value

    def get_type(self):
        return self._type

    def set_type(self, value):
        self._type = value

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value

    @staticmethod
    def from_dict(dictionary=dict()):
        obj = Constraint()
        obj.set_id(dictionary.get("id"))
        obj.set_style_id(dictionary.get("style_id"))
        obj.set_type(dictionary.get("type"))
        obj.set_value(dictionary.get("value"))
        return obj