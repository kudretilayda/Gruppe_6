from server.db.ClothingItemsMapper import ClothingItemMapper
from server.bo.ClothingItems import ClothingItem

class ClothingItemService:
    def __init__(self):
        self._mapper = ClothingItemMapper()

    def create_clothing_item(self, product_name: str, wardrobe_id: str, 
                           clothing_type_id: str, color: str, brand: str, 
                           season: str) -> ClothingItem:
        item = ClothingItem()
        item.set_product_name(product_name)
        item.set_wardrobe_id(wardrobe_id)
        item.set_clothing_type_id(clothing_type_id)
        item.set_color(color)
        item.set_brand(brand)
        item.set_season(season)
        return self._mapper.insert(item)

    def get_clothing_item(self, item_id: str) -> ClothingItem:
        return self._mapper.find_by_id(item_id)

    def get_items_by_wardrobe(self, wardrobe_id: str) -> list[ClothingItem]:
        return self._mapper.find_by_wardrobe(wardrobe_id)

    def update_clothing_item(self, item: ClothingItem) -> ClothingItem:
        return self._mapper.update(item)

    def delete_clothing_item(self, item_id: str) -> bool:
        item = self.get_clothing_item(item_id)
        if item:
            self._mapper.delete(item)
            return True
        return False