from server.bo.BusinessObject import BusinessObject


class Style(BusinessObject):
    """Klasse für Style-Objekte."""
    def __init__(self):
        super().__init__()
        self._name = None
        self._description = None
        self._created_by = None
        self._constraints = []  # Liste von Constraint-IDs

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def get_description(self):
        return self._description

    def set_description(self, value):
        self._description = value

    def get_created_by(self):
        return self._created_by

    def set_created_by(self, value):
        self._created_by = value

    def get_constraints(self):
        return self._constraints

    def set_constraints(self, constraints):
        self._constraints = constraints

    def add_constraint(self, constraint_id):
        if constraint_id not in self._constraints:
            self._constraints.append(constraint_id)

    def remove_constraint(self, constraint_id):
        if constraint_id in self._constraints:
            self._constraints.remove(constraint_id)

    def to_dict(self):
        result = super().to_dict()
        result.update({
            'name': self.get_name(),
            'description': self.get_description(),
            'created_by': self.get_created_by(),
            'constraints': self.get_constraints()
        })
        return result