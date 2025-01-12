from src.server.bo.BusinessObject import BusinessObject


class User (BusinessObject):

    def __init__(self):
        super().__init__()
#        self._user_id = 0
        self._lastname = ""
        self._firstname = ""
        self._nickname = ""
        self._google_id = ""
        self._email = ""

#    def get_user_id(self):
#        return self._user_id

#    def set_user_id(self, value):
#        self._user_id = value

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
        return "User: {}, {}, {}, {}".format(
            self.get_id(),
            self.get_lastname(),
            self.get_email(),
            self.get_firstname()
        )

    @staticmethod
    def from_dict(dictionary=None):
        
        if dictionary is None:
            dictionary = dict()
        obj = User()
        obj.set_id(dictionary.get("user_id", ""))
        obj.set_lastname(dictionary.get("lastname", ""))
        obj.set_firstname(dictionary.get("firstname", ""))
        obj.set_nickname(dictionary.get("nickname", ""))
        obj.set_google_id(dictionary.get("google_id", ""))
        obj.set_email(dictionary.get("email", ""))
        return obj
