from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Optional
from enum import Enum

class ConstraintType(Enum):
    UNARY = "unary"
    BINARY = "binary" 
    IMPLICATION = "implication"
    MUTEX = "mutex"
    CARDINALITY = "cardinality"

class ConstraintViolation:
    def __init__(self, message: str, severity: str = "error"):
        self.message = message
        self.severity = severity
        self.timestamp = datetime.now()

    def __str__(self):
        return f"{self.severity.upper()}: {self.message}"

class ValidationResult:
    def __init__(self):
        self.violations: List[ConstraintViolation] = []
        self.is_valid: bool = True

    def add_violation(self, message: str, severity: str = "error"):
        self.violations.append(ConstraintViolation(message, severity))
        if severity == "error":
            self.is_valid = False

    def __bool__(self):
        return self.is_valid

class ConstraintRule(ABC):
    def __init__(self, style_id: int, constraint_type: ConstraintType):
        self.style_id = style_id
        self.constraint_type = constraint_type
        self.created_at = datetime.now()

    @abstractmethod
    def validate(self, outfit) -> ValidationResult:
        pass

    def __str__(self):
        return f"{self.constraint_type.value} constraint for style {self.style_id}"

class UnaryConstraint(ConstraintRule):
    def __init__(self, style_id: int, reference_object_id: int, attribute: str, condition: str, value: str):
        super().__init__(style_id, ConstraintType.UNARY)
        self.reference_object_id = reference_object_id
        self.attribute = attribute
        self.condition = condition
        self.value = value

    def validate(self, clothing_item) -> ValidationResult:
        result = ValidationResult()
        
        if not hasattr(clothing_item, self.attribute):
            result.add_violation(f"Item does not have attribute {self.attribute}")
            return result

        item_value = getattr(clothing_item, self.attribute)
        
        if self.condition == "EQUAL" and item_value != self.value:
            result.add_violation(
                f"Item {clothing_item.get_id()} must have {self.attribute}={self.value}"
            )
        elif self.condition == "NOT_EQUAL" and item_value == self.value:
            result.add_violation(
                f"Item {clothing_item.get_id()} must not have {self.attribute}={self.value}"
            )
        elif self.condition == "IN" and item_value not in self.value.split(","):
            result.add_violation(
                f"Item {clothing_item.get_id()} {self.attribute} must be one of {self.value}"
            )

        return result

class BinaryConstraint(ConstraintRule):
    def __init__(self, style_id: int, object_1_id: int, object_2_id: int, attribute: str, condition: str):
        super().__init__(style_id, ConstraintType.BINARY)
        self.object_1_id = object_1_id
        self.object_2_id = object_2_id
        self.attribute = attribute
        self.condition = condition

    def validate(self, item1, item2) -> ValidationResult:
        result = ValidationResult()
        
        if not hasattr(item1, self.attribute) or not hasattr(item2, self.attribute):
            result.add_violation(f"Items do not have attribute {self.attribute}")
            return result

        value1 = getattr(item1, self.attribute)
        value2 = getattr(item2, self.attribute)

        if self.condition == "MATCH" and value1 != value2:
            result.add_violation(
                f"Items {item1.get_id()} and {item2.get_id()} must match on {self.attribute}"
            )
        elif self.condition == "DIFFERENT" and value1 == value2:
            result.add_violation(
                f"Items {item1.get_id()} and {item2.get_id()} must differ on {self.attribute}"
            )

        return result

class MutexConstraint(ConstraintRule):
    def __init__(self, style_id: int, item_type_1_id: int, item_type_2_id: int):
        super().__init__(style_id, ConstraintType.MUTEX)
        self.item_type_1_id = item_type_1_id
        self.item_type_2_id = item_type_2_id

    def validate(self, outfit) -> ValidationResult:
        result = ValidationResult()
        
        type1_items = [item for item in outfit.get_items() 
                      if item.get_clothing_type_id() == self.item_type_1_id]
        type2_items = [item for item in outfit.get_items() 
                      if item.get_clothing_type_id() == self.item_type_2_id]

        if type1_items and type2_items:
            result.add_violation(
                f"Cannot combine items of type {self.item_type_1_id} with type {self.item_type_2_id}"
            )

        return result

class ImplicationConstraint(ConstraintRule):
    def __init__(self, style_id: int, if_type_id: int, then_type_id: int):
        super().__init__(style_id, ConstraintType.IMPLICATION)
        self.if_type_id = if_type_id
        self.then_type_id = then_type_id

    def validate(self, outfit) -> ValidationResult:
        result = ValidationResult()
        
        if_items = [item for item in outfit.get_items() 
                   if item.get_clothing_type_id() == self.if_type_id]
        then_items = [item for item in outfit.get_items() 
                     if item.get_clothing_type_id() == self.then_type_id]

        if if_items and not then_items:
            result.add_violation(
                f"When using items of type {self.if_type_id}, must also include type {self.then_type_id}"
            )

        return result

class CardinalityConstraint(ConstraintRule):
    def __init__(self, style_id: int, item_type_id: int, min_count: int = 0, max_count: Optional[int] = None):
        super().__init__(style_id, ConstraintType.CARDINALITY)
        self.item_type_id = item_type_id
        self.min_count = min_count
        self.max_count = max_count if max_count is not None else float('inf')

    def validate(self, outfit) -> ValidationResult:
        result = ValidationResult()
        
        type_items = [item for item in outfit.get_items() 
                     if item.get_clothing_type_id() == self.item_type_id]
        count = len(type_items)

        if count < self.min_count:
            result.add_violation(
                f"Must include at least {self.min_count} items of type {self.item_type_id}"
            )
        
        if count > self.max_count:
            result.add_violation(
                f"Cannot include more than {self.max_count} items of type {self.item_type_id}"
            )

        return result