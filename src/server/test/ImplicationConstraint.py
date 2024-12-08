import unittest
from datetime import datetime
from ConstraintRule import ConstraintRule
from src.server.test.ImplicationConstraint import ConstraintRule

class TestImplication(unittest.TestCase):
    
    def setUp(self):
        self.implication = Implication()  # type: ignore
        self.implication.set_id("123")
        self.implication.set_style_id("456")
        self.implication.set_if_clothing_type_id("shirt")
        self.implication.set_then_clothing_type_id("jacket")
        self.implication.set_created_at(datetime(2023, 12, 8))
        self.implication.set_constraint_type(ConstraintRule("mandatory"))

    def test_get_and_set_if_clothing_type_id(self):
        self.implication.set_if_clothing_type_id("pants")
        self.assertEqual(self.implication.get_if_clothing_type_id(), "pants")

    def test_get_and_set_then_clothing_type_id(self):
        self.implication.set_then_clothing_type_id("shoes")
        self.assertEqual(self.implication.get_then_clothing_type_id(), "shoes")

    def test_to_dict(self):
        expected = {
            'id': "123",
            'style_id': "456",
            'if_clothing_type_id': "shirt",
            'then_clothing_type_id': "jacket",
            'constraint_type': "mandatory",
            'created_at': "2023-12-08T00:00:00"
        }
        self.assertEqual(self.implication.to_dict(), expected)

    def test_from_dict(self):
        data = {
            'id': "789",
            'style_id': "101112",
            'if_clothing_type_id': "hat",
            'then_clothing_type_id': "scarf",
            'constraint_type': "optional",
            'created_at': "2023-12-07T12:30:45"
        }
        implication_obj = Implication.from_dict(data)  # type: ignore
        self.assertEqual(implication_obj.get_id(), "789")
        self.assertEqual(implication_obj.get_style_id(), "101112")
        self.assertEqual(implication_obj.get_if_clothing_type_id(), "hat")
        self.assertEqual(implication_obj.get_then_clothing_type_id(), "scarf")
        self.assertEqual(implication_obj.get_constraint_type().get_id(), "optional")
        self.assertEqual(implication_obj.get_created_at(), datetime(2023, 12, 7, 12, 30, 45))

if __name__ == "__main__":
    unittest.main()