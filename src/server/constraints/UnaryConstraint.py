from src.server.Constraints.Constraint import Constraint


class UnaryConstraint(Constraint):
    def __init__(self, obj, condition):
        self.constraint_id = 0
        self.obj = obj
        self.condition = condition

    def get_obj(self):
        return self.obj

    def set_obj(self, obj):
        self.obj = obj

    def get_condition(self):
        return self.condition

    def set_condition(self, condition):
        self.condition = condition

    def auswerten(self, obj):
        if not self.condition(self.obj):
            raise ValueError(f"Constraint verletzt für Bezugsobjekt: {self.obj}.")
