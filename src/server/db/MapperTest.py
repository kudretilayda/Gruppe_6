import unittest
from server.db.StyleMapper import StyleMapper

class StyleMapperTest(unittest.TestCase):
    def setUp(self):
        self.mapper = StyleMapper()
        self.test_style = StyleMapper()
        self.test_style.set_style_name("Test Style")

    def test_insert(self):
        saved_style = self.mapper.insert(self.test_style)
        self.assertIsNotNone(saved_style.get_id())