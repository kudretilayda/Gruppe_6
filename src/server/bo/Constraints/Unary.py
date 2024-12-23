from src.server.bo.Constraints.Constraint import Constraint

class UnaryConstraint(Constraint):

    def __init__(self):
        super().__init__()
        self.style = None

    def validate(self, outfit):
        for item in outfit.item:
            if item.clothing_type in outfit.style.get_clothing_type():
                return True
            else:
                print(f'{item.item_name} entspricht nicht dem Style des Outfits')
                return False
