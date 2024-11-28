# src/server/Administration.py

from .bo.User import Person
from .bo.Wardrobe import Wardrobe
from .bo.ClothingType import Kleidungstyp
from .bo.ClothingItems import ClothingItem
from .bo.Style import Style
from .bo.Outfit import Outfit
from .bo.Constraint import Constraint

from .db.UserMapper import PersonMapper
from .db.WardrobeMapper import WardrobeMapper
from .db.ClothingTypeMapper import ClothingTypeMapper
from .db.ClothingItemsMapper import ClothingItemMapper
from .db.StyleMapper import StyleMapper
from .db.OutfitMapper import OutfitMapper
from .db.ConstraintMapper import ConstraintMapper

class WardrobeAdministration:
    """Diese Klasse aggregiert die Applikationslogik für den digitalen Kleiderschrank.
    
    Sie ist die zentrale Klasse für die Verwaltung aller Geschäftsobjekte und deren Beziehungen.
    Hier werden sämtliche Methoden zur Erstellung, Änderung, Löschung und Abfrage der 
    verschiedenen Objekte bereitgestellt."""

    def __init__(self):
        pass

    """Person-spezifische Methoden"""
    def create_person(self, google_id, firstname, lastname, nickname=None):
        """Eine Person anlegen"""
        person = Person()
        person.set_google_id(google_id)
        person.set_firstname(firstname)
        person.set_lastname(lastname)
        person.set_nickname(nickname)

        with PersonMapper() as mapper:
            person = mapper.insert(person)
            # Automatisch einen Kleiderschrank für die Person anlegen
            self.create_wardrobe_for_person(person.get_id())
            return person

    def get_person_by_id(self, id):
        """Die Person mit der gegebenen ID auslesen."""
        with PersonMapper() as mapper:
            return mapper.find_by_key(id)

    def get_person_by_google_id(self, google_id):
        """Die Person mit der gegebenen Google ID auslesen."""
        with PersonMapper() as mapper:
            return mapper.find_by_google_id(google_id)

    def update_person(self, person):
        """Die gegebene Person updaten."""
        with PersonMapper() as mapper:
            return mapper.update(person)

    def delete_person(self, person):
        """Die gegebene Person aus dem System löschen."""
        with PersonMapper() as mapper:
            # Zuerst den zugehörigen Kleiderschrank löschen
            wardrobe = self.get_wardrobe_by_person(person.get_id())
            if wardrobe is not None:
                self.delete_wardrobe(wardrobe)
            mapper.delete(person)

    """Kleiderschrank-spezifische Methoden"""
    def create_wardrobe_for_person(self, person_id):
        """Einen Kleiderschrank für eine Person anlegen."""
        with WardrobeMapper() as mapper:
            wardrobe = Wardrobe()
            wardrobe.set_person_id(person_id)
            return mapper.insert(wardrobe)

    def get_wardrobe_by_person(self, person_id):
        """Den Kleiderschrank einer Person auslesen."""
        with WardrobeMapper() as mapper:
            return mapper.find_by_person_id(person_id)

    def delete_wardrobe(self, wardrobe):
        """Einen Kleiderschrank löschen."""
        with WardrobeMapper() as mapper:
            # Zuerst alle Kleidungsstücke löschen
            items = self.get_items_of_wardrobe(wardrobe.get_id())
            if items is not None:
                for item in items:
                    self.delete_clothing_item(item)
            mapper.delete(wardrobe)

    """Kleidungsstück-spezifische Methoden"""
    def create_clothing_item(self, wardrobe_id, type_id, name):
        """Ein Kleidungsstück anlegen."""
        with ClothingItemMapper() as mapper:
            item = ClothingItem()
            item.set_wardrobe_id(wardrobe_id)
            item.set_type_id(type_id)
            item.set_name(name)
            return mapper.insert(item)

    def get_items_of_wardrobe(self, wardrobe_id):
        """Alle Kleidungsstücke eines Kleiderschranks auslesen."""
        with ClothingItemMapper() as mapper:
            return mapper.find_by_wardrobe_id(wardrobe_id)

    def delete_clothing_item(self, item):
        """Ein Kleidungsstück löschen."""
        with ClothingItemMapper() as mapper:
            # Auch alle Outfit-Zuordnungen löschen
            outfits = self.get_outfits_by_item(item.get_id())
            if outfits is not None:
                for outfit in outfits:
                    self.remove_item_from_outfit(outfit.get_id(), item.get_id())
            mapper.delete(item)

    """Style-spezifische Methoden"""
    def create_style(self, name, features):
        """Einen Style anlegen."""
        with StyleMapper() as mapper:
            style = Style()
            style.set_name(name)
            style.set_features(features)
            return mapper.insert(style)

    def get_style_by_id(self, id):
        """Einen Style mit der gegebenen ID auslesen."""
        with StyleMapper() as mapper:
            return mapper.find_by_key(id)

    def get_possible_styles_for_wardrobe(self, wardrobe_id):
        """Alle möglichen Styles für einen Kleiderschrank ermitteln."""
        # Hier kommt die Logik zur Ermittlung möglicher Styles
        # basierend auf den vorhandenen Kleidungsstücken
        items = self.get_items_of_wardrobe(wardrobe_id)
        with StyleMapper() as mapper:
            all_styles = mapper.find_all()
            possible_styles = []
            for style in all_styles:
                if self.check_style_possible(style, items):
                    possible_styles.append(style)
            return possible_styles

    def check_style_possible(self, style, available_items):
        """Prüfen ob ein Style mit den verfügbaren Kleidungsstücken möglich ist."""
        constraints = self.get_constraints_of_style(style.get_id())
        return all(self.check_constraint(constraint, available_items) 
                  for constraint in constraints)

    """Outfit-spezifische Methoden"""
    def create_outfit(self, style_id, items):
        """Ein Outfit anlegen."""
        with OutfitMapper() as mapper:
            outfit = Outfit()
            outfit.set_style_id(style_id)
            outfit = mapper.insert(outfit)
            # Items dem Outfit zuordnen
            for item in items:
                self.add_item_to_outfit(outfit.get_id(), item.get_id())
            return outfit

    def get_outfits_by_item(self, item_id):
        """Alle Outfits abrufen, die ein bestimmtes Kleidungsstück enthalten."""
        with OutfitMapper() as mapper:
            return mapper.find_by_item_id(item_id)

    """Constraint-spezifische Methoden"""
    def create_constraint(self, style_id, constraint_type):
        """Ein Constraint anlegen."""
        with ConstraintMapper() as mapper:
            constraint = Constraint()
            constraint.set_style_id(style_id)
            constraint.set_constraint_type(constraint_type)
            return mapper.insert(constraint)

    def get_constraints_of_style(self, style_id):
        """Alle Constraints eines Styles abrufen."""
        with ConstraintMapper() as mapper:
            return mapper.find_by_style_id(style_id)

    def check_constraint(self, constraint, items):
        """Ein einzelnes Constraint überprüfen."""
        # Hier kommt die spezifische Logik für die verschiedenen Constraint-Typen
        if constraint.get_constraint_type() == "binary":
            return self._check_binary_constraint(constraint, items)
        elif constraint.get_constraint_type() == "unary":
            return self._check_unary_constraint(constraint, items)
        elif constraint.get_constraint_type() == "mutex":
            return self._check_mutex_constraint(constraint, items)
        elif constraint.get_constraint_type() == "kardinalitaet":
            return self._check_cardinality_constraint(constraint, items)
        return True