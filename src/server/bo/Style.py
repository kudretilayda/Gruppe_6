from server.bo.BusinessObject import BusinessObject
from datetime import datetime


class Style(BusinessObject):
    def __init__(self):
        super().__init__()
        self._style_name: str = ""
        self._style_description = None
        self._created_by: str = ""

    def get_style_name(self) -> str:
        return self._style_name

    def set_style_name(self, value: str):
        self._style_name = value

    def get_style_description(self):
        return self._style_description

    def set_style_description(self, value):
        self._style_description = value

    def get_created_by(self):
        return self._created_by

    def set_created_by(self, value: str):
        self._created_by = value

    def to_dict(self) -> dict:
        result = super().to_dict()
        result.update({
            'style_name': self._style_name,
            'style_description': self._style_description,
            'created_by': self._created_by
        })
        return result

    @staticmethod
    def from_dict(data: dict) -> 'Style':
        obj = Style()
        obj.set_id(data.get('id'))
        obj.set_style_name(data.get('style_name'))
        obj.set_style_description(data.get('style_description'))
        obj.set_created_by(data.get('created_by'))
        if 'created_at' in data:
            obj.set_created_at(datetime.fromisoformat(data['created_at']))
        return obj