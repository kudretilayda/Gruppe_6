from src.server.db.UserMapper import UserMapper
from src.server.db.WardrobeMapper import WardrobeMapper
from src.server.db.ClothingItemMapper import ClothingItemMapper
from src.server.db.ClothingTypeMapper import ClothingTypeMapper
from src.server.db.StyleMapper import StyleMapper
from src.server.db.OutfitMapper import OutfitMapper
from src.server.db.ConstraintMapper import ConstraintMapper
from src.server.bo.User import Person
from src.server.bo.Wardrobe import Wardrobe
from src.server.bo.ClothingItem import ClothingItem
from src.server.bo.ClothingType import ClothingType
from src.server.bo.Style import Style
from src.server.bo.Outfit import Outfit
from src.server.bo.Constraints import Constraints, BinaryConstraint, UnaryConstraint, CardinalityConstraint, MutexConstraint, ImplicationConstraint


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
    
  
    

    def get_user_by_id(self, user_id):
        """Den User mit gegebener ID ausgeben."""
        with UserMapper() as mapper:
            return mapper.find_by_id(user_id)

    def get_user_by_google_id(self, google_id):
        """Den User mit der gegebenen google_id ausgeben."""
        with UserMapper() as mapper:
            return mapper.find_user_by_google_id(google_id)

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
        """Den gegebenen User ändern."""
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

    def get_wardrobe_by_user_id(self, user_id):
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

    def post_clothing_item(self, clothing_item):
        with ClothingItemMapper() as mapper:
            mapper.post(clothing_item)

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

