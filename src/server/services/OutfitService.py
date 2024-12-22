from server.db.OutfitMapper import OutfitMapper
from server.bo.Outfit import Outfit
from typing import List, Optional

class OutfitService:
    def __init__(self):
        self._mapper = OutfitMapper()

    def create_outfit(self, outfit_name: str, style_id: str, created_by: str, 
                     items: List[str]) -> Outfit:
        outfit = Outfit()
        outfit.set_outfit_name(outfit_name)
        outfit.set_style_id(style_id)
        outfit.set_created_by(created_by)
        outfit.set_items(items)
        return self._mapper.insert(outfit)

    def get_outfit(self, outfit_id: str) -> Optional[Outfit]:
        return self._mapper.find_by_id(outfit_id)

    def get_outfits_by_person(self, person_id: str) -> List[Outfit]:
        return self._mapper.find_by_person(person_id)

    def get_all_outfits(self) -> List[Outfit]:
        return self._mapper.find_all()

    def update_outfit(self, outfit: Outfit) -> Outfit:
        return self._mapper.update(outfit)

    def delete_outfit(self, outfit_id: str) -> bool:
        outfit = self.get_outfit(outfit_id)
        if outfit:
            self._mapper.delete(outfit)
            return True
        return False