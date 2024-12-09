import unittest
from server.bo.MutexConstraint import MutexConstraint

class MutexConstraintTest(unittest.TestCase):
    def setUp(self):
        self.constraint = MutexConstraint()
        self.constraint.set_style_id("style1")
        self.constraint.set_excluded_types(["type1", "type2"])

    def test_mutex_constraint_basics(self):
        self.assertEqual(self.constraint.get_style_id(), "style1")
        self.assertEqual(len(self.constraint.get_excluded_types()), 2)
        self.assertEqual(self.constraint.get_constraint_type(), "mutex")

    def test_add_excluded_type(self):
        self.constraint.add_excluded_type("type3")
        self.assertEqual(len(self.constraint.get_excluded_types()), 3)