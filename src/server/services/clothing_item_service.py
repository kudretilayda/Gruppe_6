from typing import List, Optional
import logging
from src.server.db.ClothingItemMapper import ClothingItemMapper
from src.server.bo.ClothingItem import ClothingItem
from src.server.bo.Style import Style

class ClothingItemService:
    """Service-Klasse für alle Clothing Item bezogenen Operationen"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.mapper = ClothingItemMapper()

    def create_item(self, wardrobe_id: int, type_id: int, name: str, 
                   color: Optional[str] = None, brand: Optional[str] = None, 
                   season: Optional[str] = None) -> ClothingItem:
        """Erstellt ein neues Kleidungsstück"""
        try:
            item = ClothingItem()
            item.set_wardrobe_id(wardrobe_id)
            item.set_clothing_type(type_id)
            item.set_item_name(name)
            if color:
                item.set_color(color)
            if brand:
                item.set_brand(brand)
            if season:
                item.set_season(season)

            created_item = self.mapper.insert(item)
            self.logger.info(f"Created clothing item: {created_item.get_id()}")
            return created_item

        except Exception as e:
            self.logger.error(f"Error creating clothing item: {str(e)}")
            raise

    def get_item_by_id(self, item_id: int) -> Optional[ClothingItem]:
        """Holt ein Kleidungsstück anhand seiner ID"""
        try:
            item = self.mapper.find_by_key(item_id)
            if not item:
                self.logger.warning(f"Clothing item not found: {item_id}")
            return item
        except Exception as e:
            self.logger.error(f"Error getting clothing item {item_id}: {str(e)}")
            raise

    def get_items_by_wardrobe(self, wardrobe_id: int) -> List[ClothingItem]:
        """Holt alle Kleidungsstücke eines Kleiderschranks"""
        try:
            items = self.mapper.find_by_wardrobe_id(wardrobe_id)
            self.logger.info(f"Found {len(items)} items for wardrobe {wardrobe_id}")
            return items
        except Exception as e:
            self.logger.error(f"Error getting items for wardrobe {wardrobe_id}: {str(e)}")
            raise

    def get_items_by_type(self, type_id: int) -> List[ClothingItem]:
        """Holt alle Kleidungsstücke eines bestimmten Typs"""
        try:
            return self.mapper.find_by_type(type_id)
        except Exception as e:
            self.logger.error(f"Error getting items by type {type_id}: {str(e)}")
            raise

    def update_item(self, item: ClothingItem) -> ClothingItem:
        """Aktualisiert ein Kleidungsstück"""
        try:
            updated_item = self.mapper.update(item)
            self.logger.info(f"Updated clothing item: {item.get_id()}")
            return updated_item
        except Exception as e:
            self.logger.error(f"Error updating clothing item {item.get_id()}: {str(e)}")
            raise

    def delete_item(self, item_id: int) -> bool:
        """Löscht ein Kleidungsstück"""
        try:
            item = self.get_item_by_id(item_id)
            if item:
                self.mapper.delete(item)
                self.logger.info(f"Deleted clothing item: {item_id}")
                return True
            return False
        except Exception as e:
            self.logger.error(f"Error deleting clothing item {item_id}: {str(e)}")
            raise

    def get_matching_items(self, style: Style, existing_items: List[ClothingItem]) -> List[ClothingItem]:
        """Findet passende Kleidungsstücke zu einem Style und existierenden Items"""
        try:
            # Alle verfügbaren Items holen
            all_items = self.mapper.find_all()
            matching_items = []

            # Rule Engine für Validierung nutzen
            from src.server.bo.RuleEngine import RuleEngine
            engine = RuleEngine()
            
            # Temporäres Outfit für Tests
            from src.server.bo.Outfit import Outfit
            test_outfit = Outfit()
            for item in existing_items:
                test_outfit.add_item(item)

            # Jedes potenzielle Item testen
            for item in all_items:
                if item not in existing_items:
                    test_outfit.add_item(item)
                    validation = engine.validate_outfit(test_outfit, style)
                    if validation.is_valid:
                        matching_items.append(item)
                    test_outfit.remove_item(item)

            self.logger.info(f"Found {len(matching_items)} matching items for style {style.get_id()}")
            return matching_items

        except Exception as e:
            self.logger.error(f"Error finding matching items: {str(e)}")
            raise