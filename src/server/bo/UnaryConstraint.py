from src.server.bo.Constraint import Constraint


class UnaryConstraint(Constraint):
    def __init__(self, bezugsobjekt, bedingung):  # Bedingung, um Constraints flexibel zu gestalten
        self.bezugsobjekt = bezugsobjekt
        self.bedingung = bedingung

    def auswerten(self, obj):
        # Validiert das Constraint, indem die Bedingung auf das Bezugsobjekt angewendet wird.
        if not self.bedingung(self.bezugsobjekt):
            raise ValueError(f"Constraint verletzt für Bezugsobjekt: {self.bezugsobjekt}.")
