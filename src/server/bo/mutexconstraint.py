class Kleidungsstueck:
    def __init__(self,name,item1,item2):
        self.name = name
        self.item1 = item1
        self.item2 = item2

class Outfit:
    def __init__(self):
        self.items = []

    def add_item(self,item):
        self.items.append(item)

    def get_items(self):
        return self.items


class MutexConstraint:
    def __init__(self, excluded_pairs):
        self.excluded_pairs = excluded_pairs

    def validate(self, outfit):


