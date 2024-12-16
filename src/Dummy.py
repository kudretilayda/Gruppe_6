from src.server.bo.User import User
from src.server.bo.Wardrobe import Wardrobe
from src.server.bo.ClothingItem import ClothingItem
from src.server.bo.ClothingType import ClothingType
from src.server.bo.Outfit import Outfit
from src.server.bo.Style import Style

from src.server.db.UserMapper import UserMapper
from src.server.db.WardrobeMapper import WardrobeMapper
from src.server.db.ClothingItemMapper import ClothingItemMapper
from src.server.db.ClothingTypeMapper import ClothingTypeMapper
from src.server.db.OutfitMapper import OutfitMapper
from src.server.db.StyleMapper import StyleMapper

from src.server.db.ConstraintMapper import ConstraintMapper
from src.server.bo.Constraints import (UnaryConstraint, BinaryConstraint,
                                       ImplicationConstraint, MutexConstraint, CardinalityConstraint)

from src.server.bo.RuleEngine import RuleEngine

# Erstellen User
jar_jar_binks = User()
jar_jar_binks.set_id(1)
jar_jar_binks.set_email('<EMAIL>')
jar_jar_binks.set_firstname('Jar Jar')
jar_jar_binks.set_lastname('Binks')

# Erstellen Kleiderschrank
mein_kleiderschrank = Wardrobe()
mein_kleiderschrank.set_id(1)
mein_kleiderschrank.set_wardrobe_owner(jar_jar_binks)

# Erstellen Kleidungstypen
normal = ClothingType()
normal.set_id(1)
normal.set_name('normal')
normal.set_usage('alles')

entspannt = ClothingType()
entspannt.set_id(2)
entspannt.set_name('entspannt')
entspannt.set_usage('chillen')

# Erstellen Kleidungsstücke
Hemd = ClothingItem()
Hemd.set_id(1)
Hemd.set_item_name('Hemd')
Hemd.set_clothing_type(normal)
Hemd.set_wardrobe_id(1)

JoggingHose= ClothingItem()
JoggingHose.set_id(2)
JoggingHose.set_item_name('JoggingHose')
JoggingHose.set_clothing_type(entspannt)
JoggingHose.set_wardrobe_id(1)

Jeans = ClothingItem()
Jeans.set_id(3)
Jeans.set_item_name('Jeans')
Jeans.set_clothing_type(normal)
Jeans.set_wardrobe_id(1)

a = Style()
a.set_id(1)
a.set_name('a')
