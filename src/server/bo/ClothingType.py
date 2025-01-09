from .BusinessObject import BusinessObject


class ClothingType(BusinessObject):
    def __init__(self):
        super().__init__()
        self._name = ""
        self._usage = ""

    def get_id(self):
        return self._id

    def set_id(self, value):
        self._id = value

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def get_usage(self):
        return self._usage

    def set_usage(self, value):
        self._usage = value

    def __str__(self):
        return "Kleidungstyp: {}, Name: {}, Verwendung: {}".format(
            self.get_id(), self._name, self._usage
        )

    @staticmethod
    def from_dict(dictionary=None):
        if dictionary is None:
            dictionary = {}
        obj = ClothingType()
        obj.set_id(dictionary.get("clothing_type_id", 0))
        obj.set_name(dictionary.get("clothing_type_name", ""))
        obj.set_usage(dictionary.get("clothing_type_usage", 0))
        return obj
