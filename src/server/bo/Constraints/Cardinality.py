from src.server.bo.Constraints.Constraint import Constraint


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
            print("Anzahl der ausgewählten Objekte ist korrekt.")
            return True
