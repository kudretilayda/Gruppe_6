from server.bo.BusinessObject import BusinessObject

class Wardrobe(BusinessObject):
    """Klasse für Wardrobe-Objekte."""
    def __init__(self):
        super().__init__()
        self._person_id = None
        self._owner_name = None

    def get_person_id(self):
        return self._person_id

    def set_person_id(self, value):
        self._person_id = value

    def get_owner_name(self):
        return self._owner_name

    def set_owner_name(self, value):
        self._owner_name = value

    def to_dict(self):
        result = super().to_dict()
        result.update({
            'person_id': self.get_person_id(),
            'owner_name': self.get_owner_name()
        })
        return result
