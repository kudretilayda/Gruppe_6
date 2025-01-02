import unittest
from datetime import datetime
from src.server.test.ConstraintRuletest import ConstraintRule, ConstraintType

class TestConstraintRule(unittest.TestCase):
    def setUp(self):
        self.constraint = ConstraintRule()
        self.test_id = "test123"
        self.test_style_id = "style123"
        self.test_type = ConstraintType.BINARY

    def test_basic_attributes(self):
        self.constraint.set_id(self.test_id)
        self.constraint.set_style_id(self.test_style_id)
        self.constraint.set_constraint_type(self.test_type)

        self.assertEqual(self.constraint.get_id(), self.test_id)
        self.assertEqual(self.constraint.get_style_id(), self.test_style_id)
        self.assertEqual(self.constraint.get_constraint_type(), self.test_type)

    def test_to_dict(self):
        self.constraint.set_id(self.test_id)
        self.constraint.set_style_id(self.test_style_id)
        self.constraint.set_constraint_type(self.test_type)

        d = self.constraint.to_dict()
        self.assertEqual(d['id'], self.test_id)
        self.assertEqual(d['style_id'], self.test_style_id)
        self.assertEqual(d['constraint_type'], "binary")

    def test_from_dict(self):
        test_dict = {
            'id': self.test_id,
            'style_id': self.test_style_id,
            'constraint_type': 'binary',
            'created_at': '2024-01-01T12:00:00'
        }

        constraint = ConstraintRule.from_dict(test_dict)
        self.assertEqual(constraint.get_id(), self.test_id)
        self.assertEqual(constraint.get_style_id(), self.test_style_id)
        self.assertEqual(constraint.get_constraint_type(), ConstraintType.BINARY)

if __name__ == '__main__':
    unittest.main()