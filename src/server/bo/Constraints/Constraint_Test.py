from ..ClothingType import ClothingType
from ..Style import Style
from ..Outfit import Outfit
from ..ClothingItem import ClothingItem

from Unary import UnaryConstraint
from Binary import BinaryConstraint
from Implication import ImplicationConstraint
from Cardinality import CardinalityConstraint
from Mutex import MutexConstraint

# Vorgefertigte Instanzen --------------------------------------------------------------------------------------
pulli = ClothingType()
style1 = Style()
Rollkragenpulli = ClothingItem()
outfit1 = Outfit()

sporthose = ClothingType()
style2 = Style()
jogginghose = ClothingItem()
outfit2 = Outfit()

# Beziehungen
Rollkragenpulli.clothing_type = pulli
outfit1.item = [Rollkragenpulli]
outfit1.set_style(style1)
style1.set_clothing_type(pulli)

jogginghose.clothing_type = sporthose
outfit2.item = [jogginghose]
outfit2.set_style(style1)
style2.set_clothing_type(sporthose)


# Unary----------------------------------------------------------------------------------------------
print('Unary Constraint:')
unary_true = UnaryConstraint()
style1.style_constraints.append(unary_true)
unary_false = UnaryConstraint()
style2.style_constraints.append(unary_false)
print('Fall 1 (True): ', unary_true.validate(outfit1))
print('Fall 2 (False): ', unary_false.validate(outfit2), '\n')


# Binary ----------------------------------------------------------------------------------------------
print('Binary Constraint:')
# Rollkragenpulli, pulli, style1, outfit1
# Jogginghose, sporthose, style2, outfit2

hose = ClothingType()
Jeans = ClothingItem()

# Beziehungen
Jeans.clothing_type = hose
outfit1.items = [Rollkragenpulli, Jeans]
style1.set_clothing_type(hose)
style3 = Style()
style3.set_clothing_type(sporthose)

# Constraint
binary_false = BinaryConstraint(Rollkragenpulli, jogginghose)
style1.style_constraints.append(binary_false)

binary_true = BinaryConstraint(Rollkragenpulli, Jeans)
style3.style_constraints.append(binary_true)

print(binary_false.validate())
print(binary_true.validate(), '\n')


# Implication ----------------------------------------------------------------------------------------------
print('Implication Constraint:')
# Implikation Constraint erstellen und zum Style hinzufügen
implication_constraint = ImplicationConstraint(pulli, hose)
style1.style_constraints.append(implication_constraint)
# Validierung
print(implication_constraint.validate(outfit1), '\n')


# Cardinality ----------------------------------------------------------------------------------------------
print('Cardinality Constraint:')
Jeans.selected = True
jogginghose.selected = True
cardinality_true = CardinalityConstraint([Jeans], 1, 1)
cardinality_false = CardinalityConstraint([Jeans], 2, 1)
print(cardinality_true.validate())
print(cardinality_false.validate(), '\n')


# Mutex ----------------------------------------------------------------------------------------------
print('Mutex Constraint:')
outfit1.set_items(Jeans)
outfit1.set_items(Rollkragenpulli)

outfit2.set_items(Jeans)
outfit2.set_items(jogginghose)
mutex_constraint = MutexConstraint(mutex=[(Jeans, jogginghose)])
print(mutex_constraint.validate(outfit1))
print(mutex_constraint.validate(outfit2))
