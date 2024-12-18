from abc import ABC, abstractmethod
from ClothingType import ClothingType
from Outfit import Outfit
from src.server.bo.BusinessObject import BusinessObject
from typing import List

class Constraint(BusinessObject, ABC):
    """Abstrakte Basisklasse für alle Constraints"""
    def __init__(self):
        super().__init__()
        #self._constraint_type = None
        self._constraint_id = None
        self._style_id = None  #Referenz zum Style, zu dem der Constraint gehört

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
    def __init__(self, reference_object1: 'ClothingType', reference_object2: 'ClothingType'):
        super().__init__()
        # Statt direkte Objekte zu speichern, speichern wir die IDs
        self._reference_type1_id = reference_object1.get_id() if reference_object1 else None
        self._reference_type2_id = reference_object2.get_id() if reference_object2 else None

    def get_reference_type1_id(self) -> int:
        return self._reference_type1_id

    def set_reference_type1_id(self, type_id: int):
        self._reference_type1_id = type_id

    def get_reference_type2_id(self) -> int:
        return self._reference_type2_id

    def set_reference_type2_id(self, type_id: int):
        self._reference_type2_id = type_id

    @staticmethod
    def from_dict(dictionary=dict()):
        obj = BinaryConstraint(None, None)
        obj.set_id(dictionary.get("id", 0))  # BusinessObject ID
        obj.set_constraint_id(dictionary.get("constraint_id", 0))
        obj.set_style_id(dictionary.get("style_id", 0))
        obj.set_reference_type1_id(dictionary.get("reference_type1_id", 0))
        obj.set_reference_type2_id(dictionary.get("reference_type2_id", 0))
        return obj

class Mutex(BinaryConstraint):
    def __init__(self, reference_object1: 'ClothingType', reference_object2: 'ClothingType'):
        super().__init__(reference_object1, reference_object2)

    def validate(self, outfit: 'Outfit') -> bool:
        items = outfit.get_items()
        type1_present = any(item.get_type().get_id() == self._reference_type1_id
                          for item in items)
        type2_present = any(item.get_type().get_id() == self._reference_type2_id
                          for item in items)
        return not (type1_present and type2_present)

    @staticmethod
    def from_dict(dictionary=dict()):
        obj = Mutex(None, None)
        obj.set_id(dictionary.get("id", 0))
        obj.set_constraint_id(dictionary.get("constraint_id", 0))
        obj.set_style_id(dictionary.get("style_id", 0))
        obj.set_reference_type1_id(dictionary.get("reference_type1_id", 0))
        obj.set_reference_type2_id(dictionary.get("reference_type2_id", 0))
        return obj

class Implication(BinaryConstraint):
    """
    Wenn Type1 vorhanden ist, muss auch Type2 vorhanden sein
    Beispiel: Wenn Hemd, dann muss auch Hose getragen werden
    """
    def __init__(self, reference_object1: 'ClothingType', reference_object2: 'ClothingType'):
        super().__init__(reference_object1, reference_object2)

    def validate(self, outfit: 'Outfit') -> bool:
        items = outfit.get_items()
        type1_present = any(item.get_type().get_id() == self._reference_type1_id
                          for item in items)
        type2_present = any(item.get_type().get_id() == self._reference_type2_id
                          for item in items)
        return not type1_present or type2_present  # Logische Implikation

    @staticmethod
    def from_dict(dictionary=dict()):
        obj = Implication(None, None)
        obj.set_id(dictionary.get("id", 0))
        obj.set_constraint_id(dictionary.get("constraint_id", 0))
        obj.set_style_id(dictionary.get("style_id", 0))
        obj.set_reference_type1_id(dictionary.get("reference_type1_id", 0))
        obj.set_reference_type2_id(dictionary.get("reference_type2_id", 0))
        return obj

class Cardinality(Constraint):
    """
    Definiert die erlaubte Anzahl eines Kleidungstyps
    Beispiel: Genau zwei Socken, maximal eine Hose
    """
    def __init__(self, reference_object: 'ClothingType', min_count: int, max_count: int):
        super().__init__()
        self._reference_type_id = reference_object.get_id() if reference_object else None
        self._min_count = min_count
        self._max_count = max_count

    def get_reference_type_id(self) -> int:
        return self._reference_type_id

    def set_reference_type_id(self, type_id: int):
        self._reference_type_id = type_id

    def get_min_count(self) -> int:
        return self._min_count

    def set_min_count(self, count: int):
        self._min_count = count

    def get_max_count(self) -> int:
        return self._max_count

    def set_max_count(self, count: int):
        self._max_count = count

    def validate(self, outfit: 'Outfit') -> bool:
        items = outfit.get_items()
        count = sum(1 for item in items
                   if item.get_type().get_id() == self._reference_type_id)
        return self._min_count <= count <= self._max_count

    @staticmethod
    def from_dict(dictionary=dict()):
        obj = Cardinality(None, 0, 0)
        obj.set_id(dictionary.get("id", 0))
        obj.set_constraint_id(dictionary.get("constraint_id", 0))
        obj.set_style_id(dictionary.get("style_id", 0))
        obj.set_reference_type_id(dictionary.get("reference_type_id", 0))
        obj.set_min_count(dictionary.get("min_count", 0))
        obj.set_max_count(dictionary.get("max_count", 0))
        return obj

