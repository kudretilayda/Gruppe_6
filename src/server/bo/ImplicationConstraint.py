from ConstraintRule import ConstraintRule
from datetime import datetime


class Implikation(ConstraintRule):
    def __init__(self):
        super().__init__()
        self._if_clothing_type_id: str = ""
        self._then_clothing_type_id: str = ""

    def get_if_clothing_type_id(self) -> str:
        return self._if_clothing_type_id

    def set_if_clothing_type_id(self, value: str):
        self._if_clothing_type_id = value

    def get_then_clothing_type_id(self) -> str:
        return self._then_clothing_type_id

    def set_then_clothing_type_id(self, value: str):
        self._then_clothing_type_id = value

    def to_dict(self) -> dict:
        result = super().to_dict()
        result.update({
            'if_clothing_type_id': self._if_clothing_type_id,
            'then_clothing_type_id': self._then_clothing_type_id
        })
        return result

    @staticmethod
    def from_dict(data: dict) -> 'Implikation':
        obj = Implikation()
        obj.set_id(data.get('id'))
        obj.set_style_id(data.get('style_id'))
        obj.set_if_clothing_type_id(data.get('if_clothing_type_id'))
        obj.set_then_clothing_type_id(data.get('then_clothing_type_id'))
        if data.get('constraint_type'):
            obj.set_constraint_type(ConstraintRule(data['constraint_type']))
        if 'created_at' in data:
            obj.set_created_at(datetime.fromisoformat(data['created_at']))
        return obj