from server.db.BinaryConstraintMapper import BinaryConstraintMapper
from server.bo.BinaryConstraint import BinaryConstraint
from typing import List, Optional

class BinaryConstraintService:
    def __init__(self):
        self._mapper = BinaryConstraintMapper()

    def create_constraint(self, style_id: str, ref_obj1_id: str, 
                         ref_obj2_id: str) -> BinaryConstraint:
        constraint = BinaryConstraint()
        constraint.set_style_id(style_id)
        constraint.set_reference_object1_id(ref_obj1_id)
        constraint.set_reference_object2_id(ref_obj2_id)
        return self._mapper.insert(constraint)

    def get_constraint(self, constraint_id: str) -> Optional[BinaryConstraint]:
        return self._mapper.find_by_id(constraint_id)

    def get_constraints_by_style(self, style_id: str) -> List[BinaryConstraint]:
        return self._mapper.find_by_style(style_id)

    def update_constraint(self, constraint: BinaryConstraint) -> BinaryConstraint:
        return self._mapper.update(constraint)

    def delete_constraint(self, constraint_id: str) -> bool:
        constraint = self.get_constraint(constraint_id)
        if constraint:
            self._mapper.delete(constraint)
            return True
        return False