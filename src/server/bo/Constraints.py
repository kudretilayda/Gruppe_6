from abc import ABC, abstractmethod
from ClothingType import ClothingType
from Outfit import Outfit
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

class Mutex(BinaryConstraint):
    """Zwei ClothingTypes schließen sich gegenseitig aus"""
    def __init__(self, reference_object1: 'ClothingType', reference_object2: 'ClothingType'):
        super().__init__(reference_object1, reference_object2)
        self._constraint_type = "MUTEX"

    def validate(self, outfit: 'Outfit') -> bool:
        """Prüft, ob nicht beide referenzierten Types im Outfit vorhanden sind"""
        type1_present = any(item.get_type() == self._reference_object1 for item in outfit.get_items())
        type2_present = any(item.get_type() == self._reference_object2 for item in outfit.get_items())
        return not (type1_present and type2_present)

class Implication(BinaryConstraint):
    """Wenn Type1 vorhanden ist, muss auch Type2 vorhanden sein"""
    def __init__(self, reference_object1: 'ClothingType', reference_object2: 'ClothingType'):
        super().__init__(reference_object1, reference_object2)
        self._constraint_type = "IMPLICATION"

    def validate(self, outfit: 'Outfit') -> bool:
        """Wenn Type1 vorhanden ist, muss auch Type2 vorhanden sein"""
        type1_present = any(item.get_type() == self._reference_object1 for item in outfit.get_items())
        type2_present = any(item.get_type() == self._reference_object2 for item in outfit.get_items())
        return not type1_present or type2_present

class Cardinality(UnaryConstraint):
    """Definiert minimale und maximale Anzahl eines ClothingTypes"""
    def __init__(self, reference_object: 'ClothingType', min_count: int, max_count: int):
        super().__init__(reference_object)
        self._constraint_type = "CARDINALITY"
        self._min_count = min_count
        self._max_count = max_count

    def get_min_count(self) -> int:
        return self._min_count

    def set_min_count(self, min_count: int):
        self._min_count = min_count

    def get_max_count(self) -> int:
        return self._max_count

    def set_max_count(self, max_count: int):
        self._max_count = max_count

    def validate(self, outfit: 'Outfit') -> bool:
        """Prüft, ob die Anzahl der Items vom referenzierten Typ im erlaubten Bereich liegt"""
        count = sum(1 for item in outfit.get_items() if item.get_type() == self._reference_object)
        return self._min_count <= count <= self._max_count

    @staticmethod
    def from_dict(dictionary=dict()):
        obj = Cardinality(None, 0, 0)  # Temporär None als reference_object
        obj.set_constraint_id(dictionary.get("constraint_id", 0))
        obj.set_style_id(dictionary.get("style_id", 0))
        obj.set_min_count(dictionary.get("min_count", 0))
        obj.set_max_count(dictionary.get("max_count", 0))
        # reference_object muss separat gesetzt werden
        return obj