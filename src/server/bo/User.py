from server.bo import BusinessObject as bo

class User(bo.BusinessObject):
    def __init__(self):
        super().__init__()
        self.__user_id = ""
        self.__nachname = ""
        self.__vorname = ""
        self.__nickname = ""
        self.__google_id = ""
        self.__email = ""

    # Properties für Attribute
    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, value):
        self.__user_id = value

    @property
    def nachname(self):
        return self.__nachname

    @nachname.setter
    def nachname(self, value):
        self.__nachname = value

    @property
    def vorname(self):
        return self.__vorname

    @vorname.setter
    def vorname(self, value):
        self.__vorname = value

    @property
    def nickname(self):
        return self.__nickname

    @nickname.setter
    def nickname(self, value):
        self.__nickname = value

    @property
    def google_id(self):
        return self.__google_id

    @google_id.setter
    def google_id(self, value):
        self.__google_id = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    # String-Repräsentation
    def __str__(self):
        return f"User: {self.user_id}, {self.nachname}, {self.email}, {self.vorname}"

    # Statische Methode zum Erstellen eines User-Objekts aus einem Dictionary
    @staticmethod
    def from_dict(dictionary=dict()):
        obj = User()
        obj.user_id = dictionary.get("user_id", "")
        obj.nachname = dictionary.get("nachname", "")
        obj.vorname = dictionary.get("vorname", "")
        obj.nickname = dictionary.get("nickname", "")
        obj.google_id = dictionary.get("google_id", "")
        obj.email = dictionary.get("email", "")
        return obj