from .Constraint import Constraint


class CardinalityConstraint(Constraint):
    def __init__(self, objects, min_count, max_count):
        super().__init__()
        self.objects = objects
        self.min_count = min_count
        self.max_count = max_count

    def validate(self):
        selected_count = sum(obj.is_selected() for obj in self.objects)

        if not (self.min_count <= selected_count <= self.max_count):
            print(f"Fehler: Es sind {selected_count} Objekte ausgewählt.")
            print(f"Erlaubt sind zwischen {self.min_count} und {self.max_count} Objekte.")
            return False
        else:
            # Alles in Ordnung
            print("Anzahl der ausgewählten Objekte ist korrekt.")
            return True
        
    # static method
    def from_dict(dictionary=None):
        if dictionary is None:
            dictionary = dict()
        constraint = CardinalityConstraint()
        constraint.set_id(dictionary.get("id", 0))
        constraint.objects = dictionary.get("objects")
        constraint.min_count = dictionary.get("min_count", 0)
        constraint.max_count = dictionary.get("max_count", 0)
        return constraint
