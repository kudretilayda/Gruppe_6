import unittest
from ..bo.Constraints import Constraint
#from src.server.bo.Constraint import Constraint
from ..bo.Constraints.Mutex import MutexConstraint
#from src.server.bo.MutexConstraint import MutexConstraint


# Dummy-Klasse für die zu testenden Objekte
class TestObject:
    def __init__(self, attribute, value):
        self.attribute = attribute
        self.value = value

    def get_attribute(self):
        return self.attribute

    def get_value(self):
        return self.value


class TestMutexConstraint(unittest.TestCase):
    def setUp(self):
        # Testobjekte erstellen
        self.obj1 = TestObject("color", "red")
        self.obj2 = TestObject("color", "blue")

        # MutexConstraint-Instanz erstellen
        self.mutex_constraint = MutexConstraint(self.obj1, self.obj2)

    def test_get_and_set_object1(self):
        new_obj = TestObject("size", "large")
        self.mutex_constraint.set_object1(new_obj)
        self.assertEqual(self.mutex_constraint.get_object1(), new_obj)

    def test_get_and_set_object2(self):
        new_obj = TestObject("shape", "circle")
        self.mutex_constraint.set_object2(new_obj)
        self.assertEqual(self.mutex_constraint.get_object2(), new_obj)

    def test_auswerten_true(self):
        # obj1 und obj2 haben unterschiedliche Werte
        result = self.mutex_constraint.auswerten(None)
        self.assertTrue(result)

    def test_auswerten_false(self):
        # obj1 und obj2 haben denselben Wert
        self.obj1.value = "blue"  # Beide Objekte haben jetzt denselben Wert
        result = self.mutex_constraint.auswerten(None)
        self.assertFalse(result)

    def test_to_string(self):
        expected_str = (
            "MutexConstraint: "
            "Object1: (color, red), "
            "Object2: (color, blue)"
        )
        self.assertEqual(str(self.mutex_constraint), expected_str)

    def test_from_dict(self):
        # Testdaten
        test_data = {
            "object1": self.obj1,
            "object2": self.obj2
        }
        mutex_constraint = MutexConstraint.from_dict(test_data)
        self.assertEqual(mutex_constraint.get_object1(), self.obj1)
        self.assertEqual(mutex_constraint.get_object2(), self.obj2)


if __name__ == "__main__":
    unittest.main()
