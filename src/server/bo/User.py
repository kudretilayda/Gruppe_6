from .BusinessObject import BusinessObject

class User(BusinessObject):
    """Klasse für Person-Objekte.
    
    Eine Person verfügt über eine Google ID, Vor- und Nachnamen sowie optional einen Nickname.
    """

    def __init__(self):
        super().__init__()
        self._google_id = ""
        self._firstname = ""
        self._lastname = ""
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