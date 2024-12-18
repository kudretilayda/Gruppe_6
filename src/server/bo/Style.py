#TypEbene

from src.server.bo.BusinessObject import BusinessObject
from ClothingType import ClothingType
from Constraints import Constraint
from Outfit import Outfit
from typing import List

class Style(BusinessObject):
    def __init__(self, name: str = ""):
        super().__init__()
        self._style_id = None
        self._name = name  #Verwende den Namen aus BusinessObject
        self._features = []  #Liste von Features
        self._constraints = []  #Liste von Constraints
        self._clothing_types = []  #Liste von ClothingType-Objekten

    def get_style_id(self) -> int:
        return self._style_id

    def set_style_id(self, style_id: int):
        self._style_id = style_id

    def get_name(self):
        return self._name

    def set_name(self, param):
        self._name = param

    def add_clothing_type(self, clothing_type: 'ClothingType'):
        """Fügt einen ClothingType zum Style hinzu"""
        if clothing_type not in self._clothing_types:
            self._clothing_types.append(clothing_type)

    def remove_clothing_type(self, clothing_type: 'ClothingType'):
        """Entfernt einen ClothingType aus dem Style"""
        if clothing_type in self._clothing_types:
            self._clothing_types.remove(clothing_type)

    def add_constraint(self, constraint: 'Constraint'):
        """Fügt einen Constraint zum Style hinzu"""
        if constraint not in self._constraints:
            self._constraints.append(constraint)

    def remove_constraint(self, constraint: 'Constraint'):
        """Entfernt einen Constraint aus dem Style"""
        if constraint in self._constraints:
            self._constraints.remove(constraint)

    def validate_outfit(self, outfit: 'Outfit') -> bool:
        #Prüfe erlaubte Kleidungstypen
        for item in outfit.get_items():
            if item.get_type() not in self._clothing_types:
                return False
        #Prüfe alle Constraints
        return all(constraint.validate(outfit) for constraint in self._constraints)

    def get_constraints(self) -> List['Constraint']:
        return self._constraints

    def get_clothing_types(self) -> List['ClothingType']:
        return self._clothing_types

    @staticmethod
    def from_dict(dictionary=dict()):
        obj = Style()
        obj.set_style_id(dictionary.get("style_id", 0))
        obj.set_name(dictionary.get("name", ""))
        obj.__features = dictionary.get("features", [])
        obj.__constraints = dictionary.get("constraints", [])
        obj.__clothing_types = dictionary.get("clothing_types", [])
        return obj
