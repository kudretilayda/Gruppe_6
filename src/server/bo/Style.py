from src.server.bo.BusinessObject import BusinessObject
from ClothingType import ClothingType
from Constraints import Constraint
from Outfit import Outfit
from typing import List

class Style(BusinessObject):
    def __init__(self, name: str = ""):
        super().__init__()
        self.__style_id = None
        self._name = name  #Verwende den Namen aus BusinessObject
        self.__features = []  #Liste von Features
        self.__constraints = []  #Liste von Constraints
        self.__clothing_types = []  #Liste von ClothingType-Objekten

    def get_style_id(self) -> int:
        return self.__style_id

    def set_style_id(self, style_id: int):
        self.__style_id = style_id

    def get_name(self):
        return self.__name

    def set_name(self, param):
        self.__name = param

    def add_clothing_type(self, clothing_type: 'ClothingType'):
        """Fügt einen ClothingType zum Style hinzu"""
        if clothing_type not in self.__clothing_types:
            self.__clothing_types.append(clothing_type)

    def remove_clothing_type(self, clothing_type: 'ClothingType'):
        """Entfernt einen ClothingType aus dem Style"""
        if clothing_type in self.__clothing_types:
            self.__clothing_types.remove(clothing_type)

    def add_constraint(self, constraint: 'Constraint'):
        """Fügt einen Constraint zum Style hinzu"""
        if constraint not in self.__constraints:
            self.__constraints.append(constraint)

    def remove_constraint(self, constraint: 'Constraint'):
        """Entfernt einen Constraint aus dem Style"""
        if constraint in self.__constraints:
            self.__constraints.remove(constraint)

    def validate_outfit(self, outfit: 'Outfit') -> bool:
        """Prüft, ob ein Outfit alle Constraints des Styles erfüllt"""
        return all(constraint.validate(outfit) for constraint in self.__constraints)

    def __str__(self):
        return (f"Style: ID={self.__style_id}, Name={self._name}, "
                f"Features={self.__features}, "
                f"#Constraints={len(self.__constraints)}, "
                f"#ClothingTypes={len(self.__clothing_types)}")

    @staticmethod
    def from_dict(dictionary=dict()):
        obj = Style()
        obj.set_style_id(dictionary.get("style_id", 0))
        obj.set_name(dictionary.get("name", ""))
        obj.__features = dictionary.get("features", [])
        obj.__constraints = dictionary.get("constraints", [])
        obj.__clothing_types = dictionary.get("clothing_types", [])
        return obj
