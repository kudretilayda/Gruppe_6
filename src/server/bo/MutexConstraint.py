from server.bo.ConstraintRule import ConstraintRule
from datetime import datetime
from ConstraintRule import ConstraintRule


class Mutex(ConstraintRule):

    def __init__(self):
        super().__init__()
        self._excluded_types = []  # List of clothing_type_ids that are mutually exclusive

    def get_excluded_types(self):
        return self._excluded_types

    def set_excluded_types(self, value):
        self._excluded_types = value

    def add_excluded_type(self, type_id: str):
        if type_id not in self._excluded_types:
            self._excluded_types.append(type_id)

    def remove_excluded_type(self, type_id: str):
        if type_id in self._excluded_types:
            self._excluded_types.remove(type_id)

    def to_dict(self) -> dict:
        result = super().to_dict()
        result.update({
            'excluded_types': self._excluded_types
        })
        return result

    @staticmethod
    def from_dict(data: dict) -> 'Mutex':
        obj = Mutex()
        obj.set_id(data.get('id'))
        obj.set_style_id(data.get('style_id'))
        obj.set_excluded_types(data.get('excluded_types', []))
        if data.get('constraint_type'):
            obj.set_constraint_type(ConstraintRule(data['constraint_type']))
        if 'created_at' in data:
            obj.set_created_at(datetime.fromisoformat(data['created_at']))
        return obj