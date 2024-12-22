# Evtl. nicht nötig. Wird gelöscht.

class RuleEngine:

    def __init__(self):
        self.constraints = []

    def add_constraint(self, constraint):
        self.constraints.append(constraint)
        print(f'Constraint hinzugefügt: {constraint}')

    def remove_constraint(self, constraint):
        self.constraints.remove(constraint)

    def update_constraint(self, old_constraint, new_constraint):
        i = self.constraints.index(old_constraint)
        self.constraints[i] = new_constraint

    def list_constraints(self):
        for constraint in self.constraints:
            print(constraint)

    def validate_constraint(self, outfit, style):
        print(f"Validiere Constraints für Style ID {style.style_id} und Outfit {outfit.get_outfit_name()}")
        for constraint in self.constraints:
            if constraint.style_id == style.get_style_id():
                try:
                    constraint.validate()
                    print(f"Constraint erfüllt: {constraint}")
                except ValueError as e:
                    print(f"Constraint verletzt: {constraint} -> {e}")
