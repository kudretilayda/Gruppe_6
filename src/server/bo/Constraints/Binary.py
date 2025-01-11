from src.server.bo.Constraints.Constraint import Constraint
from src.server.bo.Style import Style

# Die Klasse BinaryConstraint erbt von der Basisklasse Constraint und stellt eine binäre Bedingung zwischen zwei Objekten dar.
class BinaryConstraint(Constraint):
    def __init__(self, item_1, item_2):
        super().__init__()
        self.item_1 = item_1
        self.item_2 = item_2

    # Methode zur Überprüfung der Constraint-Bedingung
    def validate(self):
        style = Style()

        # Überprüft, ob der Kleidungstyp des ersten Objekts und des zweiten Objekts im gleichen Style vorhanden sind
        a = self.item_1.clothing_type in style.clothing_type
        b = self.item_2.clothing_type in style.clothing_type

        if a and b:
            return True
        else:
            # Wenn die Kleidungstypen nicht im gleichen Style sind, gibt eine Fehlermeldung aus und der Constraint ist ungültig
            print(f'{self.item_1.item_name} hat nicht denselben Style wie {self.item_2.item_name}')
            return False