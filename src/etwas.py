class Kleidungstyp:
    def __init__(self, name):
        self.name = name


class Kleidungsstueck:
    def __init__(self, name):
        self.name = name
        self.kleidungstyp = None


class Style:
    def __init__(self, constraint_list):
        constraint_list = constraint_list


'''
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
