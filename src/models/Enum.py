from enum import Enum

class ClothingCategory(Enum):
    """Enumeration of clothing categories"""
    TOP = "TOP"
    BOTTOM = "BOTTOM"
    DRESS = "DRESS"
    OUTERWEAR = "OUTERWEAR"
    FOOTWEAR = "FOOTWEAR"
    ACCESSORY = "ACCESSORY"

class Season(Enum):
    """Enumeration of seasons"""
    SPRING = "SPRING"
    SUMMER = "SUMMER"
    FALL = "FALL"
    WINTER = "WINTER"

class Occasion(Enum):
    """Enumeration of occasions"""
    CASUAL = "CASUAL"
    BUSINESS = "BUSINESS"
    FORMAL = "FORMAL"
    SPORT = "SPORT"
    PARTY = "PARTY"