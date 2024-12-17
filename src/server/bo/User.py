from src.server.bo.BusinessObject import BusinessObject


class User (BusinessObject):

    def __init__(self):
        super().__init__()
        self.__user_id = 0
        self.__lastname = ""
        self.__firstname = ""
        self.__nickname = ""
        self.__google_id = ""
        self.__email = ""

    def get_user_id(self):
        return self.__user_id

    def set_user_id(self, value):
        self.__user_id = value

    def get_lastname(self):
        return self.__lastname

    def set_lastname(self, lastname):
        self.__lastname = lastname

    def get_firstname(self):
        return self.__firstname

    def set_firstname(self, firstname):
        self.__firstname = firstname

    def get_nickname(self):
        return self.__nickname

    def set_nickname(self, value):
        self.__nickname = value

    def get_google_id(self):
        return self.__google_id

    def set_google_id(self, value):
        self.__google_id = value

    def get_email(self):
        return self.__email

    def set_email(self, value):
        self.__email = value

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
