class Kleidungsstueck:
    def __init__(self):
        self.kleidungstyp = None

class Kleidungstyp:
    def __init__(self):
        self.name = None

class Style:
    def __init__(self):
        self.constraints = []
        self.clothing_type = []

    def append_clothing_type(self, clothing_type):
        self.clothing_type.append(clothing_type)

    def get_clothing_type(self):
        return self.clothing_type

    def validate(self, outfit):
        for constrain in self.constraints:
            if constrain.validate(outfit):
                return True
            else:
                return False

class Outfit:
    def __init__(self):
        self.inhalt = []
        self.style = None

    def set_inhalt(self, item):
        self.inhalt.append(item)

    def get_inhalt(self):
        return self.inhalt

    def set_style(self, style):
        self.style = style

    def get_style(self):
        return self.style

class Constraint:
    def validate(self, outfit):
        for inhalt in outfit.inhalt:
            if inhalt.kleidungstyp in outfit.style.get_clothing_type():
                return True
            else:
                return False

# Neue Klasse für Implikations-Constraint
class ImplicationConstraint(Constraint):
    def __init__(self, if_type, then_type):
        self.if_type = if_type
        self.then_type = then_type

    def validate(self, outfit):
        has_if_type = False
        has_then_type = False

        for inhalt in outfit.inhalt:
            if inhalt.kleidungstyp == self.if_type:
                has_if_type = True
            if inhalt.kleidungstyp == self.then_type:
                has_then_type = True

        if has_if_type and not has_then_type:
            print(f"Regel verletzt: Wenn {self.if_type.name} vorhanden ist, muss auch {self.then_type.name} vorhanden sein.")
            return False
        return True

# Kleidungstypen
pulli = Kleidungstyp()
pulli.name = "Pulli"
hose = Kleidungstyp()  
hose.name = "Hose"

# Style und Outfit
style1 = Style()
Rollkragenpulli = Kleidungsstueck()
Jeans = Kleidungsstueck()
outfit1 = Outfit()

# Kleidungsstück -> Kleidungstyp
Rollkragenpulli.kleidungstyp = pulli
Jeans.kleidungstyp = hose

# Outfit -> Kleidungsstück
outfit1.inhalt = [Rollkragenpulli, Jeans]

# Outfit -> Style  
outfit1.set_style(style1)

# Style -> Typ
style1.append_clothing_type(pulli)
style1.append_clothing_type(hose)

# Implikations-Constraint erstellen und zum Style hinzufügen
implication_constraint = ImplicationConstraint(pulli, hose)
style1.constraints.append(implication_constraint)

# Validierung
print(style1.validate(outfit1))
