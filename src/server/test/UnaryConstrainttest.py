import unittest
from src.server.bo.Constraint import Constraint
from src.server.bo.UnaryConstraint import UnaryConstraint


# Dummy-Klasse für das zu testende Objekt
class TestObject:
    def __init__(self, attribute, value):
        self.attribute = attribute
        self.value = value

    def get_attribute(self):
        return self.attribute

    def get_value(self):
        return self.value


class TestUnaryConstraint(unittest.TestCase):
    def setUp(self):
        # Testobjekt erstellen
        self.test_obj = TestObject("color", "red")

        # Bedingung für den UnaryConstraint
        self.condition = lambda obj: obj.get_value() == "red"

        # UnaryConstraint-Instanz erstellen
        self.unary_constraint = UnaryConstraint(self.test_obj, self.condition)

    def test_get_and_set_obj(self):
        # Neues Testobjekt setzen
        new_obj = TestObject("size", "large")
        self.unary_constraint.set_obj(new_obj)
        self.assertEqual(self.unary_constraint.get_obj(), new_obj)

    def test_get_and_set_condition(self):
        # Neue Bedingung setzen
        new_condition = lambda obj: obj.get_value() == "blue"
        self.unary_constraint.set_condition(new_condition)
        self.assertEqual(self.unary_constraint.get_condition(), new_condition)

    def test_auswerten_success(self):
        # Bedingung wird erfüllt (Value ist "red")
        self.unary_constraint.auswerten(self.test_obj)  # Sollte kein Fehler werfen

    def test_auswerten_failure(self):
        # Bedingung wird nicht erfüllt (Value ist nicht "blue")
        self.test_obj.value = "blue"
        with self.assertRaises(ValueError) as context:
            self.unary_constraint.auswerten(self.test_obj)

        self.assertEqual(
            str(context.exception),
            f"Constraint verletzt für Bezugsobjekt: {self.test_obj}."
        )


if __name__ == "__main__":
    unittest.main()
