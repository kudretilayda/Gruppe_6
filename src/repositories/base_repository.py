from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional, List, Type
from src.server.db.database import Database

T = TypeVar('T')

class BaseRepository(ABC, Generic[T]):
    def __init__(self, model_class: Type[T]):
        self.db = Database()
        self.model_class = model_class

    @abstractmethod
    def create(self, entity: T) -> T:
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> Optional[T]:
        pass

    @abstractmethod
    def get_all(self) -> List[T]:
        pass

    @abstractmethod
    def update(self, entity: T) -> T:
        pass

    @abstractmethod
    def delete(self, id: str) -> bool:
        pass

    def _execute_query(self, query: str, params: tuple = None) -> Optional[dict]:
        with self.db.get_cursor() as cursor:
            cursor.execute(query, params or ())
            return cursor.fetchone()

    def _execute_query_all(self, query: str, params: tuple = None) -> List[dict]:
        with self.db.get_cursor() as cursor:
            cursor.execute(query, params or ())
            return cursor.fetchall()

    def _execute_update(self, query: str, params: tuple) -> int:
        with self.db.get_cursor() as cursor:
            cursor.execute(query, params)
            return cursor.rowcount