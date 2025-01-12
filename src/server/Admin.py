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

### Kleidungsstück ###

    def create_clothing_item(self, wardrobe_id, clothing_type_id, item_name): # Hier wird ein neues Kleidungsstück mit allen nötigen Informationen erstellt
        clothing_item = ClothingItem()
        clothing_item.set_wardrobe_id(wardrobe_id)
        clothing_item.set_clothing_type(clothing_type_id)
        clothing_item.set_item_name(item_name)

        with ClothingItemMapper() as mapper:
            return mapper.insert(clothing_item) # Das Kleidungsstück wird in der Datenbank gespeichert

    def get_all_clothing_items(self): # Holt eine Liste aller Kleidungsstücke
        with ClothingItemMapper() as mapper:
            return mapper.find_all()

    def get_clothing_item_by_id(self, clothing_item_id): # Holt ein bestimmtes Kleidungsstück anhand seiner ID
        with ClothingItemMapper() as mapper:
            return mapper.find_by_key(clothing_item_id)

    def get_clothing_items_by_wardrobe_id(self, wardrobe_id): # Holt alle Kleidungsstücke aus einem bestimmten Kleiderschrank
        with ClothingItemMapper() as mapper:
            return mapper.find_by_wardrobe_id(wardrobe_id)

    def save_clothing_item(self, clothing_item): # Speichert alle Änderungen an einem Kleidungsstück
        with ClothingItemMapper() as mapper:
            mapper.update(clothing_item)

    def delete_clothing_item(self, clothing_item): # löscht ein Kleidungsstück
        with ClothingItemMapper() as mapper:
            self._cleanup_reference(clothing_item)
            mapper.delete(clothing_item)

### Outfit ###

    def create_outfit(self, outfit_name, style_id): # Hier wird ein neues Outfit erstellt
        outfit = Outfit()
        outfit.set_outfit_name(outfit_name)
        outfit.set_style(style_id)

        with OutfitMapper() as mapper:
            return mapper.insert(outfit)

    def add_item_to_outfit(self, outfit_id, item): # Fügt ein Kleidungsstück zu einem bestimmten Outfit hinzu
        outfit = Outfit()
        outfit.set_items(item)
        with OutfitMapper() as mapper:
            mapper.add_item_to_outfit(outfit_id, item)

    def remove_item_from_outfit(self, outfit_id, item): # Entfernt ein Kleidungsstück aus einem bestimmten Outfit
        with OutfitMapper() as mapper:
            mapper.remove_item_from_outfit(outfit_id, item)

    def get_outfit_by_id(self, outfit_id): # Holt ein Outfit anhand seiner ID
        with OutfitMapper() as mapper:
            return mapper.find_by_id(outfit_id)

    def get_outfits_by_style_id(self, style_id): # Holt alle Outfits, die einem bestimmten Style zugeordnet sind
        with OutfitMapper() as mapper:
            return mapper.find_by_style_id(style_id)

    def get_all_outfits(self): # Holt alle Outfits
        with OutfitMapper() as mapper:
            return mapper.find_all()

    def save_outfit(self, outfit):
        with OutfitMapper() as mapper: # Speichert Änderungen an einem Outfit
            mapper.update(outfit)

    def delete_outfit(self, outfit):
        with OutfitMapper() as mapper: # Löscht ein Outfit
            mapper.delete(outfit)

### Style ###

    def create_style(self, style_features, style_constraints): # Hier wird ein neuer Style erstellt
        style = Style()
        style.set_style_features(style_features)
        style.set_style_constraints(style_constraints)

        with StyleMapper() as mapper:
            return mapper.insert(style)

    def get_style_by_id(self, style_id): # Holt einen Style anhand seiner ID
        with StyleMapper() as mapper:
            return mapper.find_by_id(style_id)

    def get_all_styles(self): # Holt alle Styles
        with StyleMapper() as mapper:
            return mapper.find_all()

    def save_style(self, style): # Speichert Änderungen an einem bestimmten Style
        with StyleMapper() as mapper:
            mapper.update(style)

    def delete_style(self, style): # Löscht ein Style
        with StyleMapper() as mapper:
            self._cleanup_reference(style)
            mapper.delete(style)
