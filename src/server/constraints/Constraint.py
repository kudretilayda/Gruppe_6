from src.server.bo import BusinessObject
from abc import ABC, abstractmethod

class Constraint(BusinessObject, ABC):
    def __init__(self):
        super().__init__()
        
    @abstractmethod
    def check(self):
        pass

class UnaryConstraint(Constraint):
    def __init__(self):
        super().__init__()
        self._reference_object = None
        
    def get_reference_object(self):
        return self._reference_object
        
    def set_reference_object(self, obj):
        self._reference_object = obj
        
    def check(self):
        pass

class BinaryConstraint(Constraint):
    def __init__(self):
        super().__init__()
        self._reference_object1 = None
        self._reference_object2 = None
        
    def get_reference_object1(self):
        return self._reference_object1
        
    def set_reference_object1(self, obj):
        self._reference_object1 = obj
        
    def get_reference_object2(self):
        return self._reference_object2
        
    def set_reference_object2(self, obj):
        self._reference_object2 = obj
        
class Mutex(BinaryConstraint):
    def check(self):
        if self._reference_object1 is not None and self._reference_object2 is not None:
            return not (self._reference_object1 and self._reference_object2)
        return False

class Implication(BinaryConstraint):
    def check(self):
        if self._reference_object1:
            return self._reference_object2
        return True

class Cardinality(UnaryConstraint):
    def __init__(self):
        super().__init__()
        self._min_count = 0
        self._max_count = float('inf')
        
    def set_min_count(self, min_count):
        self._min_count = min_count
        
    def set_max_count(self, max_count):
        self._max_count = max_count
        
    def check(self, count):
        return self._min_count <= count <= self._max_count