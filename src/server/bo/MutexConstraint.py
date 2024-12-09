from server.bo.ConstraintRule import ConstraintRule
from datetime import datetime

class MutexConstraint(ConstraintRule):
    def __init__(self):
        super().__init__()
        self._excluded_types: list[str] = []
        self._constraint_type = "mutex"

    def get_excluded_types(self) -> list[str]:
        return self._excluded_types

    def set_excluded_types(self, types: list[str]):
        self._excluded_types = types

    def add_excluded_type(self, type_id: str):
        if type_id not in self._excluded_types:
            self._excluded_types.append(type_id)

    def to_dict(self) -> dict:
        result = super().to_dict()
        result.update({
            'excluded_types': self._excluded_types
        })
        return result

    @staticmethod
    def from_dict(data: dict) -> 'MutexConstraint':
        obj = MutexConstraint()
        obj.set_id(data.get('id'))
        obj.set_style_id(data.get('style_id'))
        obj.set_excluded_types(data.get('excluded_types', []))
        if 'created_at' in data:
            obj.set_created_at(datetime.fromisoformat(data['created_at']))
        return obj