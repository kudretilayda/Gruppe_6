from src.server.bo.Constraints.Constraint import Constraint


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
