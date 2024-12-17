from src.server.bo.ClothingItem import ClothingItem
from src.server.bo.ClothingType import ClothingType
from src.server.bo.Style import Style
from src.server.bo.Outfit import Outfit
from src.server.bo.Constraints import Constraint, Mutex

# Kleidungstypen erstellen
shirt_type = ClothingType("Shirt", "Upper body")
pants_type = ClothingType("Pants", "Lower body")
dress_type = ClothingType("Dress", "Full body")

# Style erstellen
casual_style = Style("Casual")
casual_style.add_clothing_type(shirt_type)
casual_style.add_clothing_type(pants_type)

# Constraint hinzufügen: Kleid und Hose schließen sich aus
mutex_constraint = Mutex(dress_type, pants_type)
casual_style.constraint.append(mutex_constraint)

# Konkrete Kleidungsstücke erstellen
blue_shirt = ClothingItem("Blue Shirt", shirt_type)
black_pants = ClothingItem("Black Pants", pants_type)

# Outfit erstellen
my_outfit = Outfit("My Casual Outfit", casual_style)
my_outfit.add_item(blue_shirt)
my_outfit.add_item(black_pants)

# Outfit validieren
is_valid = my_outfit.validate_integrity()
print(f"Outfit is valid: {is_valid}")