### Helper Methods ###

    def _cleanup_user_references(self, user):
        wardrobes = self.get_wardrobe_by_user_id(user.get_id())
        if wardrobes is not None:
            for wardrobe in wardrobes:
                self.delete_wardrobe(wardrobe)

    def _cleanup_wardrobe_references(self, wardrobe):
        items = self.get_clothing_items_by_wardrobe_id(wardrobe.get_id())
        if items is not None:
            for item in items:
                self.delete_clothing_item(item)
    
    def _cleanup_clothing_item_references(self, clothing_item):
        outfits = self._find_outfits_containing_item(clothing_item)
        if outfits is not None:
            for outfit in outfits:
                self.remove_item_from_outfit(outfit.get_id(), clothing_item.get_id())

    def _cleanup_style_references(self, style):
        outfits = self.get_outfits_by_style_id(style.get_id())
        if outfits is not None:
            for outfit in outfits:
                self.delete_outfit(outfit)

        constraints = self.get_constraints_by_style(style.get_id())
        if constraints is not None:
            for constraint in constraints:
                self._delete_constraint(constraint)

    def _delete_constraint(self, constraint):
        with ConstraintMapper() as mapper:
            mapper.delete(constraint)

    def _validate_outfit_basic(self, outfit):
        style = self.get_style_by_id(outfit.get_style_id())
        items = [self.get_clothing_item_by_id(item_id) for item_id in outfit.get_items()]
        
        with ConstraintMapper() as mapper:
            constraints = mapper.find_by_style_id(style.get_id())
            for constraint in constraints:
                for item in items:
                    if not self._validate_unary_constraint(constraint, item):
                        return False
        return True
    
    def _validate_outfit_mutex(self, outfit):
        style = self.get_style_by_id(outfit.get_style_id())
        items = [self.get_clothing_item_by_id(item_id) for item_id in outfit.get_items()]
        
        with ConstraintMapper() as mapper:
            constraints = mapper.find_by_style_id(style.get_id())
            for constraint in constraints:
                if not self._validate_mutex_constraint(constraint, items):
                    return False
        return True

    def _validate_outfit_implications(self, outfit):
        style = self.get_style_by_id(outfit.get_style_id())
        items = [self.get_clothing_item_by_id(item_id) for item_id in outfit.get_items()]
        
        with ConstraintMapper() as mapper:
            constraints = mapper.find_by_style_id(style.get_id())
            for constraint in constraints:
                if not self._validate_implication_constraint(constraint, items):
                    return False
        return True
    
    def _validate_outfit_cardinality(self, outfit):
        style = self.get_style_by_id(outfit.get_style_id())
        items = [self.get_clothing_item_by_id(item_id) for item_id in outfit.get_items()]
        
        with ConstraintMapper() as mapper:
            constraints = mapper.find_by_style_id(style.get_id())
            for constraint in constraints:
                if not self._validate_cardinality_constraint(constraint, items):
                    return False
        return True

    def _create_test_outfit(self, outfit, item):
        test_outfit = Outfit()
        test_outfit.set_style_id(outfit.get_style_id())
        test_outfit.set_items(outfit.get_items() + [item.get_id()])
        return test_outfit

    def _can_create_outfit_with_style(self, style, items):
        required_types = self._get_required_types(style)
        available_types = {item.get_clothing_type_id() for item in items}
        return all(req_type in available_types for req_type in required_types)

    def _get_styles_for_occasion(self, occasion):
        all_styles = self.get_all_styles()
        return [style for style in all_styles if self._is_style_suitable_for_occasion(style, occasion)]

    def _create_outfit_for_style_and_occasion(self, style, items, occasion):
        suitable_items = [item for item in items if self._is_item_suitable_for_occasion(item, occasion)]
        
        if not suitable_items:
            return None
            
        return self.generate_style_based_outfit(style, suitable_items)

    def _get_user_used_styles(self, user):
        outfits = self._get_user_outfits(user)
        return {outfit.get_style_id() for outfit in outfits}

    def _is_style_suitable(self, style, items):
        required_types = self._get_required_types(style)
        return all(any(item.get_clothing_type_id() == req_type for item in items) for req_type in required_types)

    def _find_outfits_with_similar_types(self, item_ids):
        items = [self.get_clothing_item_by_id(item_id) for item_id in item_ids]
        item_types = {item.get_clothing_type_id() for item in items}
        all_outfits = self.get_all_outfits()
        
        similar_outfits = []
        for outfit in all_outfits:
            outfit_items = [self.get_clothing_item_by_id(item_id) for item_id in outfit.get_items()]
            outfit_types = {item.get_clothing_type_id() for item in outfit_items}
            
            similarity = len(item_types.intersection(outfit_types)) / len(item_types)
            if similarity >= 0.7:
                similar_outfits.append(outfit)
                
        return similar_outfits
    
    def _find_outfits_by_style(self, style):
        with OutfitMapper() as mapper:
            return mapper.find_by_style_id(style.get_id())

    def _get_essential_clothing_types(self):
        with ClothingTypeMapper() as mapper:
            all_types = mapper.find_all()
            return [ctype for ctype in all_types if self._is_type_essential(ctype)]

    def _has_clothing_type(self, items, ctype):
        return any(item.get_clothing_type_id() == ctype.get_id() for item in items)

    def _is_type_essential(self, ctype):
        essential_names = {'T-Shirt', 'Jeans', 'Jacket', 'Shoes'}
        return ctype.get_type_name() in essential_names

    def _get_required_types(self, style):
        required_types = set()
        
        with ConstraintMapper() as mapper:
            constraints = mapper.find_by_style_id(style.get_id())
            for constraint in constraints:
                if constraint.get_constrain() == "required":
                    required_types.add(constraint.get_reference_object_id())
        
        return required_types

    def _validate_mutex_constraint(self, constraint, items):
        type1_present = any(item.get_clothing_type_id() == constraint.get_item_type_1() for item in items)
        type2_present = any(item.get_clothing_type_id() == constraint.get_item_type_2() for item in items)
        return not (type1_present and type2_present)

    def _validate_implication_constraint(self, constraint, items):
        if_type_present = any(item.get_clothing_type_id() == constraint.get_if_type() for item in items)
        then_type_present = any(item.get_clothing_type_id() == constraint.get_then_type() for item in items)
        return not if_type_present or then_type_present

    def _validate_cardinality_constraint(self, constraint, items):
        count = sum(1 for item in items if item.get_clothing_type_id() == constraint.get_item_type())
        return constraint.get_min_count() <= count <= constraint.get_max_count()

    def _validate_unary_constraint(self, constraint, item):
        if constraint.get_reference_object_id() == item.get_clothing_type_id():
            value = getattr(item, constraint.get_attribute())
            if constraint.get_constrain() == "EQUAL":
                return value == constraint.get_val()
            elif constraint.get_constrain() == "NOT_EQUAL":
                return value != constraint.get_val()
        return True

    def _find_outfits_containing_item(self, item):
        all_outfits = self.get_all_outfits()
        return [outfit for outfit in all_outfits if item.get_id() in outfit.get_items()]

    def _get_user_outfits(self, user):
        wardrobe = self.get_wardrobe_by_user_id(user.get_id())
        if wardrobe is None:
            return []
        items = self.get_clothing_items_by_wardrobe_id(wardrobe.get_id())
        item_ids = [item.get_id() for item in items]
        all_outfits = self.get_all_outfits()
        return [outfit for outfit in all_outfits if any(item_id in outfit.get_items() for item_id in item_ids)]

    def _is_style_suitable_for_occasion(self, style, occasion):
        # Implementierung der Logik zur Überprüfung, ob ein Style für einen bestimmten Anlass geeignet ist
        pass

    def _is_item_suitable_for_occasion(self, item, occasion):
        # Implementierung der Logik zur Überprüfung, ob ein Kleidungsstück für einen bestimmten Anlass geeignet ist
        pass

    def generate_style_based_outfit(self, style, preferred_items=None):
        if preferred_items is None:
            preferred_items = []
        
        outfit_items = preferred_items.copy()
        required_types = self._get_required_types(style)
        missing_types = required_types - {item.get_clothing_type_id() for item in outfit_items}
        
        for type_id in missing_types:
            item = self._find_matching_item(type_id, outfit_items, style)
            if item:
                outfit_items.append(item)
        
        outfit = self.create_outfit(style.get_id(), [item.get_id() for item in outfit_items])
        if self.validate_outfit(outfit):
            return outfit
        return None

    def _find_matching_item(self, type_id, current_items, style):
        with ClothingItemMapper() as mapper:
            available_items = mapper.find_by_clothing_type_id(type_id)
            
            for item in available_items:
                test_items = current_items + [item]
                test_outfit = self.create_outfit(style.get_id(), [i.get_id() for i in test_items])
                
                if self.validate_outfit(test_outfit):
                    return item
                    
            return None
   