from .Constraint import Constraint


class ImplicationConstraint(Constraint):
    def __init__(self, if_type, then_type):
        super().__init__()
        self.if_type = if_type
        self.then_type = then_type

    def validate(self, outfit):
        has_if_type = False
        has_then_type = False

        for item in outfit.items:
            if item.clothing_type == self.if_type:
                has_if_type = True
            if item.clothing_type == self.then_type:
                has_then_type = True

        if has_if_type and not has_then_type:
            print(f"Regel verletzt: Wenn {self.if_type.name} vorhanden ist, "
                  f"muss auch {self.then_type.name} vorhanden sein.")
            return False
        else:
            return True

    # static method    
    def from_dict(dictionary=None):
        if dictionary is None:
            dictionary = dict()
        constraint = ImplicationConstraint()
        constraint.set_id(dictionary.get("id", 0))
        constraint.if_type = dictionary.get("if_type")
        constraint.then_type = dictionary.get("then_type")
        return constraint
