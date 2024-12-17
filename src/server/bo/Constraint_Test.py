class Kleidungsstueck:
    def __init__(self):
        self.kleidungstyp = None


class Kleidungstyp:
    def __init__(self, name):
        self.name = name


Rollkragenpulli = Kleidungsstueck()
Rollkragenpulli.kleidungstyp = Kleidungstyp('pulli')

class Style:
    def __init__(self):
        self.constraints = []

    def validate(self, constraint):
        for constraint in constraint.constraints:
            if constraint.validate():
                return True
            else:
                return False


class Outfit:
    def __init__(self):
        self.inhalt = []

outfit1 = Outfit()
outfit1.inhalt = [Rollkragenpulli]

class Constraint:
    def validate(self, outfit):
        for inhalt in outfit.inhalt:
            if inhalt.kleidungstyp.name == 'pulli':
                return True
            else:
                return False

constraint = Constraint()
print(constraint.validate(outfit1))
