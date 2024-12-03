from server.bo.BusinessObject import BusinessObject
from datetime import datetime
from enum import Enum

class ConstraintType(Enum):
    BINARY = "binary"
    UNARY = "unary"
    IMPLIKATION = "implikation"
    MUTEX = "mutex"
    KARDINALITAET = "kardinalitaet"

class ConstraintRule(BusinessObject):
    def __init__(self):
        super().__init__()
        self._style_id: str = ""
        self._constraint_type: ConstraintType = None

    def get_style_id(self) -> str:
        return self._style_id

    def set_style_id(self, value: str):
        self._style_id = value

    def get_constraint_type(self):
        return self._constraint_type

    def set_constraint_type(self, value: ConstraintType):
        self._constraint_type = value

    def to_dict(self) -> dict:
        result = super().to_dict()
        result.update({
            'style_id': self._style_id,
            'constraint_type': self._constraint_type.value if self._constraint_type else None
        })
        return result

    @staticmethod
    def from_dict(data: dict) -> 'ConstraintRule':
        obj = ConstraintRule()
        obj.set_id(data.get('id'))
        obj.set_style_id(data.get('style_id'))
        if data.get('constraint_type'):
            obj.set_constraint_type(ConstraintType(data['constraint_type']))
        if 'created_at' in data:
            obj.set_created_at(datetime.fromisoformat(data['created_at']))
        return obj