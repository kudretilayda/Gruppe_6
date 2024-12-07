import unittest
from server.bo.Style import Style

class StyleTest(unittest.TestCase):
    def setUp(self):
        self.style = Style()
        self.style.set_style_name("Casual")
        self.style.set_created_by("user1")

    def test_style_basics(self):
        self.assertEqual(self.style.get_style_name(), "Casual")
        self.assertEqual(self.style.get_created_by(), "user1")

# test/MapperTest.py
import unittest
from server.db.StyleMapper import StyleMapper

class StyleMapperTest(unittest.TestCase):
    def setUp(self):
        self.mapper = StyleMapper()
        self.test_style = Style()
        self.test_style.set_style_name("Test Style")

    def test_insert(self):
        saved_style = self.mapper.insert(self.test_style)
        self.assertIsNotNone(saved_style.get_id())