from src.server.bo.Constraint import Constraint


class BinaryConstraint(Constraint):
    def __init__(self, obj1, obj2, bedingung):  # Bedingung TypeError
        self.obj1 = obj1            # Bezugsobjekt 1
        self.obj2 = obj2            # Bezugsobjekt 2
        self.bedingung = bedingung  # Bedingung, welches obj1 und obj2 prüft

    def auswerten(self, obj):
        if not self.bedingung(self.obj1, self.obj2):
            raise ValueError(f"Binary Constraint verletzt zwischen {self.obj1} und {self.obj2}")
