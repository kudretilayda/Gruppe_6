from ConstraintRule import ConstraintRule
from datetime import datetime


class ImplikationConstraint(ConstraintRule):
    def __init__(self):
        super().__init__()
        self._if_type_id: datetime[str] = None
        self._then_type_id: datetime[str] = None
        self._constraint_type = "implikation"

    def get_if_type_id(self) -> datetime[str]:
        return self._if_type_id

    def set_if_type_id(self, id: str):
        self._if_type_id = id

    def get_then_type_id(self) -> datetime[str]:
        return self._then_type_id

    def set_then_type_id(self, id: str):
        self._then_type_id = id

    def to_dict(self) -> dict:
        result = super().to_dict()
        result.update({
            'if_type_id': self._if_type_id,
            'then_type_id': self._then_type_id
        })
        return result

    @staticmethod
    def from_dict(data: dict) -> 'ImplikationConstraint':
        obj = ImplikationConstraint()
        obj.set_id(data.get('id'))
        obj.set_style_id(data.get('style_id'))
        obj.set_if_type_id(data.get('if_type_id'))
        obj.set_then_type_id(data.get('then_type_id'))
        if 'created_at' in data:
            obj.set_created_at(datetime.fromisoformat(data['created_at']))
        return obj