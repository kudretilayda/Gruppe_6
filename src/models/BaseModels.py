# src/models/base.py
from abc import ABC
from datetime import datetime
from typing import Dict, Any, Optional
import json

class BaseModel(ABC):
    """Abstract base class for all models"""
    def __init__(self):
        self._id: Optional[int] = None
        self._created_at: datetime = datetime.now()
        self._modified_at: datetime = datetime.now()

    @property
    def id(self) -> Optional[int]:
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = value

    @property
    def created_at(self) -> datetime:
        return self._created_at

    @property
    def modified_at(self) -> datetime:
        return self._modified_at

    def to_dict(self) -> Dict[str, Any]:
        return {
            'id': self._id,
            'created_at': self._created_at.isoformat(),
            'modified_at': self._modified_at.isoformat()
        }

    def from_dict(self, data: Dict[str, Any]) -> 'BaseModel':
        if 'id' in data:
            self._id = data['id']
        if 'created_at' in data:
            self._created_at = datetime.fromisoformat(data['created_at'])
        if 'modified_at' in data:
            self._modified_at = datetime.fromisoformat(data['modified_at'])
        return self

    def __str__(self) -> str:
        return json.dumps(self.to_dict(), indent=2)
