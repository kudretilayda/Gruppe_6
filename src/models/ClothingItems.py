from typing import List, Dict, Any, Optional
from .BaseModels import BaseModel
from .Enum import Season, Occasion

class ClothingItem(BaseModel):
    """Model class for clothing items"""
    def __init__(self):
        super().__init__()
        self._name: str = ""
        self._type_id: int = 0  # ID referencing the clothing type
        self._color: str = ""
        self._wardrobe_id: int = 0  # ID referencing the wardrobe
        self._seasons: List[Season] = []
        self._occasions: List[Occasion] = []
        self._times_worn: int = 0

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def type_id(self) -> int:
        return self._type_id

    @type_id.setter
    def type_id(self, value: int) -> None:
        self._type_id = value

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self, value: str) -> None:
        self._color = value

    def wear(self) -> None:
        """Record the item being worn"""
        self._times_worn += 1

    def to_dict(self) -> Dict[str, Any]:
        """Convert clothing item to a dictionary"""
        return {
            'id': self.id,
            'name': self._name,
            'type_id': self._type_id,
            'color': self._color,
            'wardrobe_id': self._wardrobe_id,
            'seasons': [season.value for season in self._seasons],
            'occasions': [occasion.value for occasion in self._occasions],
            'times_worn': self._times_worn
        }
