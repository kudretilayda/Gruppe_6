from server.db.WardrobeMapper import WardrobeMapper
from server.bo.Wardrobe import Wardrobe

class WardrobeService:
    def __init__(self):
        self._mapper = WardrobeMapper()

    def create_wardrobe(self, owner_name: str, person_id: str) -> Wardrobe:
        wardrobe = Wardrobe()
        wardrobe.set_owner_name(owner_name)
        wardrobe.set_person_id(person_id)
        return self._mapper.insert(wardrobe)

    def get_wardrobe(self, wardrobe_id: str) -> Wardrobe:
        return self._mapper.find_by_id(wardrobe_id)

    def get_wardrobe_by_person(self, person_id: str) -> Wardrobe:
        return self._mapper.find_by_person(person_id)

    def update_wardrobe(self, wardrobe: Wardrobe) -> Wardrobe:
        return self._mapper.update(wardrobe)

    def delete_wardrobe(self, wardrobe_id: str) -> bool:
        wardrobe = self.get_wardrobe(wardrobe_id)
        if wardrobe:
            self._mapper.delete(wardrobe)
            return True
        return False