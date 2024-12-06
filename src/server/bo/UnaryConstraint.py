from server.bo.ConstraintRule import ConstraintRule
from datetime import datetime


class UnaryConstraint(ConstraintRule):
    def __init__(self):
        super().__init__()
        self._reference_object_id: datetime[str] = None
        self._constraint_type = "unary"

    def get_reference_object_id(self) -> datetime[str]:
        return self._reference_object_id

    def set_reference_object_id(self, id: str):
        self._reference_object_id = id

    def to_dict(self) -> dict:
        result = super().to_dict()
        result.update({
            'reference_object_id': self._reference_object_id
        })
        return result

    @staticmethod
    def from_dict(data: dict) -> 'UnaryConstraint':
        obj = UnaryConstraint()
        obj.set_id(data.get('id'))
        obj.set_style_id(data.get('style_id'))
        obj.set_reference_object_id(data.get('reference_object_id'))
        if 'created_at' in data:
            obj.set_created_at(datetime.fromisoformat(data['created_at']))
        return obj