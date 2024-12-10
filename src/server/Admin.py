from server.db.UserMapper import UserMapper
from server.db.WardrobeMapper import WardrobeMapper
from server.db.ClothingItemMapper import ClothingItemMapper
from server.db.ClothingTypeMapper import ClothingTypeMapper
from server.db.StyleMapper import StyleMapper
from server.db.OutfitMapper import OutfitMapper
from server.db.ConstraintMapper import ConstraintMapper
from server.bo.User import Person
from server.bo.Wardrobe import Wardrobe
from server.bo.ClothingItem import ClothingItem
from server.bo.ClothingType import ClothingType
from server.bo.Style import Style
from server.bo.Outfit import Outfit
from server.constraints.Constraint import Constraint, BinaryConstraint, UnaryConstraint, CardinalityConstraint, MutexConstraint, ImplicationConstraint


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

### Wardrobe spezifische Methoden ###

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

 
 ### ClothingItem-spezifische Methoden ###

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

### ClothingType-spezifische Methoden ###

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
        
### Style-spezifische Methoden ###
    
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


### Outfit-spezifische Methoden ###
    
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

### Constraint-spezifische Methoden ###
    
    def create_constraint(self, style_id, constraint_type, attribute=None, constrain=None, val=None):
        constraint = constraint()
        constraint.set_style_id(style_id)
        constraint.set_constraint_type(constraint_type)
        constraint.set_attribute(attribute)
        constraint.set_constrain(constrain)
        constraint.set_val(val)

        with ConstraintMapper() as mapper:
            return mapper.insert(constraint)

    def create_binary_constraint(self, style_id, reference_object1_id, reference_object2_id):
        binary_constraint = BinaryConstraint()
        binary_constraint.set_style_id(style_id)
        binary_constraint.set_reference_object1_id(reference_object1_id)
        binary_constraint.set_reference_object2_id(reference_object2_id)

        with ConstraintMapper() as mapper:
            return mapper.insert(binary_constraint)

    def create_unary_constraint(self, style_id, reference_object_id, attribute, constrain, val):
        unary_constraint = UnaryConstraint()
        unary_constraint.set_style_id(style_id)
        unary_constraint.set_reference_object_id(reference_object_id)
        unary_constraint.set_attribute(attribute)
        unary_constraint.set_constrain(constrain)
        unary_constraint.set_val(val)

        with ConstraintMapper() as mapper:
            return mapper.insert(unary_constraint)

    def create_cardinality_constraint(self, style_id, item_type, min_count, max_count):
        cardinality_constraint = CardinalityConstraint()
        cardinality_constraint.set_style_id(style_id)
        cardinality_constraint.set_item_type(item_type)
        cardinality_constraint.set_min_count(min_count)
        cardinality_constraint.set_max_count(max_count)

        with ConstraintMapper() as mapper:
            return mapper.insert(cardinality_constraint)

    def create_mutex_constraint(self, style_id, item_type_1, item_type_2):
        mutex_constraint = MutexConstraint()
        mutex_constraint.set_style_id(style_id)
        mutex_constraint.set_item_type_1(item_type_1)
        mutex_constraint.set_item_type_2(item_type_2)

        with ConstraintMapper() as mapper:
            return mapper.insert(mutex_constraint)

    def create_implication_constraint(self, style_id, if_type, then_type):
        implication_constraint = ImplicationConstraint()
        implication_constraint.set_style_id(style_id)
        implication_constraint.set_if_type(if_type)
        implication_constraint.set_then_type(then_type)

        with ConstraintMapper() as mapper:
            return mapper.insert(implication_constraint)

    def get_constraints_by_style(self, style_id):
        with ConstraintMapper() as mapper:
            return mapper.find_by_style_id(style_id)

    def get_all_constraints(self):
        with ConstraintMapper() as mapper:
            return mapper.find_all()

    def get_all_mutex_constraints(self):
        with ConstraintMapper() as mapper:
            return mapper.find_all_mutex_constraints()

    def get_all_implication_constraints(self):
        with ConstraintMapper() as mapper:
            return mapper.find_all_implication_constraints()

    def get_mutex_constraints_by_style(self, style):
        with ConstraintMapper() as mapper:
            return mapper.find_mutex_constraints_by_style_id(style.get_id())

    def get_implication_constraints_by_style(self, style):
        with ConstraintMapper() as mapper:
            return mapper.find_implication_constraints_by_style_id(style.get_id())
        
###ConstraintMapper anpassen ###


### Business Logic Methoden ###

    def validate_outfit(self, outfit):
        return self._validate_outfit_basic(outfit) and \
               self._validate_outfit_mutex(outfit) and \
               self._validate_outfit_implications(outfit) and \
               self._validate_outfit_cardinality(outfit)

    def extend_outfit(self, outfit, item):
        test_outfit = self._create_test_outfit(outfit, item)
        if self.validate_outfit(test_outfit):
            self.add_item_to_outfit(outfit.get_id(), item.get_id())
            return outfit
        return None

    def find_matching_styles_for_wardrobe(self, user):
        wardrobe_items = self.get_clothing_items_by_wardrobe_id(self.get_wardrobe_by_person_id(user.get_id()).get_id())
        all_styles = self.get_all_styles()
        matching_styles = [style for style in all_styles if self._can_create_outfit_with_style(style, wardrobe_items)]
        return matching_styles

    def generate_occasion_based_outfits(self, user, occasion):
        wardrobe_items = self.get_clothing_items_by_wardrobe_id(self.get_wardrobe_by_person_id(user.get_id()).get_id())
        suitable_styles = self._get_styles_for_occasion(occasion)
        outfits = [self._create_outfit_for_style_and_occasion(style, wardrobe_items, occasion) for style in suitable_styles]
        return [outfit for outfit in outfits if outfit is not None]

    def generate_style_recommendations(self, user):
        wardrobe_items = self.get_clothing_items_by_wardrobe_id(self.get_wardrobe_by_person_id(user.get_id()).get_id())
        current_styles = self._get_person_used_styles(user)
        all_styles = self.get_all_styles()
        recommendations = [style for style in all_styles if style not in current_styles and self._is_style_suitable(style, wardrobe_items)]
        return recommendations
      
    def find_similar_outfits(self, outfit):
        similar_outfits = []
        similar_outfits.extend(self._find_outfits_with_similar_types(outfit.get_items()))
        similar_outfits.extend(self._find_outfits_by_style(self.get_style_by_id(outfit.get_style_id())))
        return list(set(similar_outfits))  # Remove duplicates

    def find_missing_essentials(self, user):
        wardrobe_items = self.get_clothing_items_by_wardrobe_id(self.get_wardrobe_by_person_id(user.get_id()).get_id())
        essentials = self._get_essential_clothing_types()
        missing = [essential for essential in essentials if not self._has_clothing_type(wardrobe_items, essential)]
        return missing

