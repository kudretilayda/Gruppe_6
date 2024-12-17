from abc import ABC, abstractmethod
from ClothingType import ClothingType
from src.server.bo.BusinessObject import BusinessObject
from typing import List

class Constraint(BusinessObject, ABC):
    """Abstrakte Basisklasse für alle Constraints"""
    def __init__(self):
        super().__init__()
        self._constraint_id = None
        self._constraint_type = None
        self._style_id = None  # Referenz zum Style, zu dem der Constraint gehört

    def get_constraint_id(self) -> int:
        return self._constraint_id

    def set_constraint_id(self, constraint_id: int):
        self._constraint_id = constraint_id

    def get_style_id(self) -> int:
        return self._style_id

    def set_style_id(self, style_id: int):
        self._style_id = style_id

    def get_constraint_type(self) -> str:
        return self._constraint_type

    def set_constraint_type(self, constraint_type: str):
        self._constraint_type = constraint_type

    @abstractmethod
    def validate(self, outfit: 'Outfit') -> bool:
        """Validiert ein Outfit gegen diesen Constraint"""
        pass

    @staticmethod
    def from_dict(dictionary=dict()):
        # Wird von den konkreten Constraint-Klassen überschrieben
        pass

class UnaryConstraint(Constraint):
    """Constraint für einen einzelnen ClothingType"""
    def __init__(self, reference_object: 'ClothingType'):
        super().__init__()
        self._reference_object = reference_object

    def get_reference_object(self) -> 'ClothingType':
        return self._reference_object

    def set_reference_object(self, reference_object: 'ClothingType'):
        self._reference_object = reference_object

    @staticmethod
    def from_dict(dictionary=dict()):
        obj = UnaryConstraint(None)  # Temporär None als reference_object
        obj.set_constraint_id(dictionary.get("constraint_id", 0))
        obj.set_style_id(dictionary.get("style_id", 0))
        obj.set_constraint_type(dictionary.get("constraint_type", ""))
        # reference_object muss separat gesetzt werden
        return obj

class BinaryConstraint(Constraint):
    """Constraint für zwei ClothingTypes"""
    def __init__(self, reference_object1: 'ClothingType', reference_object2: 'ClothingType'):
        super().__init__()
        self._reference_object1 = reference_object1
        self._reference_object2 = reference_object2

    def get_reference_object1(self) -> 'ClothingType':
        return self._reference_object1

    def set_reference_object1(self, reference_object: 'ClothingType'):
        self._reference_object1 = reference_object

    def get_reference_object2(self) -> 'ClothingType':
        return self._reference_object2

    def set_reference_object2(self, reference_object: 'ClothingType'):
        self._reference_object2 = reference_object

    @staticmethod
    def from_dict(dictionary=dict()):
        obj = BinaryConstraint(None, None)  # Temporär None als reference_objects
        obj.set_constraint_id(dictionary.get("constraint_id", 0))
        obj.set_style_id(dictionary.get("style_id", 0))
        obj.set_constraint_type(dictionary.get("constraint_type", ""))
        # reference_objects müssen separat gesetzt werden
        return obj
