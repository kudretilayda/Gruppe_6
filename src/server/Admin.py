from typing import List, Dict, Tuple, Optional
from server.db.UserMapper import PersonMapper
from server.db.WardrobeMapper import WardrobeMapper
from server.db.ClothingItemsMapper import ClothingItemMapper
from server.db.StyleMapper import StyleMapper
from server.db.ConstraintMapper import ConstraintMapper
from server.db.OutfitMapper import OutfitMapper

from server.bo.User import Person
from server.bo.Wardrobe import Wardrobe
from server.bo.ClothingItems import ClothingItem
from server.bo.Style import Style
from server.bo.Outfit import Outfit
from server.bo.Constraint import Constraint

from server.ConstraintHelper import ConstraintHelper


class AdminException(Exception):
    """Basis-Exception für Administration-Fehler"""
    pass

class ValidationError(AdminException):
    """Exception für Validierungsfehler"""
    pass

class ConstraintError(AdminException):
    """Exception für Constraint-Fehler"""
    pass


class Administration:
    """Geschäftslogik der Anwendung"""
    
    def __init__(self):
        """Initialisierung aller benötigten Mapper und Helper"""
        self._person_mapper = PersonMapper()
        self._wardrobe_mapper = WardrobeMapper()
        self._clothing_item_mapper = ClothingItemMapper()
        self._style_mapper = StyleMapper()
        self._constraint_mapper = ConstraintMapper()
        self._outfit_mapper = OutfitMapper()
        self._constraint_helper = ConstraintHelper()
        self._cache_init()

    def _cache_init(self):
        """Initialisiert Cache für häufig verwendete Daten"""
        self._type_cache = {}
        self._constraint_cache = {}

    """Person-bezogene Methoden"""
    def create_person(self, google_id: str, first_name: str, last_name: str, 
                     nickname: str) -> Optional[Person]:
        """Eine neue Person anlegen"""
        try:
            person = Person()
            person.set_google_id(google_id)
            person.set_first_name(first_name)
            person.set_last_name(last_name)
            person.set_nickname(nickname)
            return self._person_mapper.insert(person)
        except Exception as e:
            print(f"Fehler beim Anlegen der Person: {e}")
            return None

    def get_all_persons(self) -> List[Person]:
        """Alle Personen auslesen"""
        return self._person_mapper.find_all()

    def get_person_by_id(self, id: int) -> Optional[Person]:
        """Eine Person anhand ihrer ID auslesen"""
        return self._person_mapper.find_by_id(id)

    def get_person_by_google_id(self, google_id: str) -> Optional[Person]:
        """Eine Person anhand ihrer Google ID auslesen"""
        return self._person_mapper.find_by_google_id(google_id)

    def update_person(self, person: Person) -> bool:
        """Eine Person aktualisieren"""
        try:
            self._person_mapper.update(person)
            return True
        except Exception as e:
            print(f"Fehler beim Update der Person: {e}")
            return False

    def delete_person(self, person: Person) -> bool:
        """Eine Person löschen"""
        try:
            self._person_mapper.delete(person)
            return True
        except Exception as e:
            print(f"Fehler beim Löschen der Person: {e}")
            return False

    """Wardrobe-bezogene Methoden"""
    def create_wardrobe(self, owner_id: int) -> Optional[Wardrobe]:
        """Einen neuen Kleiderschrank anlegen"""
        try:
            wardrobe = Wardrobe()
            wardrobe.set_owner_id(owner_id)
            return self._wardrobe_mapper.insert(wardrobe)
        except Exception as e:
            print(f"Fehler beim Anlegen des Kleiderschranks: {e}")
            return None

    def get_wardrobe_by_owner(self, owner_id: int) -> Optional[Wardrobe]:
        """Einen Kleiderschrank anhand der Owner ID auslesen"""
        return self._wardrobe_mapper.find_by_owner_id(owner_id)

    """ClothingItem-bezogene Methoden"""
    def create_clothing_item(self, wardrobe_id: int, type_id: int, 
                           name: str, description: str) -> Optional[ClothingItem]:
        """Ein neues Kleidungsstück anlegen"""
        try:
            item = ClothingItem()
            item.set_wardrobe_id(wardrobe_id)
            item.set_type_id(type_id)
            item.set_name(name)
            item.set_description(description)
            return self._clothing_item_mapper.insert(item)
        except Exception as e:
            print(f"Fehler beim Anlegen des Kleidungsstücks: {e}")
            return None

    def get_items_by_wardrobe(self, wardrobe_id: int) -> List[ClothingItem]:
        """Alle Kleidungsstücke eines Kleiderschranks auslesen"""
        return self._clothing_item_mapper.find_by_wardrobe(wardrobe_id)

    def update_clothing_item(self, item: ClothingItem) -> bool:
        """Ein Kleidungsstück aktualisieren"""
        try:
            self._clothing_item_mapper.update(item)
            return True
        except Exception as e:
            print(f"Fehler beim Update des Kleidungsstücks: {e}")
            return False

    def delete_clothing_item(self, item_id: int) -> bool:
        """Ein Kleidungsstück löschen"""
        try:
            item = self._clothing_item_mapper.find_by_id(item_id)
            if item:
                self._clothing_item_mapper.delete(item)
                return True
            return False
        except Exception as e:
            print(f"Fehler beim Löschen des Kleidungsstücks: {e}")
            return False

    """Style-bezogene Methoden"""
    def create_style(self, name: str, description: str, features: str) -> Optional[Style]:
        """Einen neuen Style anlegen"""
        try:
            style = Style()
            style.set_name(name)
            style.set_description(description)
            style.set_features(features)
            return self._style_mapper.insert(style)
        except Exception as e:
            print(f"Fehler beim Anlegen des Styles: {e}")
            return None

    def create_style_with_constraints(self, name: str, description: str, 
                                    features: str, constraints_data: List[Dict]) -> Optional[Style]:
        """Erstellt einen neuen Style mit zugehörigen Constraints"""
        try:
            # Erst den Style erstellen
            style = self.create_style(name, description, features)
            if not style:
                return None
            
            # Dann die Constraints hinzufügen
            for constraint_data in constraints_data:
                self.create_style_constraint(
                    style.get_id(),
                    constraint_data['type'],
                    constraint_data['data']
                )
                
            return style
        except Exception as e:
            print(f"Fehler beim Anlegen des Styles mit Constraints: {e}")
            return None

    def get_all_styles(self) -> List[Style]:
        """Alle Styles auslesen"""
        return self._style_mapper.find_all()

    def get_style_by_id(self, style_id: int) -> Optional[Style]:
        """Einen Style anhand seiner ID auslesen"""
        return self._style_mapper.find_by_id(style_id)

    def update_style(self, style: Style) -> bool:
        """Einen Style aktualisieren"""
        try:
            self._style_mapper.update(style)
            return True
        except Exception as e:
            print(f"Fehler beim Update des Styles: {e}")
            return False

    def delete_style(self, style: Style) -> bool:
        """Einen Style löschen"""
        try:
            self._style_mapper.delete(style)
            return True
        except Exception as e:
            print(f"Fehler beim Löschen des Styles: {e}")
            return False

    """Constraint-bezogene Methoden"""
    def create_style_constraint(self, style_id: int, constraint_type: str, 
                              constraint_data: dict) -> Optional[Constraint]:
        """Erstellt einen neuen Style-Constraint"""
        try:
            constraint = Constraint()
            constraint.set_style_id(style_id)
            constraint.set_type(constraint_type)

            value = self._create_constraint_value(constraint_type, constraint_data)
            constraint.set_value(value)
            return self._constraint_mapper.insert(constraint)
        except Exception as e:
            print(f"Fehler beim Erstellen des Constraints: {e}")
            return None

    def _create_constraint_value(self, constraint_type: str, data: dict) -> str:
        """Hilfsmethode zur Constraint-Wert-Erstellung"""
        constraint_creators = {
            "BINARY": self._constraint_helper.create_binary_constraint,
            "CARDINALITY": self._constraint_helper.create_cardinality_constraint,
            "COLOR": self._constraint_helper.create_color_constraint
        }
        
        if constraint_type not in constraint_creators:
            raise ValueError(f"Unbekannter Constraint-Typ: {constraint_type}")
            
        creator = constraint_creators[constraint_type]
        return creator(**data)

    def get_style_constraints(self, style_id: int) -> List[Constraint]:
        """Gibt alle Constraints eines Styles zurück"""
        return self._constraint_mapper.find_by_style(style_id)

    """Outfit-bezogene Methoden"""
    def create_outfit(self, style_id: int, name: str, clothing_items: List[int]) -> Optional[Outfit]:
        """Ein neues Outfit erstellen mit Validierung"""
        try:
            # Validiere zuerst
            validation = self.validate_outfit(clothing_items, style_id)
            if not validation["is_valid"]:
                raise ValidationError(validation["messages"])

            outfit = outfit()
            outfit.set_style_id(style_id)
            outfit.set_name(name)
            outfit.set_items(clothing_items)
            return self._outfit_mapper.insert(outfit)
        except ValidationError as e:
            print(f"Validierungsfehler: {e}")
            return None
        except Exception as e:
            print(f"Unerwarteter Fehler: {e}")
            return None

    def validate_outfit(self, outfit_items: List[int], style_id: int) -> Dict:
        """Validiert ein Outfit gegen Style-Constraints"""
        try:
            detailed_items = self._get_detailed_items(outfit_items)
            constraints = self._get_constraint_dicts(style_id)
            
            return self._constraint_helper.validate_outfit(detailed_items, constraints)
        except Exception as e:
            return {
                "is_valid": False,
                "messages": [f"Fehler bei der Validierung: {str(e)}"]
            }

    def _get_detailed_items(self, item_ids: List[int]) -> List[Dict]:
        """Lädt detaillierte Informationen zu Kleidungsstücken"""
        detailed_items = []
        for item_id in item_ids:
            item = self._clothing_item_mapper.find_by_id(item_id)
            if item:
                detailed_items.append({
                    'id': item.get_id(),
                    'type_id': item.get_type_id(),
                    'color': item.get_color() if hasattr(item, 'get_color') else None
                })
        return detailed_items

    def _get_constraint_dicts(self, style_id: int) -> List[Dict]:
        """Lädt Constraints als Dictionary-Format"""
        constraints = self.get_style_constraints(style_id)
        return [{
            'constraint_type': c.get_type(),
            'value': c.get_value()
        } for c in constraints]

    def generate_outfit_suggestion(self, wardrobe_id: int, style_id: int, 
                                 weather: str = None, occasion: str = None) -> Optional[List[int]]:
        """Generiert einen Outfit-Vorschlag basierend auf verschiedenen Kriterien"""
        try:
            available_items = self.get_items_by_wardrobe(wardrobe_id)
            style = self.get_style_by_id(style_id)
            if not available_items or not style:
                return None

            required_types = self._get_required_types(style)
            suggestion = []
            
            for required_type in required_types:
                suitable_items = [item for item in available_items 
                                if item.get_type_id() == required_type]
                
                if not suitable_items:
                    continue
                    
                selected_item = self._select_best_item(suitable_items, weather, occasion)
                if selected_item:
                    suggestion.append(selected_item.get_id())

            # Validierung des generierten Outfits
            validation = self.validate_outfit(suggestion, style_id)
            if validation["is_valid"]:
                return suggestion
            return None
            
        except Exception as e:
            print(f"Fehler bei der Outfit-Generierung: {e}")
            return None

    def _get_required_types(self, style: Style) -> List[int]:
        """Ermittelt die erforderlichen Kleidungstypen für einen Style"""
        basic_types = [1, 2, 3]  # Basis-Typen
        
        if "formal" in style.get_features().lower():
            basic_types.extend([4, 5])  # Formelle Zusatztypen
            
        if "casual" in style.get_features().lower():
            basic_types.extend([6])  # Casual Zusatztypen
            
        return basic_types

    def _select_best_item(self, items: List[ClothingItem], 
                         weather: str = None, occasion: str = None) -> Optional[ClothingItem]:
        """Wählt das am besten geeignete Kleidungsstück aus"""
        if not items:
            return None
            
        scored_items = []
        for item in items:
            score = 0
            
            if weather:
                score += self._calculate_weather_score(item, weather)
            
            if occasion:
                score += self._calculate_occasion_score(item, occasion)
            
            scored_items.append((score, item))
        
        return max(scored_items, key=lambda x: x[0])[1] if scored_items else items[0]

    def _calculate_weather_score(self, item: ClothingItem, weather: str) -> int:
        """Berechnet den Wetter-Score für ein Kleidungsstück"""
        score = 0
        description = item.get_description().lower()
        
