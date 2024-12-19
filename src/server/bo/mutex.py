class Kleidungsstueck:
    def __init__(self, name):
        self.name = name


class Outfit:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_items(self):
        return self.items


class MutexConstraint:
    def __init__(self, excluded_pairs):
        self.excluded_pairs = excluded_pairs

    def validate(self, outfit):
        for pair in self.excluded_pairs:
            item_1, item_2 = pair
            if item_1 in outfit.get_items() and item_2 in outfit.get_items():
                print(f"Regel verletzt: {item_1.name} und {item_2.name} können nicht gleichzeitig im Outfit sein.")
                return False
        print("Outfit erfüllt die Mutex-Bedingungen.")
        return True



shorts = Kleidungsstueck("shorts")
lange_hose = Kleidungsstueck("lange hose")
tshirt = Kleidungsstueck("tshirt")


outfit1 = Outfit()
outfit1.add_item(shorts)
outfit1.add_item(tshirt)

outfit2 = Outfit()
outfit2.add_item(shorts)
outfit2.add_item(lange_hose)


constraint = MutexConstraint(excluded_pairs=[(shorts, lange_hose)])


print(constraint.validate(outfit1))

print(constraint.validate(outfit2))
