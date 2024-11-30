from src.server.bo.Constraint import Constraint


class BinaryConstraint(Constraint):
    def __init__(self, object1, object2, bedingung):  # Bedingung TypeError
        self.object1 = object1            # Bezugsobjekt 1
        self.object2 = object2            # Bezugsobjekt 2
        self.bedingung = bedingung        # Bedingung, welches object1 und object2 prüft

    def auswerten(self, obj):
        if not self.bedingung(self.object1, self.object2):
            raise ValueError(f"Binary Constraint verletzt zwischen {self.object1} und {self.object2}")
