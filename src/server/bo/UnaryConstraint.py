from src.server.bo.Constraint import Constraint


class UnaryConstraint(Constraint):
    def __init__(self, bezugsobjekt, bedingung):  # Bedingung, um Constraints flexibel zu gestalten
        self.bezugsobjekt = bezugsobjekt
        self.bedingung = bedingung

    def auswerten(self):
        # Validiert das Constraint, indem die Bedingung auf das Bezugsobjekt angewendet wird.
        if not self.condition(self.bezugsobjekt):
            raise ValueError(f"Constraint verletzt für Bezugsobjekt: {self.bezugsobjekt}.")


# Beispielobjekt
''' 
class Kleidungsstueck:
    def __init__(self, typ, bezeichnung):
        self.typ = typ
        self.bezeichnung = bezeichnung


# Erstellen eines Unary Constraints

kleid = Kleidungsstück(typ="Shorts", bezeichnung="Sommer-Shorts")
constraint = UnaryConstraint(
    bezugsobjekt=kleid,
    condition=lambda obj: obj.typ in ["Hemd", "Hose"]
)

# Validierung
try:
    constraint.validate()
except ValueError as e:
    print(e)  # Constraint verletzt für Bezugsobjekt: <Kleidungsstück-Objekt>.
    '''
