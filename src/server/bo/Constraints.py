from abc import ABC, abstractmethod
from src.main import clothing_item
from src.server.bo.ClothingType import ClothingType
from src.server.bo.Style import Style
from src.server.bo.Outfit import Outfit
from src.server.bo.ClothingItem import ClothingItem


class Constraint(ABC):
    def __init__(self):
        self._constraint_id = int

    @abstractmethod
    def validate(self, *args, **kwargs):
        pass


# Unary Constraint
class UnaryConstraint(Constraint):
    def validate(self, outfit):
        for item in outfit.items:
            if item.clothing_type in outfit.style.get_clothing_type():
                return True
            else:
                return False

        # Outfit --> Style --> Constraints
        # Typ Ebene Style und Typ
        # Gegenstandsebene Item und Outfit
        # An Style Constraints anhängen
        # Integrität prüfen: Das, das und das ist enthalten. Das Outfit muss Style folgen


# Binary
class BinaryConstraint(Constraint):
    def __init__(self, style_id: int, object_1, object_2, attribute: str, condition: str, value: str):
        super().__init__(style_id, "binary", attribute, condition, value)
        self.object_1 = object_1
        self.object_2 = object_2

    def validate(self):
        obj1_value = getattr(self.object_1, self.attribute)
        obj2_value = getattr(self.object_2, self.attribute)

        if obj1_value == obj2_value and self.condition == "not equal":
            raise ValueError(f"Binary Constraint verletzt: {self.object_1} und {self.object_2}"
                             f"müssen denselben {self.attribute} teilen")
        return True


# Implication
class ImplicationConstraint(Constraint):
    def __init__(self, style_id: int, condition_a, condition_b):
        super().__init__(style_id, "implication", None, None, None)
        self.condition_a = condition_a
        self.condition_b = condition_b

    def validate(self):
        if self.condition_a and not self.condition_b:
            raise ValueError(f"Implikation verletzt: {self.condition_a} erfüllt, aber {self.condition_b} nicht")
        return True



# Mutex
class MutexConstraint(Constraint):
    def __init__(self, style_id: int, objects: list):
        super().__init__(style_id, "mutex", None, None, None)
        self.objects = objects

    def validate(self):
        selected = [obj for obj in self.objects if obj.is_selected()]

        if len(selected) > 1:
            raise ValueError("MutexConstraint verletzt: Mehr als ein Objekt ist ausgewählt.")
        return True


# Cardinality
class CardinalityConstraint(Constraint):
    def __init__(self, style_id: int, objects: list, min_count: int, max_count: int):
        super().__init__(style_id, "cardinality", None, None, None)
        self.objects = objects
        self.min_count = min_count
        self.max_count = max_count

    def validate(self):
        count = sum(1 for obj in self.objects if obj.is_selected())
        if count < self.min_count or count > self.max_count:
            raise ValueError(f"Kardinalität verletzt: {count} ausgewählt. "
                             f"Wert muss zwischen {self.min_count} und {self.max_count} liegen.")
        return True
