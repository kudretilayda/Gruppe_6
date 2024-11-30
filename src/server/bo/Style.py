from .business_object import BusinessObject

class Style(BusinessObject):
    def __init__(self):
        super().__init__()
        self._features = None
        self._constraints = []  # Liste von Constraint-Objekten
        
    def get_features(self):
        return self._features
        
    def set_features(self, features):
        self._features = features
        
    def add_constraint(self, constraint):
        self._constraints.append(constraint)
        
    def get_constraints(self):
        return self._constraints