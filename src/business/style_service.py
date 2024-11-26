# src/business/style_service.py (Fortsetzung)

def _create_constraint(self, constraint_data: dict):
        """Factory method to create appropriate constraint types"""
        constraint_type = constraint_data.get('type')
        
        if constraint_type == 'mutex':
            constraint = Mutex()
            constraint.bezugsobjekt1 = constraint_data.get('obj1')
            constraint.bezugsobjekt2 = constraint_data.get('obj2')
        elif constraint_type == 'kardinalitaet':
            constraint = Kardinalitaet()
            constraint.bezugsobjekt = constraint_data.get('obj')
            constraint.min_count = constraint_data.get('min', 0)
            constraint.max_count = constraint_data.get('max')
        else:
            raise ValueError(f"Unknown constraint type: {constraint_type}")
            
        return constraint

def get_matching_outfits(self, kleiderschrank_id: int, style_id: int) -> List[Outfit]:
        """Findet alle möglichen Outfits die zum Style passen"""
        style = self._style_mapper.find_by_id(style_id)
        if not style:
            raise ValueError("Style not found")
            
        wardrobe_items = self._get_wardrobe_items(kleiderschrank_id)
        return self._generate_valid_combinations(wardrobe_items, style)
        
def _generate_valid_combinations(self, items: list, style: Style) -> List[Outfit]:
        """Generiert und validiert alle möglichen Outfit-Kombinationen"""
        valid_outfits = []
        
        # Startkombi mit essentiellen Kleidungsstücken
        base_combinations = self._get_base_combinations(items, style)
        
        for base in base_combinations:
            # Erweitere die Basis mit optionalen Items
            extended_combinations = self._extend_combination(base, items, style)
            valid_outfits.extend(extended_combinations)
            
        return valid_outfits

# src/business/outfit_service.py
class OutfitService:
    def __init__(self):
        self._StyleMapper = StyleMapper()
        self._outfit_mapper = OutfitMapper()
        
    def suggest_outfit_completion(self, current_items: list, style_id: int) -> dict:
        """Schlägt Vervollständigung eines Outfits vor"""
        style = self._style_mapper.find_by_id(style_id)
        
        # Analysiere fehlende Kategorien
        missing_categories = self._analyze_missing_categories(current_items, style)
        
        # Finde passende Items für jede fehlende Kategorie
        suggestions = {}
        for category in missing_categories:
            matching_items = self._find_matching_items(category, current_items, style)
            if matching_items:
                suggestions[category] = matching_items
                
        return {
            'missing_categories': missing_categories,
            'suggestions': suggestions,
            'completion_percentage': self._calculate_completion_percentage(current_items, style)
        }