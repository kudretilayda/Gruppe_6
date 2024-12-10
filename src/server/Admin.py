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

 
 #ClothingItem-spezifische Methoden

    def create_clothing_item(self, wardrobe_id, clothing_type_id, clothing_item_name, color=None, brand=None, season=None):
        clothing_item = ClothingItem()
        clothing_item.set_wardrobe_id(wardrobe_id)
        clothing_item.set_clothing_type_id(clothing_type_id)
        clothing_item.set_clothing_item_name(clothing_item_name)
        clothing_item.set_color(color)
        clothing_item.set_brand(brand)
        clothing_item.set_season(season)

        with ClothingItemMapper() as mapper:
            return mapper.insert(clothing_item)

    def get_clothing_item_by_id(self, clothing_item_id):
        with ClothingItemMapper() as mapper:
            return mapper.find_by_id(clothing_item_id)

    def get_clothing_items_by_wardrobe_id(self, wardrobe_id):
        with ClothingItemMapper() as mapper:
            return mapper.find_by_wardrobe_id(wardrobe_id)

    def get_all_clothing_items(self):
        with ClothingItemMapper() as mapper:
            return mapper.find_all()

    def save_clothing_item(self, clothing_item):
        with ClothingItemMapper() as mapper:
            mapper.update(clothing_item)

    def delete_clothing_item(self, clothing_item):
        with ClothingItemMapper() as mapper:
            # Erst alle Referenzen auf ClothingItem löschen (Outfits)
            self._cleanup_clothing_item_references(clothing_item)
            mapper.delete(clothing_item)

#ClothingType-spezifische Methoden

    def create_clothing_type(self, type_name, type_usage):
        clothing_type = ClothingType()
        clothing_type.set_type_name(type_name)
        clothing_type.set_type_usage(type_usage)

        with ClothingTypeMapper() as mapper:
            return mapper.insert(clothing_type)

    def get_clothing_type_by_id(self, clothing_type_id):
        with ClothingTypeMapper() as mapper:
            return mapper.find_by_id(clothing_type_id)

    def get_all_clothing_types(self):
        with ClothingTypeMapper() as mapper:
            return mapper.find_all()
        
#Style-spezifische Methoden
    
    def create_style(self, style_features, style_constraints):
        style = Style()
        style.set_style_features(style_features)
        style.set_style_constraints(style_constraints)

        with StyleMapper() as mapper:
            return mapper.insert(style)

    def get_style_by_id(self, style_id):
        with StyleMapper() as mapper:
            return mapper.find_by_id(style_id)

    def get_all_styles(self):
        with StyleMapper() as mapper:
            return mapper.find_all()

    def save_style(self, style):
        with StyleMapper() as mapper:
            mapper.update(style)

    def delete_style(self, style):
        with StyleMapper() as mapper:
            # Erst alle Referenzen auf Style löschen (Outfits, Constraints)
            self._cleanup_style_references(style)
            mapper.delete(style)


#Outfit-spezifische Methoden
    
    def create_outfit(self, outfit_name, style_id):
        outfit = Outfit()
        outfit.set_outfit_name(outfit_name)
        outfit.set_style_id(style_id)

        with OutfitMapper() as mapper:
            return mapper.insert(outfit)

    def add_item_to_outfit(self, outfit_id, clothing_item_id):
        with OutfitMapper() as mapper:
            mapper.add_item_to_outfit(outfit_id, clothing_item_id)

    def remove_item_from_outfit(self, outfit_id, clothing_item_id):
        with OutfitMapper() as mapper:
            mapper.remove_item_from_outfit(outfit_id, clothing_item_id)

    def get_outfit_by_id(self, outfit_id):
        with OutfitMapper() as mapper:
            return mapper.find_by_id(outfit_id)

    def get_outfits_by_style_id(self, style_id):
        with OutfitMapper() as mapper:
            return mapper.find_by_style_id(style_id)

    def get_all_outfits(self):
        with OutfitMapper() as mapper:
            return mapper.find_all()

    def save_outfit(self, outfit):
        with OutfitMapper() as mapper:
            mapper.update(outfit)

    def delete_outfit(self, outfit):
        with OutfitMapper() as mapper:
            mapper.delete(outfit)

