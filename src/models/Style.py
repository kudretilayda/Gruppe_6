# src/models/style.py
from typing import Dict, Any, Optional, List, Set
from .BaseModels import BaseModel
from .Enum import Season, Occasion

class StyleConstraint:
    """Constraint class for style rules"""
    def __init__(self):
        self.type_id: int = 0  # ID of ClothingType
        self.min_count: int = 0
        self.max_count: Optional[int] = None
        self.required_colors: Set[str] = set()
        self.forbidden_colors: Set[str] = set()
        self.must_be_worn_with: Set[int] = set()  # IDs of other required ClothingTypes
        self.cannot_be_worn_with: Set[int] = set()  # IDs of incompatible ClothingTypes

    def to_dict(self) -> Dict[str, Any]:
        return {
            'type_id': self.type_id,
            'min_count': self.min_count,
            'max_count': self.max_count,
            'required_colors': list(self.required_colors),
            'forbidden_colors': list(self.forbidden_colors),
            'must_be_worn_with': list(self.must_be_worn_with),
            'cannot_be_worn_with': list(self.cannot_be_worn_with)
        }

class Style(BaseModel):
    """Model class for styles"""
    def __init__(self):
        super().__init__()
        self._name: str = ""
        self._description: Optional[str] = None
        self._creator_id: int = 0
        self._is_public: bool = False
        self._seasons: List[Season] = []
        self._occasions: List[Occasion] = []
        self._constraints: List[StyleConstraint] = []
        self._tags: Set[str] = set()

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    def add_constraint(self, constraint: StyleConstraint) -> None:
        """Add a style constraint"""
        self._constraints.append(constraint)

    def validate_outfit(self, outfit: 'Outfit') -> bool:
        """Validate if an outfit matches this style's constraints"""
        for constraint in self._constraints:
            # Count items of the constrained type
            matching_items = [item for item in outfit.items 
                            if item.type_id == constraint.type_id]
            count = len(matching_items)
            
            # Check quantity constraints
            if count < constraint.min_count:
                return False
            if constraint.max_count and count > constraint.max_count:
                return False

            # Check color constraints
            for item in matching_items:
                if constraint.required_colors and item.color not in constraint.required_colors:
                    return False
                if item.color in constraint.forbidden_colors:
                    return False

            # Check relationship constraints
            outfit_type_ids = {item.type_id for item in outfit.items}
            if not constraint.must_be_worn_with.issubset(outfit_type_ids):
                return False
            if constraint.cannot_be_worn_with.intersection(outfit_type_ids):
                return False

        return True

    def to_dict(self) -> Dict[str, Any]:
        data = super().to_dict()
        data.update({
            'name': self._name,
            'description': self._description,
            'creator_id': self._creator_id,
            'is_public': self._is_public,
            'seasons': [season.value for season in self._seasons],
            'occasions': [occasion.value for occasion in self._occasions],
            'constraints': [constraint.to_dict() for constraint in self._constraints],
            'tags': list(self._tags)
        })
        return data

class Outfit(BaseModel):
    """Model class for outfits"""
    def __init__(self):
        super().__init__()
        self._name: str = ""
        self._wardrobe_id: int = 0
        self._style_id: Optional[int] = None
        self._items: List['ClothingItems'] = []
        self._occasions: List[Occasion] = []
        self._seasons: List[Season] = []
        self._rating: Optional[int] = None
        self._notes: Optional[str] = None
        self._times_worn: int = 0

    def add_item(self, item: 'ClothingItems') -> None:
        """Add an item to the outfit"""
        if item.wardrobe_id != self._wardrobe_id:
            raise ValidationException("Item must belong to the same wardrobe")
        self._items.append(item)

    def remove_item(self, item: 'ClothingItes') -> None:
        """Remove an item from the outfit"""
        self._items.remove(item)

    def wear(self) -> None:
        """Record the outfit being worn"""
        self._times_worn += 1
        for item in self._items:
            item.wear()

    def calculate_season_compatibility(self) -> Dict[Season, float]:
        """Calculate compatibility score for each season"""
        scores = {season: 0.0 for season in Season}
        if not self._items:
            return scores

        for item in self._items:
            for season in item._seasons:
                scores[season] += 1

        # Normalize scores
        total_items = len(self._items)
        for season in scores:
            scores[season] /= total_items

        return scores

    def to_dict(self) -> Dict[str, Any]:
        data = super().to_dict()
        data.update({
            'name': self._name,
            'wardrobe_id': self._wardrobe_id,
            'style_id': self._style_id,
            'items': [item.to_dict() for item in self._items],
            'occasions': [occasion.value for occasion in self._occasions],
            'seasons': [season.value for season in self._seasons],
            'rating': self._rating,
            'notes': self._notes,
            'times_worn': self._times_worn
        })
        return data