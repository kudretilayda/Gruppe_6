from server.bo.BusinessObject import BusinessObject
from datetime import datetime

class Wardrobe(BusinessObject):
    def __init__(self):
        super().__init__()
        self._person_id: str = ""
        self._owner_name = None

    def get_person_id(self) -> str:
        return self._person_id

    def set_person_id(self, value: str):
        self._person_id = value

    def get_owner_name(self):
        return self._owner_name

    def set_owner_name(self, value):
        self._owner_name = value

    def to_dict(self) -> dict:
        result = super().to_dict()
        result.update({
            'person_id': self._person_id,
            'owner_name': self._owner_name
        })
        return result

    @staticmethod
    def from_dict(data: dict) -> 'Wardrobe':
        obj = Wardrobe()
        obj.set_id(data.get('id'))
        obj.set_person_id(data.get('person_id'))
        obj.set_owner_name(data.get('owner_name'))
        if 'created_at' in data:
            obj.set_created_at(datetime.fromisoformat(data['created_at']))
        return obj
