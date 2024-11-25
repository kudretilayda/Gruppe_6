from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List
import uuid

@dataclass
class Person:
    id: str
    google_id: str
    firstname: str
    lastname: str
    nickname: Optional[str] = None
    created_at: datetime = datetime.now()

    @classmethod
    def create(cls, google_id: str, firstname: str, lastname: str, nickname: Optional[str] = None) -> 'Person':
        return cls(
            id=str(uuid.uuid4()),
            google_id=google_id,
            firstname=firstname,
            lastname=lastname,
            nickname=nickname
        )

@dataclass
class Wardrobe:
    id: str
    owner_id: str
    name: str
    created_at: datetime = datetime.now()

    @classmethod
    def create(cls, owner_id: str, name: str) -> 'Wardrobe':
        return cls(
            id=str(uuid.uuid4()),
            owner_id=owner_id,
            name=name
        )

@dataclass
class ClothingType:
    id: str
    name: str
    description: str
    category: str
    created_at: datetime = datetime.now()

    @classmethod
    def create(cls, name: str, description: str, category: str) -> 'ClothingType':
        return cls(
            id=str(uuid.uuid4()),
            name=name,
            description=description,
            category=category
        )

@dataclass
class ClothingItem:
    id: str
    wardrobe_id: str
    type_id: str
    name: str
    color: Optional[str] = None
    brand: Optional[str] = None
    season: Optional[str] = None
    created_at: datetime = datetime.now()

    @classmethod
    def create(cls, wardrobe_id: str, type_id: str, name: str, 
               color: Optional[str] = None, brand: Optional[str] = None, 
               season: Optional[str] = None) -> 'ClothingItem':
        return cls(
            id=str(uuid.uuid4()),
            wardrobe_id=wardrobe_id,
            type_id=type_id,
            name=name,
            color=color,
            brand=brand,
            season=season
        )

@dataclass
class Style:
    id: str
    name: str
    description: str
    created_by: str
    created_at: datetime = datetime.now()

    @classmethod
    def create(cls, name: str, description: str, created_by: str) -> 'Style':
        return cls(
            id=str(uuid.uuid4()),
            name=name,
            description=description,
            created_by=created_by
        )

@dataclass
class StyleConstraint:
    id: str
    style_id: str
    constraint_type: str
    first_type_id: str
    second_type_id: Optional[str] = None
    created_at: datetime = datetime.now()

    @classmethod
    def create(cls, style_id: str, constraint_type: str, 
               first_type_id: str, second_type_id: Optional[str] = None) -> 'StyleConstraint':
        return cls(
            id=str(uuid.uuid4()),
            style_id=style_id,
            constraint_type=constraint_type,
            first_type_id=first_type_id,
            second_type_id=second_type_id
        )

@dataclass
class Outfit:
    id: str
    name: str
    style_id: Optional[str]
    created_by: str
    items: List[str]  # Liste von clothing_item_ids
    created_at: datetime = datetime.now()

    @classmethod
    def create(cls, name: str, created_by: str, items: List[str], 
               style_id: Optional[str] = None) -> 'Outfit':
        return cls(
            id=str(uuid.uuid4()),
            name=name,
            style_id=style_id,
            created_by=created_by,
            items=items
        )