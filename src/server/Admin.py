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

    def create_user(self, firstname, lastname, nickname, email, google_id):
        user = User()
        user.set_firstname(firstname)
        user.set_lastname(lastname)
        user.set_nickname(nickname)
        user.set_email(email)
        user.set_google_id(google_id)
        with UserMapper() as mapper:
            return mapper.insert(user)

    def get_all_users(self):
        with UserMapper() as mapper:
            return mapper.find_all()

    def get_user_by_id(self, user_id):
        with UserMapper() as mapper:
            return mapper.find_by_key(user_id)

    def get_user_by_google_id(self, google_id):
        with UserMapper() as mapper:
            return mapper.find_by_google_id(google_id)

    def change_user(self, user):
        with UserMapper() as mapper:
            return mapper.update(user)

    def save_user(self, user):
        with UserMapper() as mapper:
            mapper.insert(user)

    def delete_user(self, user):
        with UserMapper() as mapper:
            mapper.delete(user)

### Kleiderschrank ###

    def create_wardrobe(self, user_id):
        wardrobe = Wardrobe()
        wardrobe.set_wardrobe_owner(user_id)
        with WardrobeMapper() as mapper:
            return mapper.insert(wardrobe)

    def add_item_to_wardrobe(self, item):
        wardrobe = Wardrobe()
        wardrobe.set_items(item)

    def get_wardrobe_by_id(self, wardrobe_id):
        with WardrobeMapper() as mapper:
            return mapper.find_by_key(wardrobe_id)

    def get_wardrobe_by_user_id(self, user_id):
        with WardrobeMapper() as mapper:
            return mapper.find_by_person_id(user_id)

    def get_all_wardrobes(self):
        with WardrobeMapper() as mapper:
            return mapper.find_all()

    def save_wardrobe(self, wardrobe):
        with WardrobeMapper() as mapper:
            mapper.update(wardrobe)

    def delete_wardrobe(self, wardrobe):
        with WardrobeMapper() as mapper:
            self._cleanup_reference(wardrobe)
            mapper.delete(wardrobe)

### Kleidungsstück ###

    def create_clothing_item(self, wardrobe_id, clothing_type_id, item_name):
        clothing_item = ClothingItem()
        clothing_item.set_wardrobe_id(wardrobe_id)
        clothing_item.set_clothing_type(clothing_type_id)
        clothing_item.set_item_name(item_name)

        with ClothingItemMapper() as mapper:
            return mapper.insert(clothing_item)

    def get_all_clothing_items(self):
        with ClothingItemMapper() as mapper:
            return mapper.find_all()

    def get_clothing_item_by_id(self, clothing_item_id):
        with ClothingItemMapper() as mapper:
            return mapper.find_by_key(clothing_item_id)

    def get_clothing_items_by_wardrobe_id(self, wardrobe_id):
        with ClothingItemMapper() as mapper:
            return mapper.find_by_wardrobe_id(wardrobe_id)

    def save_clothing_item(self, clothing_item):
        with ClothingItemMapper() as mapper:
            mapper.update(clothing_item)

    def delete_clothing_item(self, clothing_item):
        with ClothingItemMapper() as mapper:
            # Erst alle Referenzen auf ClothingItem löschen (Outfits)
            self._cleanup_reference(clothing_item)
            mapper.delete(clothing_item)

### Outfit ###

    def create_outfit(self, outfit_name, style_id):
        outfit = Outfit()
        outfit.set_outfit_name(outfit_name)
        outfit.set_style(style_id)

        with OutfitMapper() as mapper:
            return mapper.insert(outfit)

    def add_item_to_outfit(self, outfit_id, item):
        outfit = Outfit()
        outfit.set_items(item)
        with OutfitMapper() as mapper:
            mapper.add_item_to_outfit(outfit_id, item)

    def remove_item_from_outfit(self, outfit_id, item):
        with OutfitMapper() as mapper:
            mapper.remove_item_from_outfit(outfit_id, item)

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

### Style ###

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
            self._cleanup_reference(style)
            mapper.delete(style)

