from server.bo.ConstraintRule import ConstraintRule
from server.bo.UnaryConstraint import UnaryConstraint
from datetime import datetime


class Kardinalitaet(ConstraintRule):
    def __init__(self):
        super().__init__()
        self._clothing_type_id: str = ""
        self._min_count: int = 0
        self._max_count: int = 0

    def get_clothing_type_id(self) -> str:
        return self._clothing_type_id

    def set_clothing_type_id(self, value: str):
        self._clothing_type_id = value

    def get_min_count(self) -> int:
        return self._min_count

    def set_min_count(self, value: int):
        self._min_count = value

    def get_max_count(self) -> int:
        return self._max_count

    def set_max_count(self, value: int):
        self._max_count = value

    def to_dict(self) -> dict:
        result = super().to_dict()
        result.update({
            'clothing_type_id': self._clothing_type_id,
            'min_count': self._min_count,
            'max_count': self._max_count
        })
        return result

    @staticmethod
    def from_dict(data: dict) -> 'Kardinalitaet':
        obj = Kardinalitaet()
        obj.set_id(data.get('id'))
        obj.set_style_id(data.get('style_id'))
        obj.set_clothing_type_id(data.get('clothing_type_id'))
        obj.set_min_count(data.get('min_count', 0))
        obj.set_max_count(data.get('max_count', 0))
        if data.get('constraint_type'):
            obj.set_constraint_type(ConstraintRule(data['constraint_type']))
        if 'created_at' in data:
            obj.set_created_at(datetime.fromisoformat(data['created_at']))
        return obj