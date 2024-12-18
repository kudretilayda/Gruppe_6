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

    def validate(self):
        for constrain in self.constraints:
            if constrain.validate():
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


pulli = Kleidungstyp()
style1 = Style()
Rollkragenpulli = Kleidungsstueck()
outfit1 = Outfit()

# Kleidungsstück -> Kleidungstyp
Rollkragenpulli.kleidungstyp = pulli
# Outfit -> Kleidungsstück
outfit1.inhalt = [Rollkragenpulli]
# Outfit -> Style
outfit1.set_style(style1)
# Style -> Typ
style1.append_clothing_type(pulli)


constraint = Constraint()
print(constraint.validate(outfit1))
print(style1)
