from src.server.bo.ClothingType import ClothingType
from src.server.bo.ClothingItem import ClothingItem
from src.server.bo.Wardrobe import Wardrobe
from src.server.bo.User import User
from src.server.bo.Outfit import Outfit
from src.server.bo.Style import Style


class ConstraintRule:
    """
    Basisklasse für Constraints, die auf einen Style angewendet werden können.
    """
    def __init__(self, style_id: int, constraint_type: str, attribute: str, condition: str, value: str):
        self.style_id = style_id
        self.constraint_type = constraint_type
        self.attribute = attribute
        self.condition = condition
        self.value = value

    def validate(self, *args, **kwargs):
        """
        Muss in den Subklassen implementiert werden.
        """
        raise NotImplementedError("Die Methode 'validate' muss in einer Subklasse implementiert werden.")

    def __str__(self):
        return (f"ConstraintRule: Style ID={self.style_id}, Type={self.constraint_type}, "
                f"Attribute={self.attribute}, Condition={self.condition}, Value={self.value}")


class UnaryConstraint(ConstraintRule):
    """
    Einschränkungen, die auf ein einzelnes Objekt angewendet werden.
    """
    def __init__(self, style_id: int, reference_object, attribute: str, condition: str, value: str):
        super().__init__(style_id, "unary", attribute, condition, value)
        self.reference_object = reference_object

    def validate(self):
        """
        Überprüft, ob das referenzierte Objekt die Bedingung erfüllt.
        """
        obj_value = getattr(self.reference_object, self.attribute, None)
        if self.condition == "EQUAL" and obj_value != self.value:
            raise ValueError(f"UnaryConstraint verletzt: {self.attribute} muss {self.value} sein.")
        if self.condition == "NOT EQUAL" and obj_value == self.value:
            raise ValueError(f"UnaryConstraint verletzt: {self.attribute} darf nicht {self.value} sein.")
        return True


class BinaryConstraint(ConstraintRule):
    """
    Einschränkungen, die zwischen zwei Objekten bestehen.
    """
    def __init__(self, style_id: int, object1, object2, attribute: str, condition: str, value: str):
        super().__init__(style_id, "binary", attribute, condition, value)
        self.object1 = object1
        self.object2 = object2

    def validate(self):
        """
        Überprüft die Beziehung zwischen den beiden Objekten.
        """
        obj1_value = getattr(self.object1, self.attribute, None)
        obj2_value = getattr(self.object2, self.attribute, None)

        if self.condition == "NOT EQUAL" and obj1_value == obj2_value:
            raise ValueError(f"BinaryConstraint verletzt: {self.object1} und {self.object2} "
                             f"dürfen nicht dieselbe {self.attribute} haben.")
        return True


class ImplikationConstraint(ConstraintRule):
    """
    Repräsentiert eine logische Implikation: Wenn A, dann B.
    """
    def __init__(self, style_id: int, condition_a, condition_b):
        super().__init__(style_id, "implication", None, None, None)
        self.condition_a = condition_a
        self.condition_b = condition_b

    def validate(self):
        """
        Überprüft, ob die Implikation gültig ist.
        """
        if self.condition_a() and not self.condition_b():
            raise ValueError("Implikationsconstraint verletzt: Bedingung A erfüllt, aber Bedingung B nicht.")
        return True


class MutexConstraint(ConstraintRule):
    """
    Gegenseitiger Ausschluss: Zwei oder mehr Objekte dürfen nicht gleichzeitig ausgewählt werden.
    """
    def __init__(self, style_id: int, objects: list):
        super().__init__(style_id, "mutex", None, None, None)
        self.objects = objects

    def validate(self):
        """
        Überprüft, ob nicht mehr als ein Objekt ausgewählt ist.
        """
        selected = [obj for obj in self.objects if obj.is_selected()]
        if len(selected) > 1:
            raise ValueError("MutexConstraint verletzt: Mehr als ein Objekt ist ausgewählt.")
        return True


class CardinalityConstraint(ConstraintRule):
    """
    Einschränkungen bezüglich der Anzahl der Objekte in einer Gruppe.
    """
    def __init__(self, style_id: int, objects: list, min_count: int, max_count: int):
        super().__init__(style_id, "cardinality", None, None, None)
        self.objects = objects
        self.min_count = min_count
        self.max_count = max_count

    def validate(self):
        """
        Überprüft, ob die Anzahl der ausgewählten Objekte innerhalb des erlaubten Bereichs liegt.
        """
        count = sum(1 for obj in self.objects if obj.is_selected())
        if count < self.min_count or count > self.max_count:
            raise ValueError(f"CardinalityConstraint verletzt: {count} Objekte ausgewählt, "
                             f"erlaubt sind zwischen {self.min_count} und {self.max_count}.")
        return True


# Datenbankreferenzen
# clothing_type = ClothingType(id=3, type_name="T-Shirt", type_usage="Sommerbekleidung")
clothing_type = ClothingType().set_id(3)
clothing_type = ClothingType().set_name('T-Shirt')
clothing_type = ClothingType().set_usage('Sommer')

constraint = UnaryConstraint(style_id=1, reference_object=clothing_type,
                              attribute="type_usage", condition="NOT EQUAL", value="Sommer")
constraint.validate()


jacke = ClothingType().set_id(1)
jacke = ClothingType().set_name('Jacke')
jacke = ClothingType().set_usage('Winterjacke')

hose = ClothingType().set_id(2)
hose = ClothingType().set_name('Chino')
hose = ClothingType().set_usage('Business Casual')

constraint = BinaryConstraint(style_id=2, object1=jacke, object2=hose,
                               attribute="type_name", condition="EQUAL", value="Gelb")
constraint.validate()
