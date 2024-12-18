#TypEbene

from src.server.bo.BusinessObject import BusinessObject

class ClothingType(BusinessObject):
    def __init__(self, name: str = "", usage: str= ""):
        super().__init__()
        self._id = None
        self._name = name
        self._usage = usage

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
        return f"ClothingType: ID={self._id}, Name={self._name}, Usage={self._usage}"


    @staticmethod
    def from_dict(dictionary=dict()):
        obj = ClothingType()
        obj.set_id(dictionary.get("id", 0))
        obj.set_name(dictionary.get("name", ""))
        obj.set_usage(dictionary.get("usage", ""))
        return obj