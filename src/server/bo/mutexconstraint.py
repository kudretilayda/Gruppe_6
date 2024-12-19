class Kleidungsstueck:
    def __init__(self,name):
        self.name = name


class Outfit:
    def __init__(self):
        self.items = []

    def add_item(self,item):
        self.items.append(item)

    def get_items(self):
        return self.items


class MutexConstraint:
    def __init__(self):
        self.item_1 = None
        self.item_2 = None                          """auschließende paare"""

    def validate(self, outfit):
        for item in outfit.items:
            if item_1.clothing_type == item_2.clothing_type:
                print(f'Regel verletzt: {item_1} und {item_2} können nicht gleichzeitig im outfit sein.')
                return False
            else:
                return True

            """if item1 in outfit.get_items() and item2 in outfit.get_items():
                print(f'Regel verletzt: {item1.name} und {item2.name} können nicht gleichzeitig im outfit sein.')
                return False
            else:
                return True"""

shorts = Kleidungsstueck("shorts")
anzugshose = Kleidungsstueck("anzugshose")
tshirt = Kleidungsstueck("tshirt")

outfit1 = Outfit()
outfit1.add_item(shorts)
outfit1.add_item(tshirt)

outfit2 = Outfit()
outfit2.add_item(shorts)
outfit2.add_item(anzugshose)

constraint = MutexConstraint(excluded_pairs=shorts, anzugshose)

print(constraint.validate(outfit1))





