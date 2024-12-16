from typing import List, Optional, Dict
import logging
from datetime import datetime
from src.server.db.OutfitMapper import OutfitMapper
from src.server.bo.Outfit import Outfit
from src.server.bo.RuleEngine import RuleEngine
from src.server.bo.Style import Style

class OutfitService:
    """Service-Klasse für alle Outfit-bezogenen Operationen"""

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.outfit_mapper = OutfitMapper()
        self.rule_engine = RuleEngine()

    def create_outfit(self, name: str, style_id: int, items: List[int], created_by: int) -> Outfit:
        """Erstellt ein neues Outfit und validiert es gegen den Style"""
        try:
            # Outfit erstellen
            outfit = Outfit()
            outfit.set_outfit_name(name)
            outfit.set_style_id(style_id)
            
            # Items hinzufügen
            for item_id in items:
                outfit.add_item(item_id)

            # Style-Validierung durchführen
            from src.server.service.StyleService import StyleService
            style_service = StyleService()
            style = style_service.get_style_by_id(style_id)
            
            validation_result = self.rule_engine.validate_outfit(outfit, style)
            if not validation_result.is_valid:
                raise ValueError(f"Outfit violates style constraints: {validation_result.violations}")

            # Outfit speichern
            created_outfit = self.outfit_mapper.insert(outfit)
            self.logger.info(f"Created outfit: {created_outfit.get_id()}")
            return created_outfit

        except Exception as e:
            self.logger.error(f"Error creating outfit: {str(e)}")
            raise

    def generate_outfit_proposals(self, style_id: int, wardrobe_id: int, 
                                preferred_items: Optional[List[int]] = None) -> List[Dict]:
        """Generiert Outfit-Vorschläge basierend auf Style und verfügbaren Items"""
        try:
            # Services laden
            from src.server.service.StyleService import StyleService
            from src.server.service.ClothingItemService import ClothingItemService
            
            style_service = StyleService()
            clothing_service = ClothingItemService()

            # Benötigte Daten laden
            style = style_service.get_style_by_id(style_id)
            available_items = clothing_service.get_items_by_wardrobe(wardrobe_id)
            
            if preferred_items:
                preferred_items = [item for item in available_items 
                                 if item.get_id() in preferred_items]

            # Outfit-Vorschläge generieren
            proposals = self.rule_engine.generate_outfit(
                style=style,
                available_items=available_items,
                preferred_items=preferred_items
            )

            self.logger.info(f"Generated outfit proposals for style {style_id}")
            return proposals

        except Exception as e:
            self.logger.error(f"Error generating outfit proposals: {str(e)}")
            raise

    def complete_partial_outfit(self, partial_outfit_items: List[int], 
                              style_id: int, wardrobe_id: int) -> List[Dict]:
        """Schlägt Vervollständigungen für ein teilweise gewähltes Outfit vor"""
        try:
            # Services laden
            from src.server.service.StyleService import StyleService
            from src.server.service.ClothingItemService import ClothingItemService
            
            style_service = StyleService()
            clothing_service = ClothingItemService()

            # Daten laden
            style = style_service.get_style_by_id(style_id)
            available_items = clothing_service.get_items_by_wardrobe(wardrobe_id)
            
            # Temporäres Outfit erstellen
            partial_outfit = Outfit()
            for item_id in partial_outfit_items:
                item = clothing_service.get_item_by_id(item_id)
                if item:
                    partial_outfit.add_item(item)

            # Vervollständigungen vorschlagen
            suggestions = self.rule_engine.suggest_additions(
                partial_outfit=partial_outfit,
                style=style,
                available_items=[item for item in available_items 
                               if item.get_id() not in partial_outfit_items]
            )

            self.logger.info(f"Generated completion suggestions for partial outfit")
            return suggestions

        except Exception as e:
            self.logger.error(f"Error completing partial outfit: {str(e)}")
            raise

    def get_outfit_by_id(self, outfit_id: int) -> Optional[Outfit]:
        """Holt ein Outfit anhand seiner ID"""
        try:
            return self.outfit_mapper.find_by_key(outfit_id)
        except Exception as e:
            self.logger.error(f"Error getting outfit {outfit_id}: {str(e)}")
            raise

    def get_outfits_by_style(self, style_id: int) -> List[Outfit]:
        """Holt alle Outfits eines Styles"""
        try:
            return self.outfit_mapper.find_by_style(style_id)
        except Exception as e:
            self.logger.error(f"Error getting outfits for style {style_id}: {str(e)}")
            raise

    def delete_outfit(self, outfit_id: int) -> bool:
        """Löscht ein Outfit"""
        try:
            outfit = self.get_outfit_by_id(outfit_id)
            if outfit:
                self.outfit_mapper.delete(outfit)
                self.logger.info(f"Deleted outfit: {outfit_id}")
                return True
            return False
        except Exception as e:
            self.logger.error(f"Error deleting outfit {outfit_id}: {str(e)}")
            raise
