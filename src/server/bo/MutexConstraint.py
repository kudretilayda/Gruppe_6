class MutexConstraint(BinaryConstraint):
    """Klasse für Mutex-Constraints (wechselseitiger Ausschluss)."""

    def __init__(self):
        super().__init__()
        self.set_constraint_type('mutex')