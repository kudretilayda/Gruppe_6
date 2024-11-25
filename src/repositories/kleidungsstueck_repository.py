from typing import List, Optional
from src.models.models import ClothingItem
from src.repositories.base_repository import BaseRepository

class ClothingRepository(BaseRepository[ClothingItem]):
    def __init__(self):
        super().__init__(ClothingItem)

    def create(self, item: ClothingItem) -> ClothingItem:
        query = """
            INSERT INTO clothing_item 
            (id, wardrobe_id, type_id, name, color, brand, season, created_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        self._execute_query(query, (
            item.id,
            item.wardrobe_id,
            item.type_id,
            item.name,
            item.color,
            item.brand,
            item.season,
            item.created_at
        ))
        return item

    def get_by_id(self, id: str) -> Optional[ClothingItem]:
        result = self._execute_query(
            "SELECT * FROM clothing_item WHERE id = %s",
            (id,)
        )
        return ClothingItem(**result) if result else None

    def get_by_wardrobe(self, wardrobe_id: str) -> List[ClothingItem]:
        results = self._execute_query_all(
            "SELECT * FROM clothing_item WHERE wardrobe_id = %s",
            (wardrobe_id,)
        )
        return [ClothingItem(**row) for row in results]

    def get_all(self) -> List[ClothingItem]:
        results = self._execute_query_all("SELECT * FROM clothing_item")
        return [ClothingItem(**row) for row in results]

    def update(self, item: ClothingItem) -> ClothingItem:
        query = """
            UPDATE clothing_item 
            SET name = %s, color = %s, brand = %s, season = %s
            WHERE id = %s
        """
        self._execute_update(query, (
            item.name,
            item.color,
            item.brand,
            item.season,
            item.id
        ))
        return item

    def delete(self, id: str) -> bool:
        return self._execute_update(
            "DELETE FROM clothing_item WHERE id = %s",
            (id,)
        ) > 0