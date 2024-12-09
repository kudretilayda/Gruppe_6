from server.bo.BusinessObject import BusinessObject
from datetime import datetime


class Outfit(BusinessObject):
    """Klasse für Outfit-Objekte."""
    def __init__(self):
        super().__init__()
        self._name = None
        self._style_id = None
        self._created_by = None
        self._items = []  # Liste von Kleidungsstück-IDs

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def get_style_id(self):
        return self._style_id

    def set_style_id(self, value):
        self._style_id = value

    def get_created_by(self):
        return self._created_by

    def set_created_by(self, value):
        self._created_by = value

    def get_items(self):
        return self._items

    def set_items(self, items):
        self._items = items

    def add_item(self, item_id):
        if item_id not in self._items:
            self._items.append(item_id)

    def remove_item(self, item_id):
        if item_id in self._items:
            self._items.remove(item_id)

    def to_dict(self):
        result = super().to_dict()
        result.update({
            'name': self.get_name(),
            'style_id': self.get_style_id(),
            'created_by': self.get_created_by(),
            'items': self.get_items()
        })
        return result
     
    @staticmethod
    def from_dict(data: dict) -> 'Outfit':
        obj = Outfit()
        obj.set_id(data.get('id'))
        obj.set_outfit_name(data.get('outfit_name'))
        obj.set_style_id(data.get('style_id'))
        obj.set_created_by(data.get('created_by'))
        obj.set_items(data.get('items', []))
        if 'created_at' in data:
            obj.set_created_at(datetime.fromisoformat(data['created_at']))
        return obj