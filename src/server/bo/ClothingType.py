from src.server.bo.BusinessObject import BusinessObject


class ClothingType(BusinessObject):
    def __init__(self):
        super().__init__()
        self._id = int
        self._name = ""
        self._verwendung = ""

    def get_id(self):
        return self._id

    def set_id(self, value):
        self._id = value

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def get_verwendung(self):
        return self._verwendung

    def set_verwendung(self, value):
        self._verwendung = value

    def __str__(self):
        return "Kleidungstyp: {}, Name: {}, Verwendung: {}".format(
            self.get_id(), self._name, self._verwendung
        )

    @staticmethod
    def from_dict(dictionary=None):
        if dictionary is None:
            dictionary = {}
        obj = ClothingType()
        obj.set_id(dictionary.get("kleidungstyp_id", 0))
        obj.set_name(dictionary.get("kleidungstyp_name", ""))
        obj.set_verwendung(dictionary.get("kleidungstyp_verwendung", 0))
        return obj
