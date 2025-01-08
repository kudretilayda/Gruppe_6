from .BusinessObject import BusinessObject


class User (BusinessObject):

    def __init__(self):
        super().__init__()
        self._user_id = 0
        self._lastname = ""
        self._firstname = ""
        self._nickname = ""
        self._google_id = ""
        self._email = ""

    def get_user_id(self):
        return self._user_id

    def set_user_id(self, value):
        self._user_id = value

    def get_lastname(self):
        return self._lastname

    def set_lastname(self, lastname):
        self._lastname = lastname

    def get_firstname(self):
        return self._firstname

    def set_firstname(self, firstname):
        self._firstname = firstname

    def get_nickname(self):
        return self._nickname

    def set_nickname(self, value):
        self._nickname = value

    def get_google_id(self):
        return self._google_id

    def set_google_id(self, value):
        self._google_id = value

    def get_email(self):
        return self._email

    def set_email(self, value):
        self._email = value

    def __str__(self):
        return "User: {}, {}, {}, {}".format(self.get_user_id(), self.get_lastname(), self.get_email(), self.get_firstname())

    @staticmethod
    def from_dict(dictionary=dict()):
        obj = User()
        obj.set_user_id(dictionary("user_id", ""))
        obj.set_lastname(dictionary("lastname", ""))
        obj.set_firstname(dictionary("firstname", ""))
        obj.set_nickname(dictionary("nickname", ""))
        obj.set_google_id(dictionary("google_id", ""))
        obj.set_email(dictionary("email", ""))
        return obj
