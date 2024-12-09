# test/BinaryConstraintTest.py
import unittest
from server.bo.BinaryConstraint import BinaryConstraint

class BinaryConstraintTest(unittest.TestCase):
    def setUp(self):
        self.constraint = BinaryConstraint()
        self.constraint.set_style_id("style1")
        self.constraint.set_reference_object1_id("obj1")
        self.constraint.set_reference_object2_id("obj2")

    def test_binary_constraint_basics(self):
        self.assertEqual(self.constraint.get_style_id(), "style1")
        self.assertEqual(self.constraint.get_reference_object1_id(), "obj1")
        self.assertEqual(self.constraint.get_reference_object2_id(), "obj2")
        self.assertEqual(self.constraint.get_constraint_type(), "binary")

class BinaryConstraintMapperTest(unittest.TestCase):
    def setUp(self):
        self.mapper = BinaryConstraintMapperTest()
        self.test_constraint = BinaryConstraint()
        self.test_constraint.set_style_id("test_style")
        self.test_constraint.set_reference_object1_id("test_obj1")
        self.test_constraint.set_reference_object2_id("test_obj2")

    def test_insert(self):
        saved_constraint = self.mapper.insert(self.test_constraint)
        self.assertIsNotNone(saved_constraint.get_id())