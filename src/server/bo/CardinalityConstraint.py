from server.bo.ConstraintRule import ConstraintRule
from datetime import datetime
from typing import Optional

class KardinalitaetConstraint(ConstraintRule):
    def __init__(self):
        super().__init__()
        self._clothing_type_id: datetime[str] = None
        self._min_count: int = 0
        self._max_count: int = 0
        self._constraint_type = "kardinalitaet"

    def get_clothing_type_id(self) -> datetime[str]:
        return self._clothing_type_id

    def set_clothing_type_id(self, type_id: str):
        self._clothing_type_id = type_id

    def get_min_count(self) -> int:
        return self._min_count

    def set_min_count(self, count: int):
        self._min_count = count

    def get_max_count(self) -> int:
        return self._max_count

    def set_max_count(self, count: int):
        self._max_count = count

    def to_dict(self) -> dict:
        result = super().to_dict()
        result.update({
            'clothing_type_id': self._clothing_type_id,
            'min_count': self._min_count,
            'max_count': self._max_count
        })
        return result

    @staticmethod
    def from_dict(data: dict) -> 'KardinalitaetConstraint':
        obj = KardinalitaetConstraint()
        obj.set_id(data.get('id'))
        obj.set_style_id(data.get('style_id'))
        obj.set_clothing_type_id(data.get('clothing_type_id'))
        obj.set_min_count(data.get('min_count', 0))
        obj.set_max_count(data.get('max_count', 0))
        if 'created_at' in data:
            obj.set_created_at(datetime.fromisoformat(data['created_at']))
        return obj