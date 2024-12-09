from server.db.ImplicationMapper import ImplikationMapper
from server.bo.ImplicationConstraint import ImplikationConstraint
from typing import List, Optional

class ImplikationConstraintService:
    def __init__(self):
        self._mapper = ImplikationMapper()

    def create_constraint(self, style_id: str, if_type_id: str, 
                         then_type_id: str) -> ImplikationConstraint:
        constraint = ImplikationConstraint()
        constraint.set_style_id(style_id)
        constraint.set_if_type_id(if_type_id)
        constraint.set_then_type_id(then_type_id)
        return self._mapper.insert(constraint)

    def get_constraint(self, constraint_id: str) -> Optional[ImplikationConstraint]:
        return self._mapper.find_by_id(constraint_id)

    def get_constraints_by_style(self, style_id: str) -> List[ImplikationConstraint]:
        return self._mapper.find_by_style(style_id)

    def update_constraint(self, constraint: ImplikationConstraint) -> ImplikationConstraint:
        return self._mapper.update(constraint)

    def delete_constraint(self, constraint_id: str) -> bool:
        constraint = self.get_constraint(constraint_id)
        if constraint:
            self._mapper.delete(constraint)
            return True
        return False