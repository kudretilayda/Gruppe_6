from mapper.person_mapper import PersonMapper

class PersonService:
    @staticmethod
    def create_person(data):
        # Business logic for person creation
        return PersonMapper.insert(data)

    @staticmethod
    def get_person_by_google_id(google_id):
        return PersonMapper.find_by_google_id(google_id)

# /services/wardrobe_service.py
from mapper.wardrobe_mapper import WardrobeMapper

class WardrobeService:
    @staticmethod
    def create_wardrobe(owner_id):
        wardrobe_data = {'eigentuemer_id': owner_id}
        return WardrobeMapper.insert(wardrobe_data)

    @staticmethod
    def get_wardrobe(owner_id):
        return WardrobeMapper.find_by_owner(owner_id)