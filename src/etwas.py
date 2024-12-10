class Kleidungstyp:
    def __init__(self, name):
        self.name = name


class Kleidungsstueck:
    def __init__(self, name):
        self.name = name
        self.kleidungstyp = None


'''
class Style:
    def __init__(self, kleidungstyp):
        constraint_list = []
        
    def auswerten(self, kleidungstyp):
        if not Kleidungstyp()
        if not self.Klei(self.kleidungstyp):
            raise ValueError(f"Constraint verletzt für Bezugsobjekt: {self.obj}.")


class Outfit:
def __init__(self)
'''


class Constraint:
    def __init__(self):
        pass

    def evaluate(self, kleidungstyp):
        pass


tshirt1 = Kleidungsstueck('t-shirt 1')
tshirt1.kleidungstyp = Kleidungstyp('tshirt')

'''Constraints mit einer for schleife durchlaufen

outfits_to_check = [
    ("Kurze Hose", "Winterjacke"),
    ("Jogginghose", "Sakko"),
    ("T-Shirt", "Anzug"),
    ("Jeans", "T-Shirt")  # Gültiges Outfit
]
for outfit in outfits_to_check:
    constraint = BinaryConstraint(outfit[0], outfit[1], ist_unzulässiges_outfit)
    try:
        constraint.auswerten(None)
        print(f"Outfit {outfit[0]} und {outfit[1]} ist zulässig.")
    except ValueError as e:
        print(e)
'''
