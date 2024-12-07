import unittest
from server.bo.ImplicationConstraint import ImplikationConstraint

class ImplikationConstraintTest(unittest.TestCase):
    def setUp(self):
        self.constraint = ImplikationConstraint()
        self.constraint.set_style_id("style1")
        self.constraint.set_if_type_id("object1")
        self.constraint.set_then_type_id("object2")

    def test_implication_constraint_basics(self):
        self.assertEqual(self.constraint.get_style_id(), "style1")
        self.assertEqual(self.constraint.get_if_type_id(), "object1")
        self.assertEqual(self.constraint.get_then_type_id(), "objedt2")
        self.assertEqual(self.constraint.get_constraint_type(), "implikation")