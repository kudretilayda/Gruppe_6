from src.server.bo.Constraint import Constraint


class ImplicationConstraint(Constraint):
    def __init__(self, condition=None, implication=None):
        super().__init__()    
        self._condition = condition
        self._implication = implication

    def get_condition(self):
        return self._condition

    def set_condition(self, value):
        self._condition = value

    def get_implication(self):
        return self._implication

    def set_implication(self, value):
        self._implication = value

    def auswerten(self, obj):

        if self._condition is not None:
            # Beispielhafte Evaluierungslogik:
            # Wenn die Bedingung erfüllt ist, muss die Implikation ebenfalls erfüllt sein.
            if self._condition:  # Beispiel: Wenn die Bedingung wahr ist
                return self._implication  # Die Implikation muss wahr sein
        return True

    def __str__(self):

        return (
            f"ImplicationConstraint: "
            f"Bedingung: {self._condition}, "
            f"Implikation: {self._implication}"
        )

    @staticmethod
    def from_dict(dictionary=None):
        if dictionary is None:
            dictionary = dict()
        obj = ImplicationConstraint()
        obj.set_condition(dictionary.get("condition", None))
        obj.set_implication(dictionary.get("implication", None))
        return obj

