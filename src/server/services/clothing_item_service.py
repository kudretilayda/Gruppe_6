from mapper.clothing_item_mapper import ClothingItemMapper
from bo.clothing_item import ClothingItem

class ClothingItemService:
    @staticmethod
    def get_all_items():
        return ClothingItemMapper.find_all()

    @staticmethod
    def create_item(item_data):
        item = ClothingItem()
        item.set_type(item_data['type_id'])
        return ClothingItemMapper.insert(item)

    @staticmethod
    def get_item_by_id(item_id):
        return ClothingItemMapper.find_by_id(item_id)

    @staticmethod
    def delete_item(item_id):
        return ClothingItemMapper.delete(item_id)