from src.server.bo.ClothingType import ClothingType
from src.server.bo.ClothingItem import ClothingItem

class ClothingTypeEntry(ClothingType):
    def __init__(self):
        super().__init__()
        self.__clothing_type_id = None

    def get_clothing_type_id(self):
        return self.__clothing_type_id

    def set_clothing_type_id(self, clothing_type_id):
        self.__clothing_type_id = clothing_type_id

    def __str__(self):
        return (f"ID: {self.get_id()}, "
                f"Name: {self.get_name()}, "
                f"Verwendung: {self.get_usage()}, "
                f"ClothingType-ID: {self.get_clothing_type_id()}")

    def __repr__(self):
        return (f"< ClothingTypeEntry(clothing_type_id={self.__clothing_type_id}, "
                f"name={self._name}, "
                f"usage={self._usage}) > ")

    def from_dict(dictionary=None):
        obj = ClothingType()
        obj.set_id(dictionary.get("clothing_type_id"))
        obj.set_name(dictionary.get("clothing_type_name"))
        obj.set_usage(dictionary.get("clothing_type_usage"))
        return obj