### Kleidungstyp ###

    def create_clothing_type(self, type_name, type_usage):
        clothing_type = ClothingType()
        clothing_type.set_name(type_name)
        clothing_type.set_usage(type_usage)

        with ClothingTypeMapper() as mapper:
            return mapper.insert(clothing_type)

    def get_clothing_type_by_id(self, clothing_type_id):
        with ClothingTypeMapper() as mapper:
            return mapper.find_by_id(clothing_type_id)

    def get_all_clothing_types(self):
        with ClothingTypeMapper() as mapper:
            return mapper.find_all()


    '''
    3) Abfrage, welche Styles mit den aktuell im Kleiderschrank befindlichen Kleidungsstücken umgesetzt
    werden könnten und deren Umsetzung nach Auswahl eines Styles
    '''

### Business Logic Methoden ###

    def find_applicable_styles(self):
        with ClothingTypeMapper() as item_mapper:
            wardrobe_items = item_mapper.find_all()

        with StyleMapper() as style_mapper:
            styles = style_mapper.find_all()

        applicable_styles = []
        for style in styles:
            required_clothing_types = style.get_clothing_type()
            matches = 0

            for required in required_clothing_types:
                for item in wardrobe_items:
                    if item.get_clothing_type() == required:
                        matches += 1
                        break
            if matches == len(required_clothing_types):
                applicable_styles.append(style)

        return applicable_styles

    def generate_outfit_for_style(self, style_id):
        with ClothingItemMapper() as item_mapper, StyleMapper() as style_mapper:
            wardrobe_items = item_mapper.find_all()
            style = style_mapper.find_by_key(style_id)

        selected_items = []
        required_clothing_types = style.get_clothing_type()

        for c_type in required_clothing_types:
            for item in wardrobe_items:
                if item.get_clothing_type() == c_type:
                    selected_items.append(item)
                    break

        outfit = Outfit()
        outfit.set_style(style_id)
        outfit.set_outfit_name(f"Generated Outfit for Style {style_id}")

        for item in selected_items:
            outfit.set_items(item)

        with OutfitMapper() as outfit_mapper:
            return outfit_mapper.insert(outfit)

    '''
    4) Abfrage, welche Kleidungsstücke ergänzend zu einer zuvor gewählten Teilbekleidung anzuziehen
    sind, um ein in Bezug auf einen Style konsistentes Outfit zu erhalten und schrittweise 
    Führung durch den weiteren Prozess der Vervollständigung des Outfits auf Basis der verfügbaren Styles.'''

    def suggest_complementary_outfits(self, outfit):
        with ClothingItemMapper() as item_mapper, StyleMapper() as style_mapper:
            wardrobe_items = item_mapper.find_all()
            style = style_mapper.find_by_key(outfit.get_style())

        # Ist- und Soll-Zustand
        required_clothing_types = style.get_clothing_type()
        existing_clothing_types = {item.get_clothing_type() for item in outfit.get_items()}

        # Differenz
        missing_clothing_types = [ctype for ctype in required_clothing_types if ctype not in existing_clothing_types]

        suggested_items = []
        for missing_type in missing_clothing_types:
            for item in wardrobe_items:
                if item.get_clothing_type() == missing_type:
                    suggested_items.append(item)
                    break

        return suggested_items

    '''
    5) Verwalten von Constraints bezüglich Styles sowie eine jederzeit erfolgende 
    Bewertung allerConstraints des jeweiligen Style in Bezug auf das aktuelle Outfit.'''

    # Verwaltung der Constraints

    def create_unary_constraint(self, style):
        constraint = UnaryConstraint()
        constraint.style = style

        with UnaryConstraintMapper() as mapper:
            return mapper.insert(constraint)

    def create_binary_constraint(self, item_1, item_2):
        constraint = BinaryConstraint(item_1, item_2)

        with BinaryConstraintMapper() as mapper:
            return mapper.insert(constraint)

    def create_implication_constraint(self, if_type, then_type):
        constraint = ImplicationConstraint(if_type, then_type)

        with ImplicationConstraintMapper() as mapper:
            return mapper.insert(constraint)

    def create_cardinality_constraint(self, objects, min_count, max_count):
        constraint = CardinalityConstraint(objects, min_count, max_count)

        with CardinalityConstraintMapper() as mapper:
            return mapper.insert(constraint)

    def create_mutex_constraint(self, mutex):
        constraint = MutexConstraint(mutex)

        with MutexConstraintMapper() as mapper:
            return mapper.insert(constraint)

    def delete_constraint(self, constraint):
        mapper_class = {
            UnaryConstraint: UnaryConstraintMapper,
            BinaryConstraint: BinaryConstraintMapper,
            ImplicationConstraint: ImplicationConstraintMapper,
            CardinalityConstraint: CardinalityConstraintMapper,
            MutexConstraint: MutexConstraintMapper
        }[type(constraint)]

        with mapper_class() as mapper:
            mapper.delete(constraint)

    def add_constraint_to_style(self, style_id, constraint):
        with StyleMapper() as style_mapper:
            style = style_mapper.find_by_key(style_id)

        if not style:
            raise ValueError(f"Style {style_id} not found")

        style.set_style_constraints(constraint)

        mapper_class = {
            UnaryConstraint: UnaryConstraintMapper,
            BinaryConstraint: BinaryConstraintMapper,
            ImplicationConstraint: ImplicationConstraintMapper,
            CardinalityConstraint: CardinalityConstraintMapper,
            MutexConstraint: MutexConstraintMapper
        }[type(constraint)]

        with mapper_class() as mapper:
            mapper.insert(constraint)

    def get_constraints_by_style(self, style_id):
        constraints = []

        with UnaryConstraintMapper() as unary_mapper:
            constraints.extend(unary_mapper.find_by_style_id(style_id))

        with BinaryConstraintMapper() as binary_mapper:
            constraints.extend(binary_mapper.find_by_style_id(style_id))

        with ImplicationConstraintMapper() as implication_mapper:
            constraints.extend(implication_mapper.find_by_style_id(style_id))

        with CardinalityConstraintMapper() as cardinality_mapper:
            constraints.extend(cardinality_mapper.find_by_style_id(style_id))

        with MutexConstraintMapper() as mutex_mapper:
            constraints.extend(mutex_mapper.find_by_style_id(style_id))

        return constraints

    # Validieren der Constraints (2 Varianten)

    def validate_outfit(self, outfit):
        with StyleMapper() as style_mapper:
            style = style_mapper.find_by_key(outfit.get_style())

        if not style:
            raise ValueError(f"Style {outfit.get_style()} not found")

        constraints = self.get_constraints_by_style(style.get_id())

        for constraint in constraints:
            if not constraint.validate(outfit):
                print(f"Constraint verletzt: {constraint}")
                return False
            else:
                return True

    '''def validate_outfit(self, outfit):
        style = self.get_style_by_id(outfit.get_style_id())
        items = [self.get_clothing_item_by_id(item_id) for item_id in outfit.get_items()]

        constraints = self.load_constraints_for_style(style.get_id())

        for constraint in constraints:
            if not constraint.validate(outfit):
                print(f"Constraint violated: {constraint}")
                return False
            else:
                return True'''

    # Integrierte Verwaltung und Validierung

    def manage_constraints_and_validate_outfit(self, outfit):
        with StyleMapper() as style_mapper:
            style = style_mapper.find_by_key(outfit.get_style())

        if not style:
            raise ValueError(f"Style with ID {outfit.get_style()} does not exist.")

        constraints = self.get_constraints_by_style(style.get_id())

        for constraint in constraints:
            if not constraint.validate(outfit):
                print(f"Constraint violated: {constraint}")
                return None

        print("The outfit satisfies all constraints!")
        return outfit

    ### Helper Methods ###

    def get_outfit_by_style(self, style_id):
        with OutfitMapper() as mapper:
            return mapper.find_by_style(style_id)

    def _cleanup_reference(self, obj):
        if isinstance(obj, User):
            wardrobes = self.get_wardrobe_by_user_id(obj.get_id())
            for wardrobe in wardrobes:
                self.delete_wardrobe(wardrobe)

        elif isinstance(obj, Wardrobe):
            items = self.get_clothing_items_by_wardrobe_id(obj.get_id())
            for item in items:
                self.delete_wardrobe(item)

        elif isinstance(obj, Style):
            outfits = self.get_outfit_by_style(obj.get_id())
            for outfit in outfits:
                self.delete_outfit(outfit)

            constraints = self.get_constraints_by_style(obj.get_id())
            for constrain in constraints:
                self.delete_constraint(constrain)
