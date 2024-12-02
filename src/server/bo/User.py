from server.bo.BusinessObject import BusinessObject


class Person(BusinessObject):
    """Klasse für Person-Objekte."""
    def __init__(self):
        super().__init__()
        self._google_id = None
        self._firstname = None
        self._lastname = None
        self._nickname = None

    def get_google_id(self):
        return self._google_id

    def set_google_id(self, value):
        self._google_id = value

    def get_firstname(self):
        return self._firstname

    def set_firstname(self, value):
        self._firstname = value

    def get_lastname(self):
        return self._lastname

    def set_lastname(self, value):
        self._lastname = value

    def get_nickname(self):
        return self._nickname

    def set_nickname(self, value):
        self._nickname = value

    def to_dict(self):
        result = super().to_dict()
        result.update({
            'google_id': self.get_google_id(),
            'firstname': self.get_firstname(),
            'lastname': self.get_lastname(),
            'nickname': self.get_nickname()
        })
        return result