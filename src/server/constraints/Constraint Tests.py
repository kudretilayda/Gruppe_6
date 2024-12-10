from abc import abstractmethod


class ConstraintRule:
    def __init__(self, style_id: int, constraint_type: str, attribute: str, condition: str, value: str):
        self.style_id = style_id
        self.constraint_type = constraint_type
        self.attribute = attribute
        self.condition = condition
        self.value = value

    @abstractmethod
    def validate(self, *args, **kwargs):
        pass

    def __str__(self):
        return (f"ConstraintRule: "
                f"Style ID={self.style_id}, "
                f"Type={self.constraint_type}, "
                f"Attribute={self.attribute}, "
                f"Condition={self.condition}, "
                f"Value={self.value}")


class UnaryConstraint(ConstraintRule):
    def __init__(self, style_id: int, reference_object, attribute: str, condition: str, value: str):
        super().__init__(style_id, "unary", attribute, condition, value)
        self.reference_object = reference_object

    def validate(self):
        obj_value = getattr(self.reference_object, self.attribute, None)

        if self.condition == "EQUAL" and obj_value != self.value:
            raise ValueError(f"UnaryConstraint verletzt: {self.attribute} muss {self.value} sein.")

        if self.condition == "NOT EQUAL" and obj_value == self.value:
            raise ValueError(f"UnaryConstraint verletzt: {self.attribute} darf nicht {self.value} sein.")

        return True


class BinaryConstraint(ConstraintRule):
    def __init__(self, style_id: int, object1, object2, attribute: str, condition: str, value: str):
        super().__init__(style_id, "binary", attribute, condition, value)
        self.object1 = object1
        self.object2 = object2

    def validate(self):
        obj1_value = getattr(self.object1, self.attribute, None)
        obj2_value = getattr(self.object2, self.attribute, None)

        if self.condition == "NOT EQUAL" and obj1_value == obj2_value:
            raise ValueError(f"BinaryConstraint verletzt: {self.object1} und {self.object2} "
                             f"dürfen nicht dieselbe {self.attribute} haben.")
        return True


class ImplikationConstraint(ConstraintRule):

    def __init__(self, style_id: int, condition_a, condition_b):
        super().__init__(style_id, "implication", None, None, None)
        self.condition_a = condition_a
        self.condition_b = condition_b

    def validate(self):
        if self.condition_a() and not self.condition_b():
            raise ValueError("Implikationsconstraint verletzt: Bedingung A erfüllt, aber Bedingung B nicht.")
        return True


class MutexConstraint(ConstraintRule):

    def __init__(self, style_id: int, objects: list):
        super().__init__(style_id, "mutex", None, None, None)
        self.objects = objects

    def validate(self):
        selected = [obj for obj in self.objects if obj.is_selected()]
        if len(selected) > 1:
            raise ValueError("MutexConstraint verletzt: Mehr als ein Objekt ist ausgewählt.")
        return True


class CardinalityConstraint(ConstraintRule):

    def __init__(self, style_id: int, objects: list, min_count: int, max_count: int):
        super().__init__(style_id, "cardinality", None, None, None)
        self.objects = objects
        self.min_count = min_count
        self.max_count = max_count

    def validate(self):
        count = sum(1 for obj in self.objects if obj.is_selected())
        if count < self.min_count or count > self.max_count:
            raise ValueError(f"CardinalityConstraint verletzt: {count} Objekte ausgewählt, "
                             f"erlaubt sind zwischen {self.min_count} und {self.max_count}.")
        return True
