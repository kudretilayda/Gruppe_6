from server.db.MutexMapper import MutexMapper
from server.bo.MutexConstraint import MutexConstraint
from typing import List, Optional

class MutexConstraintService:
    def __init__(self):
        self._mapper = MutexMapper()

    def create_constraint(self, style_id: str, excluded_types: List[str]) -> MutexConstraint:
        constraint = MutexConstraint()
        constraint.set_style_id(style_id)
        constraint.set_excluded_types(excluded_types)
        return self._mapper.insert(constraint)

    def get_constraint(self, constraint_id: str) -> Optional[MutexConstraint]:
        return self._mapper.find_by_id(constraint_id)

    def get_constraints_by_style(self, style_id: str) -> List[MutexConstraint]:
        return self._mapper.find_by_style(style_id)

    def update_constraint(self, constraint: MutexConstraint) -> MutexConstraint:
        return self._mapper.update(constraint)

    def delete_constraint(self, constraint_id: str) -> bool:
        constraint = self.get_constraint(constraint_id)
        if constraint:
            self._mapper.delete(constraint)
            return True
        return False

    def add_excluded_type(self, constraint_id: str, type_id: str) -> bool:
        constraint = self.get_constraint(constraint_id)
        if constraint:
            constraint.add_excluded_type(type_id)
            self._mapper.update(constraint)
            return True
        return False