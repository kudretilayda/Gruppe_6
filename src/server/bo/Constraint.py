# src/models/bo/business_object.py
from datetime import datetime

class BusinessObject:
    def __init__(self):
        self.id = None
        self.created_at = datetime.now()

# src/models/bo/style.py
from server.bo import BusinessObject

class Style(BusinessObject):
    def __init__(self):
        super().__init__()
        self.name = None
        self.features = None
        self.constraints = []
        
    def add_constraint(self, constraint):
        self.constraints.append(constraint)
        
    def remove_constraint(self, constraint):
        self.constraints.remove(constraint)

# src/models/bo/outfit.py
class Outfit(BusinessObject):
    def __init__(self):
        super().__init__()
        self.style_id = None
        self.items = []  # List of Kleidungsstueck objects
        
    def add_item(self, item):
        self.items.append(item)
        
    def remove_item(self, item):
        self.items.remove(item)
        
    def get_types(self):
        return [item.typ for item in self.items]

# src/models/bo/constraint.py
from abc import ABC, abstractmethod

class Constraint(BusinessObject, ABC):
    @abstractmethod
    def is_satisfied(self, items):
        pass
        
    @abstractmethod
    def get_violation_message(self, items):
        pass

class BinaryConstraint(Constraint):
    def __init__(self):
        super().__init__()
        self.bezugsobjekt1 = None
        self.bezugsobjekt2 = None
        
class UnaryConstraint(Constraint):
    def __init__(self):
        super().__init__()
        self.bezugsobjekt = None

class Mutex(BinaryConstraint):
    """Represents mutual exclusion between two items"""
    
    def is_satisfied(self, items):
        # Check if not both items are present
        item1_present = any(item.typ_id == self.bezugsobjekt1 for item in items)
        item2_present = any(item.typ_id == self.bezugsobjekt2 for item in items)
        return not (item1_present and item2_present)
        
    def get_violation_message(self, items):
        return f"Items of types {self.bezugsobjekt1} and {self.bezugsobjekt2} cannot be worn together"

class Kardinalitaet(UnaryConstraint):
    def __init__(self):
        super().__init__()
        self.min_count = 0
        self.max_count = None
        
    def is_satisfied(self, items):
        count = sum(1 for item in items if item.typ_id == self.bezugsobjekt)
        if self.max_count is None:
            return count >= self.min_count
        return self.min_count <= count <= self.max_count
        
    def get_violation_message(self, items):
        return f"Number of items of type {self.bezugsobjekt} must be between {self.min_count} and {self.max_count}"