from src.server.constraints.Constraint import Constraint


class BinaryConstraint(Constraint):
    def __init__(self, object1, object2, bedingung):
        self.constraint_id = 0
        self.object1 = object1
        self.object2 = object2
        self.bedingung = bedingung

    def get_object1(self):
        return self.object1

    def set_object1(self, object1):
        self.object1 = object1

    def get_object2(self):
        return self.object2

    def set_object2(self, object2):
        self.object2 = object2

    def get_bedingung(self):
        return self.bedingung

    def set_bedingung(self, bedingung):
        self.bedingung = bedingung

    def auswerten(self, obj):
        if not self.bedingung(self.object1, self.object2):
            raise ValueError(f"Binary Constraint verletzt zwischen {self.object1} und {self.object2}")
