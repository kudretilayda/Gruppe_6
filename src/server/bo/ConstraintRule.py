from server.bo.BusinessObject import BusinessObject
from datetime import datetime

class Constraint(BusinessObject):
    def __init__(self):
        super().__init__()
        self._style_id: datetime[str] = None
        self._constraint_type: str = ""

    def get_style_id(self) -> datetime[str]:
        return self._style_id

    def set_style_id(self, style_id: str):
        self._style_id = style_id

    def get_constraint_type(self) -> str:
        return self._constraint_type

    def set_constraint_type(self, constraint_type: str):
        self._constraint_type = constraint_type

    def to_dict(self) -> dict:
        result = super().to_dict()
        result.update({
            'style_id': self._style_id,
            'constraint_type': self._constraint_type
        })
        return result

    @staticmethod
    def from_dict(data: dict) -> 'Constraint':
        obj = Constraint()
        obj.set_id(data.get('id'))
        obj.set_style_id(data.get('style_id'))
        obj.set_constraint_type(data.get('constraint_type'))
        if 'created_at' in data:
            obj.set_created_at(datetime.fromisoformat(data['created_at']))
        return obj