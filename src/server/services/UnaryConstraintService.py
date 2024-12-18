from server.db.UnaryConstraintMapper import UnaryConstraintMapper
from server.bo.UnaryConstraint import UnaryConstraint
from typing import List, Optional

class UnaryConstraintService:
    def __init__(self):
        self._mapper = UnaryConstraintMapper()

    def create_constraint(self, style_id: str, ref_obj_id: str) -> UnaryConstraint:
        constraint = UnaryConstraint()
        constraint.set_style_id(style_id)
        constraint.set_reference_object_id(ref_obj_id)
        return self._mapper.insert(constraint)

    def get_constraint(self, constraint_id: str) -> Optional[UnaryConstraint]:
        return self._mapper.find_by_id(constraint_id)

    def get_constraints_by_style(self, style_id: str) -> List[UnaryConstraint]:
        return self._mapper.find_by_style(style_id)

    def update_constraint(self, constraint: UnaryConstraint) -> UnaryConstraint:
        return self._mapper.update(constraint)

    def delete_constraint(self, constraint_id: str) -> bool:
        constraint = self.get_constraint(constraint_id)
        if constraint:
            self._mapper.delete(constraint)
            return True
        return False