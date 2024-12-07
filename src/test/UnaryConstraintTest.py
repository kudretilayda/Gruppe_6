import unittest
from server.bo.UnaryConstraint import UnaryConstraint

class UnaryConstraintTest(unittest.TestCase):
    def setUp(self):
        self.constraint = UnaryConstraint()
        self.constraint.set_style_id("style1")
        self.constraint.set_reference_object_id("obj1")

    def test_unary_constraint_basics(self):
        self.assertEqual(self.constraint.get_style_id(), "style1")
        self.assertEqual(self.constraint.get_reference_object_id(), "obj1")
        self.assertEqual(self.constraint.get_constraint_type(), "unary")

class UnaryConstraintMapperTest(unittest.TestCase):
    def setUp(self):
        self.mapper = UnaryConstraintMapperTest()
        self.test_constraint = UnaryConstraint()
        self.test_constraint.set_style_id("test_style")
        self.test_constraint.set_reference_object_id("test_obj")

    def test_insert(self):
        saved_constraint = self.mapper.insert(self.test_constraint)
        self.assertIsNotNone(saved_constraint.get_id())