from src.server.bo.Constraint import Constraint


class ImplicationConstraint(Constraint):
    def __init__(self, condition=None, implication=None):
        super().__init__()
        self.constraint_id = 0
        self.condition = condition
        self.implication = implication

    def get_condition(self):
        return self.condition

    def set_condition(self, value):
        self.condition = value

    def get_implication(self):
        return self.implication

    def set_implication(self, value):
        self.implication = value

    def auswerten(self, obj):

        if self.condition is not None:
            # Beispielhafte Evaluierungslogik:
            # Wenn die Bedingung erfüllt ist, muss die Implikation ebenfalls erfüllt sein.
            if self.condition:  # Beispiel: Wenn die Bedingung wahr ist
                return self.implication  # Die Implikation muss wahr sein
        return True

    def __str__(self):

        return (
            f"ImplicationConstraint: "
            f"Bedingung: {self.condition}, "
            f"Implikation: {self.implication}"
        )

    @staticmethod
    def from_dict(dictionary=None):
        if dictionary is None:
            dictionary = dict()
        obj = ImplicationConstraint()
        obj.set_condition(dictionary.get("condition", None))
        obj.set_implication(dictionary.get("implication", None))
        return obj
