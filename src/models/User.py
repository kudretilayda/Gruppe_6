from datetime import datetime
from typing import Dict, Any, Optional
from .BaseModels import BaseModel

class Person(BaseModel):
    """Person model class"""
    def __init__(self):
        super().__init__()
        self._google_id: str = ""
        self._email: str = ""
        self._first_name: str = ""
        self._last_name: str = ""
        self._nickname: Optional[str] = None

    @property
    def google_id(self) -> str:
        return self._google_id

    @google_id.setter
    def google_id(self, value: str):
        self._google_id = value

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str):
        self._email = value

    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, value: str):
        self._first_name = value

    @property
    def last_name(self) -> str:
        return self._last_name

    @last_name.setter
    def last_name(self, value: str):
        self._last_name = value

    @property
    def nickname(self) -> Optional[str]:
        return self._nickname

    @nickname.setter
    def nickname(self, value: Optional[str]):
        self._nickname = value

    def to_dict(self) -> Dict[str, Any]:
        data = super().to_dict()
        data.update({
            'google_id': self._google_id,
            'email': self._email,
            'first_name': self._first_name,
            'last_name': self._last_name,
            'nickname': self._nickname
        })
        return data

    def from_dict(self, data: Dict[str, Any]) -> 'Person':
        super().from_dict(data)
        self._google_id = data.get('google_id', '')
        self._email = data.get('email', '')
        self._first_name = data.get('first_name', '')
        self._last_name = data.get('last_name', '')
        self._nickname = data.get('nickname')
        return self