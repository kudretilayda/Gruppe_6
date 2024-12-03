from server.bo.BusinessObject import BusinessObject



class User(BusinessObject):
    """Klasse für Person-Objekte."""
    def __init__(self):
        super().__init__()
        self._google_id = " "
        self._first_name = " "
        self._last_name = " "
        self._nick_name = None
        self._email = " "

    def get_google_id(self):
        """Gibt Google ID des Users zurück"""
        return self._google_id

    def set_google_id(self, value):
        """Setzt Google ID des Users"""
        self._google_id = value

    def get_firstname(self):
        """Gibt den Vornamen des Users zurück"""
        return self._firstname

    def set_firstname(self, value):
        """Setzt den Vornamen des Users"""
        self._firstname = value

    def get_lastname(self):
        """Gibt den Nachnamen des Users zurück"""
        return self._lastname

    def set_lastname(self, value):
        """Setzt den Nachnamen des Users"""
        self._lastname = value

    def get_nickname(self):
        """Gibt den Nickname des Users zurück"""
        return self._nickname

    def set_nickname(self, value):
        """Setzt den Nickname des Users"""
        self._nickname = value

    def __str__(self):
        """Erzeugen einer einfachen textuellen Darstellung der jeweiligen Instanz"""
        return "User: {}, {}, {}, {},{},{}".format(self.get_id(), self._google_user_id, self._first_name, self._last_name, self._nickname, self._email)
    
    
   
    @staticmethod
    def from_dict(dictionary=dict()):
        obj = User()
        obj.set_id(dictionary["id"]) #Setzt die ID des Users aus dem Dictionary
        obj.set_google_user_id(dictionary["google_user_id"]) #Setzt die Google User ID aus dem Dictionary
        obj.set_nick_name(dictionary["nick_name"]) #Setzt den Nickname aus dem Dictionary
        obj.set_first_name(dictionary["first_name"]) #Setzt den Vornamen aus dem Dictionary
        obj.set_last_name(dictionary["last_name"]) #Setzt den Nachnamen aus dem Dictionary
        return obj