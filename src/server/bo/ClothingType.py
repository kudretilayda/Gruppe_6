from server.bo.BusinessObject import BusinessObject
from datetime import datetime
from enum import Enum

class Category(Enum):
    OBERTEILE = "oberteile"
    UNTERTEILE = "unterteile"
    SCHUHE = "schuhe"

class ClothingType(BusinessObject):
    def __init__(self):
        super().__init__()
        self._type_name: str = ""
        self._type_description = None
        self._category: Category = None

    def get_type_name(self) -> str:
        return self._type_name

    def set_type_name(self, value: str):
        self._type_name = value

    def get_type_description(self):
        return self._type_description

    def set_type_description(self, value):
        self._type_description = value

    def get_category(self) -> Category:
        return self._category

    def set_category(self, value: Category):
        self._category = value

    def to_dict(self) -> dict:
        result = super().to_dict()
        result.update({
            'type_name': self._type_name,
            'type_description': self._type_description,
            'category': self._category.value if self._category else None
        })
        return result

    @staticmethod
    def from_dict(data: dict) -> 'ClothingType':
        obj = ClothingType()
        obj.set_id(data.get('id'))
        obj.set_type_name(data.get('type_name'))
        obj.set_type_description(data.get('type_description'))
        if data.get('category'):
            obj.set_category(Category(data['category']))
        if 'created_at' in data:
            obj.set_created_at(datetime.fromisoformat(data['created_at']))
        return obj