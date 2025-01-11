from src.server.bo.Constraints.Constraint import Constraint
from src.server.bo.Style import Style


class BinaryConstraint(Constraint):
    def __init__(self, item_1, item_2):
        super().__init__()
        self.item_1 = item_1
        self.item_2 = item_2

    def validate(self):
        style = Style()

        a = self.item_1.clothing_type in style.clothing_type
        b = self.item_2.clothing_type in style.clothing_type

        if a and b:
            return True
        else:
            print(f'{self.item_1.item_name} hat nicht denselben Style wie {self.item_2.item_name}')
            return False
