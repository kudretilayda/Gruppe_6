from src.server.bo.Constraint import Constraint


class UnaryConstraint(Constraint):
    def __init__(self, bezugsobjekt, bedingung):
        self.bezugsobjekt = bezugsobjekt
        self.bedingung = bedingung

    def auswerten(self, obj):
        if not self.bedingung(self.bezugsobjekt):
            raise ValueError(f"Constraint verletzt für Bezugsobjekt: {self.bezugsobjekt}.")
