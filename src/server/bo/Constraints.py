from abc import ABC, abstractmethod


class ConstraintRule(ABC):
    def __init__(self, style_id: id, constraint_type: str, condition, attribute, val):
        self.style_id = style_id
        self.constraint_type = constraint_type
        self.attribute = attribute
        self.condition = condition
        self.val = val

    @abstractmethod
    def validate(self, *args, **kwargs):
        pass

    def __str__(self):
        return (
            f"ConstraintRule: "
            f"Style ID: {self.style_id}, "
            f"Constraint Type: {self.constraint_type}, "
            f"Condition: {self.condition}, "
            f"Attribute: {self.attribute}, "
            f"Value: {self.val}"
        )


# Unary Constraint
class UnaryConstraint(ConstraintRule):
    def __init__(self, style_id: int, reference_object_id: int, attribute: str, condition: str, val: str):
        super().__init__(style_id, "unary", attribute, condition, val)

        # Outfit --> Style --> Constraints
        # Typ Ebene Style und Typ
        # Gegenstandsebene Item und Outfit
        # An Style Constraints anhängen
        # Integrität prüfen: Das Das und Das ist enthalten. Das Outfit muss Style folgen
        
        self.reference_object_id = reference_object_id

    def validate(self):
        obj_value = getattr(self.reference_object_id, self.attribute)

        if self.condition == "equal" and obj_value != self.val:
            raise ValueError(f"Unary Constraint verletzt: {self.attribute} und {self.val} müssen gleich sein")

        if self.condition == "not equal" and obj_value == self.val:
            raise ValueError(f"Unary Constraint verletzt: {self.attribute} und {self.val} dürfen nicht gleich sein")

        return True


# Binary
class BinaryConstraint(ConstraintRule):
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
class ImplicationConstraint(ConstraintRule):
    def __init__(self, style_id: int, condition_a, condition_b):
        super().__init__(style_id, "implication", None, None, None)
        self.condition_a = condition_a
        self.condition_b = condition_b

    def validate(self):
        if self.condition_a and not self.condition_b:
            raise ValueError(f"Implikation verletzt: {self.condition_a} erfüllt, aber {self.condition_b} nicht")
        return True



# Mutex
class MutexConstraint(ConstraintRule):
    def __init__(self, style_id: int, objects: list):
        super().__init__(style_id, "mutex", None, None, None)
        self.objects = objects

    def validate(self):
        selected = [obj for obj in self.objects if obj.is_selected()]

        if len(selected) > 1:
            raise ValueError("MutexConstraint verletzt: Mehr als ein Objekt ist ausgewählt.")
        return True


# Cardinality
class CardinalityConstraint(ConstraintRule):
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

#static method?