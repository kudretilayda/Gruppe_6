from .Constraint import Constraint


class MutexConstraint(Constraint):
    def __init__(self, mutex):
        super().__init__()
        self.mutex = mutex

    def validate(self, outfit):
        for pair in self.mutex:
            item_1, item_2 = pair
            if item_1 in outfit.get_items() and item_2 in outfit.get_items():
                print(f"Regel verletzt: {item_1.item_name} und {item_2.item_name} können nicht gleichzeitig im Outfit sein.")
                return False
            else:
                print("Outfit erfüllt die Mutex-Bedingungen.")
                return True
