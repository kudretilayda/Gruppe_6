class ImplicationConstraint(BinaryConstraint):
    """Klasse für Implikations-Constraints (Wenn-Dann-Beziehungen)."""

    def __init__(self):
        super().__init__()
        self.set_constraint_type('implikation')