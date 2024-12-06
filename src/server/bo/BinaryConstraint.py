from server.bo.ConstraintRule import ConstraintRule
from datetime import datetime


class BinaryConstraint(ConstraintRule):
    def __init__(self):
        super().__init__()
        self._reference_object1_id: datetime[str] = None
        self._reference_object2_id: datetime[str] = None
        self._constraint_type = "binary"

    def get_reference_object1_id(self) -> datetime[str]:
        return self._reference_object1_id

    def set_reference_object1_id(self, id: str):
        self._reference_object1_id = id

    def get_reference_object2_id(self) -> datetime[str]:
        return self._reference_object2_id

    def set_reference_object2_id(self, id: str):
        self._reference_object2_id = id

    def to_dict(self) -> dict:
        result = super().to_dict()
        result.update({
            'reference_object1_id': self._reference_object1_id,
            'reference_object2_id': self._reference_object2_id
        })
        return result

    @staticmethod
    def from_dict(data: dict) -> 'BinaryConstraint':
        obj = BinaryConstraint()
        obj.set_id(data.get('id'))
        obj.set_style_id(data.get('style_id'))
        obj.set_reference_object1_id(data.get('reference_object1_id'))
        obj.set_reference_object2_id(data.get('reference_object2_id'))
        if 'created_at' in data:
            obj.set_created_at(datetime.fromisoformat(data['created_at']))
        return obj