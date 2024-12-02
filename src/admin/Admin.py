# src/server/admin/administration.py

from server.db.UserMapper import PersonMapper
from server.db.WardrobeMapper import WardrobeMapper
from server.db.ClothingTypeMapper import ClothingTypeMapper
from server.db.ClothingItemsMapper import ClothingItemMapper
from server.db.OutfitMapper import OutfitMapper
from server.db.StyleMapper import StyleMapper
from server.db.ConstraintMapper import (ConstraintRuleMapper, 
                                              BinaryConstraintMapper, 
                                              UnaryConstraintMapper)

class Administration:
    """Zentralle Administrationsklasse der Anwendung."""
    
    def __init__(self):
        self._person_mapper = PersonMapper()
        self._wardrobe_mapper = WardrobeMapper()
        self._clothing_type_mapper = ClothingTypeMapper()
        self._clothing_item_mapper = ClothingItemMapper()
        self._outfit_mapper = OutfitMapper()
        self._style_mapper = StyleMapper()
        self._constraint_rule_mapper = ConstraintRuleMapper()
        self._binary_constraint_mapper = BinaryConstraintMapper()
        self._unary_constraint_mapper = UnaryConstraintMapper()

    """Person-spezifische Methoden"""
    def create_person(self, google_id, firstname, lastname, nickname=None):
        """Person anlegen"""
        person = PersonMapper()
        person.set_google_id(google_id)
        person.set_firstname(firstname)
        person.set_lastname(lastname)
        person.set_nickname(nickname)
        return self._person_mapper.insert(person)

    def get_person_by_id(self, id):
        """Person mit ID auslesen"""
        return self._person_mapper.find_by_id(id)

    def get_person_by_google_id(self, google_id):
        """Person mit Google ID auslesen"""
        return self._person_mapper.find_by_google_id(google_id)

    def update_person(self, person):
        """Person aktualisieren"""
        return self._person_mapper.update(person)

    def delete_person(self, person):
        """Person löschen"""
        self._person_mapper.delete(person)

    """Wardrobe-spezifische Methoden"""
    def create_wardrobe(self, person_id, owner_name):
        """Wardrobe anlegen"""
        wardrobe = WardrobeMapper()
        wardrobe.set_person_id(person_id)
        wardrobe.set_owner_name(owner_name)
        return self._wardrobe_mapper.insert(wardrobe)

    def get_wardrobe_by_person(self, person_id):
        """Wardrobe einer Person auslesen"""
        return self._wardrobe_mapper.find_by_person_id(person_id)

    """ClothingItem-spezifische Methoden"""
    def create_clothing_item(self, wardrobe_id, type_id, product_name, color=None, brand=None, season=None):
        """Kleidungsstück anlegen"""
        item = ClothingItemMapper()
        item.set_wardrobe_id(wardrobe_id)
        item.set_type_id(type_id)
        item.set_product_name(product_name)
        item.set_color(color)
        item.set_brand(brand)
        item.set_season(season)
        return self._clothing_item_mapper.insert(item)

    def get_clothing_items_by_wardrobe(self, wardrobe_id):
        """Alle Kleidungsstücke einer Wardrobe auslesen"""
        return self._clothing_item_mapper.find_by_wardrobe(wardrobe_id)

    """Outfit-spezifische Methoden"""
    def create_outfit(self, name, style_id, created_by):
        """Outfit anlegen"""
        outfit = OutfitMapper()
        outfit.set_name(name)
        outfit.set_style_id(style_id)
        outfit.set_created_by(created_by)
        return self._outfit_mapper.insert(outfit)

    def add_item_to_outfit(self, outfit_id, item_id):
        """Kleidungsstück zu Outfit hinzufügen"""
        self._outfit_mapper.add_item_to_outfit(outfit_id, item_id)

    def get_outfit_items(self, outfit_id):
        """Alle Kleidungsstücke eines Outfits auslesen"""
        return self._outfit_mapper.find_items_by_outfit(outfit_id)

    def remove_item_from_outfit(self, outfit_id, item_id):
        """Kleidungsstück aus Outfit entfernen"""
        self._outfit_mapper.remove_item_from_outfit(outfit_id, item_id)

    """Style-spezifische Methoden"""
    def create_style(self, name, description, created_by):
        """Style anlegen"""
        style = StyleMapper()
        style.set_name(name)
        style.set_description(description)
        style.set_created_by(created_by)
        return self._style_mapper.insert(style)

    def add_constraint_to_style(self, style_id, constraint_type, **constraint_data):
        """Constraint zu Style hinzufügen"""
        # Basis-Constraint erstellen
        constraint = ConstraintRuleMapper()
        constraint.set_style_id(style_id)
        constraint.set_constraint_type(constraint_type)
        constraint = self._constraint_rule_mapper.insert(constraint)

        # Spezifisches Constraint erstellen
        if constraint_type == 'binary':
            binary = BinaryConstraintMapper()
            binary.set_id(constraint.get_id())
            binary.set_reference_object1_id(constraint_data.get('reference_object1_id'))
            binary.set_reference_object2_id(constraint_data.get('reference_object2_id'))
            self._binary_constraint_mapper.insert(binary)
        elif constraint_type == 'unary':
            unary = UnaryConstraintMapper()
            unary.set_id(constraint.get_id())
            unary.set_reference_object_id(constraint_data.get('reference_object_id'))
            self._unary_constraint_mapper.insert(unary)

        return constraint

    def check_style_constraints(self, outfit_id):
        """Prüft alle Constraints eines Outfits"""
        outfit = self._outfit_mapper.find_by_id(outfit_id)
        style = self._style_mapper.find_by_id(outfit.get_style_id())
        constraints = self._constraint_rule_mapper.find_by_style(style.get_id())
        
        violations = []
        for constraint in constraints:
            if not self._check_constraint(constraint, outfit):
                violations.append(f"Constraint {constraint.get_id()} verletzt")
        
        return len(violations) == 0, violations

    def _check_constraint(self, constraint, outfit):
        """Prüft ein einzelnes Constraint"""
        if constraint.get_constraint_type() == 'binary':
            binary = self._binary_constraint_mapper.find_by_constraint_id(constraint.get_id())
            items = self.get_outfit_items(outfit.get_id())
            return self._check_binary_constraint(binary, items)
        elif constraint.get_constraint_type() == 'unary':
            unary = self._unary_constraint_mapper.find_by_constraint_id(constraint.get_id())
            items = self.get_outfit_items(outfit.get_id())
            return self._check_unary_constraint(unary, items)
        return True

    def _check_binary_constraint(self, constraint, items):
        """Prüft ein binäres Constraint"""
        item_types = [item.get_type_id() for item in items]
        return (constraint.get_reference_object1_id() in item_types and 
                constraint.get_reference_object2_id() in item_types)

    def _check_unary_constraint(self, constraint, items):
        """Prüft ein unäres Constraint"""
        item_types = [item.get_type_id() for item in items]
        return constraint.get_reference_object_id() in item_types