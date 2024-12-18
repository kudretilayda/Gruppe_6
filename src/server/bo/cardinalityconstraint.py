class kleidungsstueck:
    def __init__(self, name, selected=False):
        self.name= name
        self.selected = selected

    def is_select(self):
        return self.selected

class cardinalityconstraint:
    def __init__(self, style_id, objects, min_count, max_count):
        self.style_id = style_id
        self.objects = objects
        self.min_count = min_count
        self.max_count = max_count


    def validate(self):
        selected_count = sum(obj.is_selected()
            for obj in self.objects)

        if not (self.min_count <= selected_count <= self.max_count):
            print(f"Fehler: Es sind {selected_count} Objekte ausgewählt.")
            print(f"Erlaubt sind zwischen {self.min_count} und {self.max_count} Objekte.")
            return False
        else:
            # Alles in Ordnung
            print("Anzahl der ausgewählten Objekte ist korrekt.")
            return True

anzugshose = kleidungsstueck("anzugshose", selected=True)
hose = kleidungsstueck("hose", selected=False)


constraint = cardinalityconstraint(1, [anzugshose, hose], 1, 1)