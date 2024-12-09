from server.db.UserMapper import UserMapper
from server.db.WardrobeMapper import WardrobeMapper
from server.db.ClothingItemMapper import ClothingItemMapper
from server.db.ClothingTypeMapper import ClothingTypeMapper
from server.db.StyleMapper import StyleMapper
from server.db.OutfitMapper import OutfitMapper
#from server.db.ConstraintMapper import ConstraintMapper
from server.bo.User import Person
from server.bo.Wardrobe import Wardrobe
from server.bo.ClothingItem import ClothingItem
from server.bo.ClothingType import ClothingType
from server.bo.Style import Style
from server.bo.Outfit import Outfit
#from server.bo.Constraint import Constraint, BinaryConstraint, UnaryConstraint, CardinalityConstraint, MutexConstraint, ImplicationConstraint


class Administration(object):
    """Diese Klasse aggregiert nahezu sämtliche Applikationslogik (engl. Business Logic).
    Sie ist wie eine Spinne, die sämtliche Zusammenhänge in ihrem Netz (in unserem
    Fall die Daten der Applikation) überblickt und für einen geordneten Ablauf und
    dauerhafte Konsistenz der Daten und Abläufe sorgt.
    Die Applikationslogik findet sich in den Methoden dieser Klasse. Jede dieser
    Methoden kann als *Transaction Script* bezeichnet werden. Dieser Name
    lässt schon vermuten, dass hier analog zu Datenbanktransaktion pro
    Transaktion gleiche mehrere Teilaktionen durchgeführt werden, die das System
    von einem konsistenten Zustand in einen anderen, auch wieder konsistenten
    Zustand überführen. Wenn dies zwischenzeitig scheitern sollte, dann ist das
    jeweilige Transaction Script dafür verwantwortlich, eine Fehlerbehandlung
    durchzuführen.
    Diese Klasse steht mit einer Reihe weiterer Datentypen in Verbindung. Diese
    sind:
    - die Klassen BusinessObject und deren Subklassen,
    - die Mapper-Klassen für den DB-Zugriff."""

    def __init__(self):
        pass

#### User-spezifische Methoden ####
   
    def create_user(self, user_id, google_id, vorname="", nachname="", nickname="", email=""):
        user = user()
        user.set_user_id(user_id)
        user.set_google_id(google_id)
        user.set_vorname(vorname)
        user.set_nachname(nachname)
        user.set_nickname(nickname)
        user.set_email(email)

        with UserMapper() as mapper:
            return mapper.insert(user)
    
  
    

    def get_user_by_id(self, number):
        """Den User mit gegebener ID ausgeben."""
        with UserMapper() as mapper:
            return mapper.find_by_id(number)

    def get_user_by_google_id(self, id):
        """Den User mit der gegebenen google_id ausgeben."""
        with UserMapper() as mapper:
            return mapper.find_user_by_google_id(id)

    def get_user_by_vorname(self, vorname):
        """Alle User mit dem Vornamen auslesen."""
        with UserMapper() as mapper:
            return mapper.find_user_by_vorname(vorname)

    def get_user_by_nachname(self, nachname):
        """Alle User mit dem Nachnamen auslesen."""
        with UserMapper() as mapper:
            return mapper.find_user_by_nachname(nachname)

    def get_user_by_nickname(self, nickname):
        """Alle User mit dem Nickname auslesen."""
        with UserMapper() as mapper:
            return mapper.find_user_by_nickname(nickname)

    def get_user_by_email(self, email):
        """Alle User mit gegebener E-Mail-Adresse auslesen."""
        with UserMapper() as mapper:
            return mapper.find_user_by_email(email)

    def get_all_users(self):
        """Alle User ausgeben."""
        with UserMapper() as mapper:
            return mapper.find_all()
    
    def change_user(self, user):
        """Den gegebenen User speichern."""
        with UserMapper() as mapper:
            return mapper.update(user)
    
    def save_user(self, user):
        """Den gegebenen Benutzer speichern."""
        with UserMapper() as mapper:
            mapper.update(user)

    def delete_user(self, user):
        """Den gegebenen Benutzer aus unserem System löschen."""
        with UserMapper() as mapper:
            mapper.delete(user)

###Wardrobe spezifische Methoden###

    def create_wardrobe(self, user_id):
        wardrobe = Wardrobe()
        wardrobe.set_user_id(user_id)

        with WardrobeMapper() as mapper:
            return mapper.insert(wardrobe)

    def get_wardrobe_by_id(self, wardrobe_id):
        with WardrobeMapper() as mapper:
            return mapper.find_by_id(wardrobe_id)

    def get_wardrobe_by_person_id(self, user_id):
        with WardrobeMapper() as mapper:
            return mapper.find_by_user_id(user_id)

    def get_all_wardrobes(self):
        with WardrobeMapper() as mapper:
            return mapper.find_all()

    def save_wardrobe(self, wardrobe):
        with WardrobeMapper() as mapper:
            mapper.update(wardrobe)

    def delete_wardrobe(self, wardrobe):
        with WardrobeMapper() as mapper:
            self._cleanup_wardrobe_references(wardrobe)
            mapper.delete(wardrobe)


