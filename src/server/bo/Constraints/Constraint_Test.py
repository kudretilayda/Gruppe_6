from src.server.bo.ClothingType import ClothingType
from src.server.bo.Style import Style
from src.server.bo.Outfit import Outfit
from src.server.bo.ClothingItem import ClothingItem

from Unary import UnaryConstraint
from Binary import BinaryConstraint
from Implication import ImplicationConstraint
from Cardinality import CardinalityConstraint


# Unary
print('Unary Constraint:')
pulli = ClothingType()
style1 = Style()
Rollkragenpulli = ClothingItem()
outfit1 = Outfit()
# Beziehungen
Rollkragenpulli.clothing_type = pulli
outfit1.item = [Rollkragenpulli]
outfit1.set_style(style1)
style1.set_clothing_type(pulli)
# Constrain
constraint = UnaryConstraint()
style1.style_constraints.append(constraint)
print(constraint.validate(outfit1), '\n')


# Binary
print('Binary Constraint:')
pulli = ClothingType()
hose = ClothingType()
style1 = Style()
Rollkragenpulli = ClothingItem()
Jeans = ClothingItem()
outfit1 = Outfit()
# Beziehungen
Rollkragenpulli.clothing_type = pulli
Jeans.clothing_type = hose
outfit1.items = [Rollkragenpulli, Jeans]
outfit1.set_style(style1)
style1.set_clothing_type(pulli)
style1.set_clothing_type(hose)
jogginghose = ClothingItem()
jogginghose.clothing_type = hose
st2 = Style()
st2.set_clothing_type(jogginghose)
# Constraint
binary_constraint = BinaryConstraint(Rollkragenpulli, jogginghose)
style1.style_constraints.append(binary_constraint)
print(binary_constraint.validate(), '\n')

# Implication
print('Implication Constraint:')
pulli = ClothingType()
hose = ClothingType()
style1 = Style()
Rollkragenpulli = ClothingItem()
Jeans = ClothingItem()
outfit1 = Outfit()
# Beziehungen
Rollkragenpulli.clothing_type = pulli
Jeans.clothing_type = hose
outfit1.items = [Rollkragenpulli, Jeans]
outfit1.set_style(style1)
style1.set_clothing_type(pulli)
style1.set_clothing_type(hose)
# Implikation Constraint erstellen und zum Style hinzufügen
implication_constraint = ImplicationConstraint(pulli, hose)
style1.style_constraints.append(implication_constraint)
# Validierung
print(implication_constraint.validate(outfit1), '\n')


# Cardinality
print('Cardinality Constraint:')
anzughose = ClothingItem()
anzughose.name = 'Anzughose'
anzughose.selected = True
hose = ClothingItem()
hose.name = 'Hose'
hose.selected = True
cardinality_constraint = CardinalityConstraint([anzughose], 1, 1)
print(cardinality_constraint.validate(), '\n')

# Mutex
print('Mutex Constraint:')
print('\n')