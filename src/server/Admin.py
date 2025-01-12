# Importieren der notwendigen Mapper- und BO-Klassen
from src.server.db.UserMapper import UserMapper
from src.server.db.WardrobeMapper import WardrobeMapper
from src.server.db.ClothingItemMapper import ClothingItemMapper
from src.server.db.ClothingTypeMapper import ClothingTypeMapper
from src.server.db.StyleMapper import StyleMapper
from src.server.db.OutfitMapper import OutfitMapper

from src.server.db.ConstraintMapper.UnaryMapper import UnaryConstraintMapper
from src.server.db.ConstraintMapper.BinaryMapper import BinaryConstraintMapper
from src.server.db.ConstraintMapper.ImplicationMapper import ImplicationConstraintMapper
from src.server.db.ConstraintMapper.CardinalityMapper import CardinalityConstraintMapper
from src.server.db.ConstraintMapper.MutexMapper import MutexConstraintMapper

from src.server.bo.User import User
from src.server.bo.Wardrobe import Wardrobe
from src.server.bo.ClothingItem import ClothingItem
from src.server.bo.ClothingType import ClothingType
from src.server.bo.Style import Style
from src.server.bo.Outfit import Outfit

from src.server.bo.Constraints.Unary import UnaryConstraint
from src.server.bo.Constraints.Binary import BinaryConstraint
from src.server.bo.Constraints.Implication import ImplicationConstraint
from src.server.bo.Constraints.Cardinality import CardinalityConstraint
from src.server.bo.Constraints.Mutex import MutexConstraint

'''
Service Layer und Business Logic Layer stellen zusammen den sog. Applikationsserver dar. Er soll der
Präsentationsschicht mindestens folgende Dienste anbieten:

1) Anlegen, Editieren und Löschen von Instanzen der in Tabelle 2, S. 6 aufgeführten Klassen.

1. Style                Features, Constraints                   ✓
2. Outfit                                                       ✓
3. Kleidungstyp         Bezeichnung, Verwendung                 ✓
4. Kleidungsstück       Typ                                     ✓
5. Kleiderschrank       Eigentümer, Inhalt                      ✓
6. Person               Nachname, Vorname, Nickname, Google ID  ✓
7. Constraint                                                   ✓
8. BinaryConstraint     Bezugsobjekt 1, Bezugsobjekt 2          ✓
9. UnaryConstraint      Bezugsobjekt                            ✓
10. Implikation                                                 ✓
11. Mutex                                                       ✓
12. Kardinalität                                                ✓

2) Zuordnungen zwischen den unter Zif. 1 genannten Elementen. Für den Umgang mit Nutzerdaten soll auf 
die Google Firebase Authentication API zurückgegriffen werden.

'''
class Admin(object):
    def __init__(self):
        pass

### Person ###

    def create_user(self, firstname, lastname, nickname, email, google_id): # Methode zum Erstellen eines neuen Benutzers
        user = User()
        user.set_firstname(firstname)
        user.set_lastname(lastname)
        user.set_nickname(nickname)
        user.set_email(email)
        user.set_google_id(google_id)
        with UserMapper() as mapper:
            return mapper.insert(user) # Speichert den Benutzer in der Datenbank

    def get_all_users(self):
        with UserMapper() as mapper:
            return mapper.find_all() # Holen alle Benutzer aus der Datenbank

    def get_user_by_id(self, user_id):
        with UserMapper() as mapper:
            return mapper.find_by_key(user_id) # Sucht den Benutzer mit der übergebenen ID

    def get_user_by_google_id(self, google_id):
        with UserMapper() as mapper:
            return mapper.find_by_google_id(google_id) # Sucht den Benutzer mit der übergebenen Google-ID

    def change_user(self, user):
        with UserMapper() as mapper:
            return mapper.update(user) # Aktualisiert die Benutzerdaten in der Datenbank

    def save_user(self, user):
        with UserMapper() as mapper:
            mapper.insert(user) # Speichert den Benutzer in der Datenbank


    def delete_user(self, user):
        with UserMapper() as mapper:
            mapper.delete(user) # Löscht den Benutzer aus der Datenbank

### Kleiderschrank ###

    def create_wardrobe(self, user_id): # Erstellt einen neuen Kleiderschrank für den angegebenen Benutzer
        wardrobe = Wardrobe()
        wardrobe.set_wardrobe_owner(user_id)
        with WardrobeMapper() as mapper:
            return mapper.insert(wardrobe)

    def add_item_to_wardrobe(self, item): # Fügt ein Kleidungsstück zum Kleiderschrank hinzu
        wardrobe = Wardrobe()
        wardrobe.set_items(item)

    def get_wardrobe_by_id(self, wardrobe_id): # Sucht einen Kleiderschrank anhand seiner einzigartigen ID
        with WardrobeMapper() as mapper:
            return mapper.find_by_key(wardrobe_id)

    def get_wardrobe_by_user_id(self, user_id): # Sucht den Kleiderschrank eines bestimmten Benutzers anhand seiner Benutzer-ID
        with WardrobeMapper() as mapper:
            return mapper.find_by_person_id(user_id)

    def get_all_wardrobes(self): # Gibt eine Liste aller Kleiderschränke in der Datenbank zurück
        with WardrobeMapper() as mapper:
            return mapper.find_all()

    def save_wardrobe(self, wardrobe): # Speichert die Änderungen eines Kleiderschranks in der Datenbank
        with WardrobeMapper() as mapper:
            mapper.update(wardrobe)

    def delete_wardrobe(self, wardrobe): # Löscht einen Kleiderschrank aus der Datenbank
        with WardrobeMapper() as mapper:
            self._cleanup_reference(wardrobe)
            mapper.delete(wardrobe)
